const fs = require("fs");
const path = require("path");
const OpenAI = require("openai");

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

const transcribeVoice = async (audioBuffer) => {
  const tempFilePath = path.join(__dirname, "temp_audio.webm");

  await fs.promises.writeFile(tempFilePath, audioBuffer);

  try {
    const response = await openai.audio.transcriptions.create({
      file: fs.createReadStream(tempFilePath),
      model: "whisper-1",
    });

    await fs.promises.unlink(tempFilePath);

    return response.text;
  } catch (error) {
    await fs.promises.unlink(tempFilePath);
    throw error;
  }
};

module.exports = transcribeVoice;
