const mongoose = require('mongoose');

const RoadmapSchema = new mongoose.Schema({
  goal: { type: String, required: true },
  skills: [String],
  courses: [{
    title: String,
    link: String,
  }],
  createdAt: { type: Date, default: Date.now },
});

module.exports = mongoose.model('Roadmap', RoadmapSchema);
