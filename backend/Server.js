const express = require("express");
const cors = require("cors");
const dotenv = require("dotenv");
const connectDB = require("./config/db");
dotenv.config();

const userRoutes = require("./routes/userRoutes");
const resumeRoutes = require("./routes/resumeRoutes");
const jobRoutes = require("./routes/jobRoutes");
const roadmapRoutes = require("./routes/roadmapRoutes");
const projectRoutes = require("./routes/projectRoutes");
const mentorRoutes = require("./routes/mentorRoutes");
const adminRoutes = require("./routes/adminRoutes");
const voiceRoutes = require("./routes/voiceRoutes");

connectDB();

const app = express();
app.use(cors());
app.use(express.json());

console.log("OpenAI API Key:", process.env.OPENAI_API_KEY);

console.log('Loading userRoutes...');
app.use("/api/users", userRoutes);
console.log('Loading resumeRoutes...');
app.use("/api/resume", resumeRoutes);
console.log('Loading jobRoutes...');
app.use("/api/jobs", jobRoutes);
console.log('Loading roadmapRoutes...');
app.use("/api/roadmap", roadmapRoutes);
console.log('Loading projectRoutes...');
app.use("/api/projects", projectRoutes);
console.log('Loading mentorRoutes...');
app.use("/api/mentors", mentorRoutes);
console.log('Loading adminRoutes...');
app.use("/api/admin", adminRoutes);
console.log('Loading voiceRoutes...');
app.use("/api/voice", voiceRoutes);

app.get("/", (req, res) => res.send("AI Career Assistant API running"));

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
