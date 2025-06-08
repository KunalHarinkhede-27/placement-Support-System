const User = require('../models/User');
const Roadmap = require('../models/Roadmap');
const JobMatch = require('../models/Jobmatch');

exports.getDashboardData = async (req, res) => {
  try {
    // For demo: count users, jobs, roadmaps
    const userCount = await User.countDocuments();
    const jobCount = await JobMatch.countDocuments();
    const roadmapCount = await Roadmap.countDocuments();

    res.json({ userCount, jobCount, roadmapCount });
  } catch (error) {
    console.error('Admin dashboard error:', error);
    res.status(500).json({ message: 'Error fetching dashboard data' });
  }
};

exports.getAllUsers = async (req, res) => {
  try {
    const users = await User.find().select('-password'); // no passwords
    res.json(users);
  } catch (error) {
    console.error('Admin get users error:', error);
    res.status(500).json({ message: 'Error fetching users' });
  }
};

// Roadmap management
exports.createRoadmap = async (req, res) => {
  try {
    const roadmap = new Roadmap(req.body);
    await roadmap.save();
    res.json(roadmap);
  } catch (error) {
    console.error('Create roadmap error:', error);
    res.status(500).json({ message: 'Error creating roadmap' });
  }
};

exports.updateRoadmap = async (req, res) => {
  try {
    const roadmap = await Roadmap.findByIdAndUpdate(req.params.id, req.body, { new: true });
    if (!roadmap) return res.status(404).json({ message: 'Roadmap not found' });
    res.json(roadmap);
  } catch (error) {
    console.error('Update roadmap error:', error);
    res.status(500).json({ message: 'Error updating roadmap' });
  }
};

exports.deleteRoadmap = async (req, res) => {
  try {
    const roadmap = await Roadmap.findByIdAndDelete(req.params.id);
    if (!roadmap) return res.status(404).json({ message: 'Roadmap not found' });
    res.json({ message: 'Roadmap deleted' });
  } catch (error) {
    console.error('Delete roadmap error:', error);
    res.status(500).json({ message: 'Error deleting roadmap' });
  }
};

// Job management
exports.createJob = async (req, res) => {
  try {
    const job = new JobMatch(req.body);
    await job.save();
    res.json(job);
  } catch (error) {
    console.error('Create job error:', error);
    res.status(500).json({ message: 'Error creating job' });
  }
};

exports.updateJob = async (req, res) => {
  try {
    const job = await JobMatch.findByIdAndUpdate(req.params.id, req.body, { new: true });
    if (!job) return res.status(404).json({ message: 'Job not found' });
    res.json(job);
  } catch (error) {
    console.error('Update job error:', error);
    res.status(500).json({ message: 'Error updating job' });
  }
};

exports.deleteJob = async (req, res) => {
  try {
    const job = await JobMatch.findByIdAndDelete(req.params.id);
    if (!job) return res.status(404).json({ message: 'Job not found' });
    res.json({ message: 'Job deleted' });
  } catch (error) {
    console.error('Delete job error:', error);
    res.status(500).json({ message: 'Error deleting job' });
  }
};
