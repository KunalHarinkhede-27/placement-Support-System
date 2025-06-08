const express = require('express');
const router = express.Router();
const multer = require('multer');
const {protect} = require('../middleware/auth');
const voiceController = require('../controllers/voiceController');

const storage = multer.memoryStorage();
const upload = multer({ storage });

router.post('/transcribe', protect(), upload.single('audio'), voiceController.transcribeVoice);

module.exports = router;
