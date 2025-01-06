import json
from typing import Dict

from openai import OpenAI

from src.config.settings import OPENAI_API_KEY, MODEL_NAME, SYSTEM_PROMPT
from src.storage import VectorStore


class OpenAIClient:
    def __init__(self, vector_store_dir):
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.conversation_history = []
        self.vector_store = VectorStore()
        self.vector_store.load(vector_store_dir)

    def get_action_json(self, user_input: str) -> Dict:
        """Get actionable JSON from OpenAI based on user input."""
        try:
            results = self.vector_store.search(user_input)
            if results:
                user_input += ("\n\n Following additional context might be relevant in finding out the actionable "
                               "JSON\n\n")
                for result in results:
                    user_input += f"{result['url']}\n\n"
                    user_input += f"{result['content']}\n\n"
            self.conversation_history.append({"role": "user", "content": user_input})

            messages = [
                {"role": "system", "content": SYSTEM_PROMPT},
                *self.conversation_history
            ]
            response = self.client.chat.completions.create(
                model=MODEL_NAME,
                messages=messages
            )

            response_json = json.loads(response.choices[0].message.content)
            self.conversation_history.append({
                "role": "assistant",
                "content": response.choices[0].message.content
            })
            return response_json
        except Exception as e:
            print(e.__cause__)
            raise Exception(f"Error getting OpenAI response: {str(e)}")

    def clear_history(self):
        """Clear conversation history."""
        self.conversation_history = []
