const mongoose = require('mongoose');

const JobMatchSchema = new mongoose.Schema({
  title: String,
  company: String,
  description: String,
  skillsRequired: [String],
  postedAt: { type: Date, default: Date.now },
});

module.exports = mongoose.model('JobMatch', JobMatchSchema);
