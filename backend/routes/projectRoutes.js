const express = require('express');
const router = express.Router();
const projectController = require('../controllers/projectController');
const { protect } = require('../middleware/auth');

// Get all projects
router.get('/', protect(), projectController.getAllProjects);

// Get project by id
router.get('/:id', protect(), projectController.getProjectById);

// Create new project
router.post('/', protect(), projectController.createProject);

// Update project by id
router.put('/:id', protect(), projectController.updateProject);

// Delete project by id
router.delete('/:id', protect(), projectController.deleteProject);

module.exports = router;
