const express = require("express");
const { analyzeResume } = require("../controllers/resumeController");
const { protect } = require("../middleware/auth");

const router = express.Router();
router.post("/analyze", protect(["user"]), analyzeResume);

module.exports = router;
