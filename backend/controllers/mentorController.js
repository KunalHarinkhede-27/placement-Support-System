const MentorLink = require('../models/MentorLink');
const User = require('../models/User');

exports.requestMentor = async (req, res) => {
  const { mentorId } = req.body;
  if (!mentorId) return res.status(400).json({ message: 'Mentor ID required' });

  try {
    // Prevent duplicate request
    const existingRequest = await MentorLink.findOne({
      mentor: mentorId,
      mentee: req.user.id,
    });
    if (existingRequest) return res.status(400).json({ message: 'Request already sent' });

    const mentorLink = new MentorLink({
      mentor: mentorId,
      mentee: req.user.id,
    });
    await mentorLink.save();

    res.json({ message: 'Mentor request sent' });
  } catch (error) {
    console.error('Mentor request error:', error);
    res.status(500).json({ message: 'Error sending mentor request' });
  }
};

exports.getMentorLinks = async (req, res) => {
  try {
    const links = await MentorLink.find({
      $or: [{ mentor: req.user.id }, { mentee: req.user.id }],
    })
      .populate('mentor', 'name email')
      .populate('mentee', 'name email');

    res.json(links);
  } catch (error) {
    console.error('Get mentor links error:', error);
    res.status(500).json({ message: 'Error fetching mentor links' });
  }
};

exports.acceptMentorRequest = async (req, res) => {
  try {
    const link = await MentorLink.findById(req.params.id);
    if (!link) return res.status(404).json({ message: 'Mentor link not found' });

    if (link.mentor.toString() !== req.user.id) {
      return res.status(403).json({ message: 'Not authorized to accept this request' });
    }

    link.status = 'accepted';
    await link.save();

    res.json({ message: 'Mentor request accepted' });
  } catch (error) {
    console.error('Accept mentor error:', error);
    res.status(500).json({ message: 'Error accepting mentor request' });
  }
};

exports.rejectMentorRequest = async (req, res) => {
  try {
    const link = await MentorLink.findById(req.params.id);
    if (!link) return res.status(404).json({ message: 'Mentor link not found' });

    if (link.mentor.toString() !== req.user.id) {
      return res.status(403).json({ message: 'Not authorized to reject this request' });
    }

    link.status = 'rejected';
    await link.save();

    res.json({ message: 'Mentor request rejected' });
  } catch (error) {
    console.error('Reject mentor error:', error);
    res.status(500).json({ message: 'Error rejecting mentor request' });
  }
};
