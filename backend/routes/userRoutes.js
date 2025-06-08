const express = require('express');
const router = express.Router();
const userController = require('../controllers/userControllers'); // ensure this file exists
const { protect } = require('../middleware/auth');

// Public routes
router.post('/register', userController.registerUser);
router.post('/login', userController.loginUser);

// Protected routes
router.get('/profile', protect(), userController.getUserProfile);
router.put('/profile', protect(), userController.updateUserProfile);

module.exports = router;
