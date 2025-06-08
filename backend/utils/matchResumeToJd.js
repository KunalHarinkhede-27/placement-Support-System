const axios = require("axios");

const matchResumeToJD = async (resumeText, jdText) => {
  try {
    const { data } = await axios.post("http://localhost:5001/match", { resumeText, jdText });
    return data;
  } catch (error) {
    throw new Error("Matching failed");
  }
};

module.exports = matchResumeToJD;
