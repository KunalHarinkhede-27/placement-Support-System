const User = require("../models/User");

const findPeerMatch = async (userId) => {
  const user = await User.findById(userId);
  if (!user) throw new Error("User not found");

  const peers = await User.find({
    _id: { $ne: userId },
    role: "user",
    goals: user.goals,
    interests: { $in: user.interests },
  });

  return peers;
};

module.exports = findPeerMatch;
