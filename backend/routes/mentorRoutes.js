const express = require('express');
const router = express.Router();
const {protect} = require('../middleware/auth');
const mentorController = require('../controllers/mentorController');

// Request mentor link
router.post('/request', protect(), mentorController.requestMentor);

// Get mentor links for a user
router.get('/links', protect(), mentorController.getMentorLinks);

// Accept mentor request
router.post('/accept/:id', protect(), mentorController.acceptMentorRequest);

// Reject mentor request
router.post('/reject/:id', protect(), mentorController.rejectMentorRequest);

module.exports = router;
