const ProjectIdea = require('../models/ProjectIdea');

// Get all project ideas
exports.getAllProjects = async (req, res) => {
  try {
    const projects = await ProjectIdea.find().sort({ createdAt: -1 });
    res.json(projects);
  } catch (error) {
    console.error('Error fetching projects:', error);
    res.status(500).json({ message: 'Server error fetching projects' });
  }
};

// Get a project idea by ID
exports.getProjectById = async (req, res) => {
  try {
    const project = await ProjectIdea.findById(req.params.id);
    if (!project) return res.status(404).json({ message: 'Project not found' });
    res.json(project);
  } catch (error) {
    console.error('Error fetching project:', error);
    res.status(500).json({ message: 'Server error fetching project' });
  }
};

// Create a new project idea
exports.createProject = async (req, res) => {
  try {
    const newProject = new ProjectIdea(req.body);
    const savedProject = await newProject.save();
    res.status(201).json(savedProject);
  } catch (error) {
    console.error('Error creating project:', error);
    res.status(500).json({ message: 'Server error creating project' });
  }
};

// Update a project idea by ID
exports.updateProject = async (req, res) => {
  try {
    const updatedProject = await ProjectIdea.findByIdAndUpdate(
      req.params.id,
      req.body,
      { new: true }
    );
    if (!updatedProject) return res.status(404).json({ message: 'Project not found' });
    res.json(updatedProject);
  } catch (error) {
    console.error('Error updating project:', error);
    res.status(500).json({ message: 'Server error updating project' });
  }
};

// Delete a project idea by ID
exports.deleteProject = async (req, res) => {
  try {
    const deletedProject = await ProjectIdea.findByIdAndDelete(req.params.id);
    if (!deletedProject) return res.status(404).json({ message: 'Project not found' });
    res.json({ message: 'Project deleted successfully' });
  } catch (error) {
    console.error('Error deleting project:', error);
    res.status(500).json({ message: 'Server error deleting project' });
  }
};
