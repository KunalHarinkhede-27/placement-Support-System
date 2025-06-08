const parseResume = require("../utils/parseResume");
const ResumeScore = require("../models/ResumeScore");

const analyzeResume = async (req, res) => {
  try {
    const { resumeUrl } = req.body;
    const parsed = await parseResume(resumeUrl);
    const feedback = { score: parsed.score, feedback: parsed.feedback };

    await ResumeScore.create({ userId: req.user.id, ...feedback });
    res.json(feedback);
  } catch (error) {
    res.status(500).json({ msg: error.message });
  }
};

module.exports = { analyzeResume };
