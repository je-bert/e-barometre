import { Router } from "express";
import { put } from "./answer.controllers";

const router = Router();

router.route("/").put(put);

export default router;
