const axios = require("axios");

const parseResume = async (resumeUrl) => {
  try {
    const { data } = await axios.post("http://localhost:5001/parse", { resumeUrl });
    return data;
  } catch (error) {
    throw new Error("Resume parsing failed");
  }
};

module.exports = parseResume;
