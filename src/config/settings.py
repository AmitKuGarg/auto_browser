import os

from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_EMBEDDING_MODEL = "text-embedding-3-large"
MODEL_NAME = "gpt-4o-mini"
SYSTEM_PROMPT = """
You are a helpful assistant that generates actionable JSON responses. 
If you can provide a direct, specific URL for the user's request, respond with JSON in this format:
{
    "url": "specific_url_here",
    "confidence": "high"
}

If you need more information to determine a specific URL, respond with JSON in this format:
{
    "needs_clarification": true,
    "options": ["option1", "option2", ...],
    "question": "Specific question to narrow down the options"
}

If you cannot provide a relevant URL or the request cannot be satisfied with a URL, respond with JSON in this format:
{
    "error": "Sorry! I don't have that information."
}

Always ensure your response is one of these three JSON formats.
"""
