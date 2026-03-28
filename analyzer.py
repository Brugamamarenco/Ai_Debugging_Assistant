from google import genai
import os

# Create client using API key
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

def analyze_error(error_text: str) -> str:
    # If no error, return immediately
    if not error_text:
        return "No error detected"

    print("Sending to Gemini...")  # debug line

    # Build prompt
    prompt = f"""
You are a precise Python debugging assistant.

Rules:
- Be concise and direct
- Do NOT list multiple possibilities
- Identify the MOST likely cause only
- If it is a simple typo, say it clearly
- Do NOT ramble

Respond EXACTLY in this format:

Error type:
Root Cause:
Simple Explanation:
Suggested Fix:

Error:
{error_text}
""".strip()

    # Call Gemini API
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    print("Received response")  # debug line

    return response.text