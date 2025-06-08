const express = require('express');
const router = express.Router();
const jobController = require('../controllers/jobController');
const { protect } = require('../middleware/auth'); // ✅ destructure protect

router.get('/', protect(), jobController.getJobs); // ✅ use protect()
router.post('/match', protect(), jobController.matchJobsToUserSkills);

module.exports = router;
