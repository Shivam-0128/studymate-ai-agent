"""
config.py

This file is responsible for reading configuration values from environment variables.

Why do we need this file?
- We should not write secret API keys directly inside Python code.
- We keep secrets in a .env file.
- This file reads those values and gives them to the rest of the program.
"""

import os
from dotenv import load_dotenv


# Load variables from the .env file into the program environment.
load_dotenv()


class Config:
    """
    Config class stores important settings used by the application.
    """

    # Gemini API key will be read from the .env file.
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    # Model name is also read from .env.
    # If it is missing, we use gemini-2.5-flash as default.
    GEMINI_MODEL_NAME = os.getenv("GEMINI_MODEL_NAME", "gemini-2.5-flash")

    @staticmethod
    def validate():
        """
        Checks whether required configuration values are available.

        Raises:
            ValueError: if GEMINI_API_KEY is missing.
        """

        if not Config.GEMINI_API_KEY:
            raise ValueError(
                "GEMINI_API_KEY is missing. Please create a .env file and add your Gemini API key."
            )