const express = require('express');
const router = express.Router();
const roadmapController = require('../controllers/roadmapController');
const {protect} = require('../middleware/auth');

router.get('/', protect(), roadmapController.getAllRoadmaps);
router.post('/goal', protect(), roadmapController.getRoadmapByGoal);

module.exports = router;
