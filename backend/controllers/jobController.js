const JobMatch = require('../models/Jobmatch');

exports.getJobs = async (req, res) => {
  try {
    const jobs = await JobMatch.find().sort({ postedAt: -1 });
    res.json(jobs);
  } catch (error) {
    console.error('Get jobs error:', error);
    res.status(500).json({ message: 'Error fetching jobs' });
  }
};

exports.matchJobsToUserSkills = async (req, res) => {
  const { skills } = req.body;

  if (!skills || !Array.isArray(skills)) {
    return res.status(400).json({ message: 'Skills array required' });
  }

  try {
    // Find jobs where at least one skill matches user skills
    const matchedJobs = await JobMatch.find({
      skillsRequired: { $in: skills.map(s => s.toLowerCase()) }
    });

    res.json(matchedJobs);
  } catch (error) {
    console.error('Match jobs error:', error);
    res.status(500).json({ message: 'Server error matching jobs' });
  }
};
