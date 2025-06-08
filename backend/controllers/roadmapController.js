const Roadmap = require('../models/Roadmap');

exports.getAllRoadmaps = async (req, res) => {
  try {
    const roadmaps = await Roadmap.find();
    res.json(roadmaps);
  } catch (error) {
    console.error('Get roadmaps error:', error);
    res.status(500).json({ message: 'Error fetching roadmaps' });
  }
};

exports.getRoadmapByGoal = async (req, res) => {
  const { goal } = req.body;
  if (!goal) return res.status(400).json({ message: 'Goal is required' });

  try {
    const roadmap = await Roadmap.findOne({ goal: goal.toLowerCase() });
    if (!roadmap) return res.status(404).json({ message: 'Roadmap not found' });
    res.json(roadmap);
  } catch (error) {
    console.error('Get roadmap by goal error:', error);
    res.status(500).json({ message: 'Error fetching roadmap' });
  }
};
