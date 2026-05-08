"""
file_reader.py

This tool reads study notes from a .txt file.

Responsibilities:
- Check if the file exists.
- Check if the file is a .txt file.
- Check if the file is not empty.
- Return the text content.
"""

from pathlib import Path


def read_file(file_path: str) -> str:
    """
    Reads a text file and returns its content.

    Args:
        file_path: Path to the .txt file.

    Returns:
        The text content of the file.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file is not .txt or is empty.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    if path.suffix.lower() != ".txt":
        raise ValueError("Only .txt files are supported.")

    content = path.read_text(encoding="utf-8").strip()

    if not content:
        raise ValueError("The file is empty.")

    return content