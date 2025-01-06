import gradio as gr

from src.api.openai_client import OpenAIClient
from src.services.browser_service import BrowserService


class GradioInterface:
    def __init__(self, vector_store_dir):
        self.openai_client = OpenAIClient(vector_store_dir)
        self.browser_service = BrowserService()

    def process_input(self, text: str, chat_history: list) -> tuple:
        """Process user input and launch browser."""
        try:
            action_json = self.openai_client.get_action_json(text)

            # Case 1: Direct URL available
            if "url" in action_json:
                self.browser_service.launch_url(action_json)
                chat_history.append((text, f"Successfully launched URL: {action_json['url']}"))
                self.openai_client.clear_history()

            # Case 2: Need more information
            elif "needs_clarification" in action_json:
                options = "\n".join([f"- {opt}" for opt in action_json["options"]])
                response = f"{action_json['question']}\n\nOptions:\n{options}"
                chat_history.append((text, response))

            # Case 3: No information available
            elif "error" in action_json:
                chat_history.append((text, action_json["error"]))
                self.openai_client.clear_history()

            return "", chat_history
        except Exception as e:
            chat_history.append((text, f"Error: {str(e)}"))
            self.openai_client.clear_history()
            return "", chat_history

    def launch(self):
        """Launch Gradio interface."""
        with gr.Blocks() as interface:
            chatbot = gr.Chatbot(label="Conversation")
            msg = gr.Textbox(label="Your Request")

            # msg.submit(
            #     self.process_input,
            #     inputs=[msg, chatbot],
            #     outputs=[msg, chatbot]
            # )
            submit_btn = gr.Button("Submit")
            submit_btn.click(
                fn=self.process_input,
                inputs=[msg, chatbot],
                outputs=[msg, chatbot]
            )
            clear_btn = gr.Button("Clear")
            clear_btn.click(
                lambda: ([], []),
                outputs=[chatbot, msg],
                queue=False
            ).then(
                lambda: self.openai_client.clear_history()
            )

        interface.launch()
