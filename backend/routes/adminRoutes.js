const express = require('express');
const router = express.Router();
const {protect} = require('../middleware/auth');
const adminController = require('../controllers/adminController');

// Admin dashboard data
router.get('/dashboard', protect(), adminController.getDashboardData);

// Manage users (list)
router.get('/users', protect(), adminController.getAllUsers);

// Manage roadmaps
router.post('/roadmaps', protect(), adminController.createRoadmap);
router.put('/roadmaps/:id', protect(), adminController.updateRoadmap);
router.delete('/roadmaps/:id', protect(), adminController.deleteRoadmap);

// Manage jobs
router.post('/jobs', protect(), adminController.createJob);
router.put('/jobs/:id', protect(), adminController.updateJob);
router.delete('/jobs/:id', protect(), adminController.deleteJob);

// Add other admin routes as needed...

module.exports = router;
