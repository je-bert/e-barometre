import { Router } from "express";
import { getAll, getById } from "./survey.controllers";

const router = Router();

router.route("/").get(getAll);
router.route("/:id").get(getById);

export default router;
