const mongoose = require('mongoose');

const ResumeScoreSchema = new mongoose.Schema({
  user: { type: mongoose.Schema.Types.ObjectId, ref: 'User', required: true },
  fileUrl: { type: String, required: true },
  score: { type: Number, default: 0 }, // ATS Score or feedback score
  feedback: { type: String },
  parsedData: { type: Object }, // Parsed resume content JSON
  createdAt: { type: Date, default: Date.now },
});

module.exports = mongoose.model('ResumeScore', ResumeScoreSchema);
