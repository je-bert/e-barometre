const bcrypt = require("bcryptjs");
const jwt = require("jsonwebtoken");
import { db } from "../db";

export const signUp = async (req, res) => {
  try {
    const { first_name, last_name, email, phone_number, password } = req.body;

    if (!first_name || typeof first_name !== "string")
      return res.status(400).json({
        message: `'first_name' is missing or invalid`,
      });
    if (!last_name || typeof last_name !== "string")
      return res.status(400).json({
        message: `'last_name' is missing or invalid`,
      });
    if (!email || typeof email !== "string")
      return res.status(400).json({
        message: `'email' is missing or invalid`,
      });
    if (!phone_number || typeof phone_number !== "string")
      return res.status(400).json({
        message: `'phone_number' is missing or invalid`,
      });
    if (!password || typeof password !== "string")
      return res.status(400).json({
        message: `'password' is missing or invalid`,
      });

    const results = await db.all(`SELECT * FROM user WHERE email = ?`, email);

    if (results.length !== 0) {
      return res.status(400).json({ message: "User already exists" });
    }

    const salt = bcrypt.genSaltSync(10);

    const statement = await db.run(
      `INSERT INTO user (email, first_name, last_name, phone_number, password, date_created, role) VALUES (?,?,?,?,?,DATE('now'),?)`,
      email,
      first_name,
      last_name,
      phone_number,
      bcrypt.hashSync(password, salt),
      "user"
    );

    if (statement && statement.changes === 1) {
      // todo refactor jeremie  I (simon) added this one to get the token as soon as the user creates the account so we can move to dashboard asap

      const user = await db.get("SELECT * FROM user WHERE email = ?", email);

      if (!user) {
        return res
          .status(500)
          .json({ message: "error while creating the user" });
      }

      const token = jwt.sign(
        { user_id: user.user_id, email: email, role: user.role },
        "SECRET TOKEN 123",
        {
          expiresIn: "1h", // 60s = 60 seconds - (60m = 60 minutes, 2h = 2 hours, 2d = 2 days)
        }
      );

      return res.status(200).json({
        message: "The account has been created.",
        token: token,
      });
    } else {
      return res.status(400).json({
        message: "Error while creating the account.",
      });
    }
  } catch (err) {
    console.log(err);
    return res.status(500).json({
      message: "Error while creating the account.",
    });
  }
};

export const signIn = async (req, res) => {
  try {
    const { email, password } = req.body;

    if (!email || typeof email !== "string")
      return res.status(400).json({
        message: `'email' is missing or invalid`,
      });
    if (!password || typeof password !== "string")
      return res.status(400).json({
        message: `'password' is missing or invalid`,
      });

    const user = await db.get("SELECT * FROM user WHERE email = ?", email);

    if (!user || !bcrypt.compareSync(password, user.password))
      return res.status(400).json({
        message: "Invalid credentials.",
      });

    const token = jwt.sign(
      { user_id: user.user_id, email: email, role: user.role },
      process.env.JWT_SECRET,
      {
        expiresIn: "1h", // 60s = 60 seconds - (60m = 60 minutes, 2h = 2 hours, 2d = 2 days)
      }
    );

    await db.run(
      `UPDATE user SET date_logged_in = Date('now') WHERE user_id = ?;`,
      user.user_id
    );

    return res.status(200).json({
      user_id: user.user_id,
      email: email,
      first_name: user.first_name,
      last_name: user.last_name,
      token: token,
    });
  } catch (err) {
    console.log(err);
    return res.status(500).json({
      message: "Error! Please try again later.",
    });
  }
};

export const protect = async (req, res, next) => {
  const token =
    req.body.token || req.query.token || req.headers["x-access-token"];

  if (!token) {
    return res.status(401).json({ message: "Token required" });
  }
  try {
    const decoded = jwt.verify(token, process.env.JWT_SECRET);

    res.locals.user = decoded;
  } catch (err) {
    return res.status(401).json({ message: "Invalid token" });
  }
  return next();
};

export const protectAdmin = async (req, res, next) => {
  protect(req, res, async function () {
    const { role } = res.locals.user;
    if (!role || role != "admin") {
      res.status(403).json({
        message: "You don't have the right permission to access this ressource",
      });
    }
    return next();
  });
};
