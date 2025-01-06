import webbrowser
from typing import Dict


class BrowserService:
    @staticmethod
    def launch_url(action_json: Dict) -> None:
        """Launch URL from action JSON in default browser."""
        try:
            url = action_json.get("url")
            if not url:
                raise ValueError("No URL found in action JSON")
            webbrowser.open(url)
        except Exception as e:
            raise Exception(f"Error launching browser: {str(e)}")
