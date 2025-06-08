const voiceTranscriber = require('../utils/voiceTranscriber');

exports.transcribeVoice = async (req, res) => {
  if (!req.file) return res.status(400).json({ message: 'Audio file required' });

  try {
    const transcript = await voiceTranscriber(req.file.buffer);
    res.json({ transcript });
  } catch (error) {
    console.error('Voice transcribe error:', error);
    res.status(500).json({ message: 'Error transcribing audio' });
  }
};
