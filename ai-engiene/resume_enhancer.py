import os
import openai

# Initialize OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

def enhance_resume_text(resume_text: str) -> dict:
    """
    Enhance resume text using GPT:
    - Improve summary
    - Add impactful keywords
    - Correct grammar and wording

    Parameters:
        resume_text (str): Raw text extracted from the resume

    Returns:
        dict: {
            "enhanced_summary": str,
            "enhanced_resume": str
        }
    """

    prompt = (
        "You are an expert career coach and resume writer.\n"
        "Improve the following resume text by:\n"
        "1. Writing a compelling summary at the top.\n"
        "2. Enhancing wording and grammar.\n"
        "3. Adding relevant keywords to optimize for ATS.\n\n"
        "Resume Text:\n"
        f"{resume_text}\n\n"
        "Enhanced Resume:"
    )

    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            temperature=0.7,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        enhanced_resume = response.choices[0].text.strip()

        # Extract the summary (assumed to be the first paragraph)
        enhanced_summary = enhanced_resume.split("\n\n")[0] if enhanced_resume else ""

        return {
            "enhanced_summary": enhanced_summary,
            "enhanced_resume": enhanced_resume
        }

    except Exception as e:
        return {
            "error": str(e)
        }


if __name__ == "__main__":
    # Example usage
    sample_resume_text = """
    Experienced software developer with knowledge of Python and JavaScript.
    Worked on web applications using Flask and React. Seeking challenging role.
    """

    result = enhance_resume_text(sample_resume_text)
    print(result)
