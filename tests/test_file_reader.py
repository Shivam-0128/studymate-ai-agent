import pytest
from pathlib import Path

from src.tools.file_reader import read_file


def test_read_file_success(tmp_path):
    file_path = tmp_path / "notes.txt"
    file_path.write_text("This is a test note.", encoding="utf-8")

    result = read_file(str(file_path))

    assert result == "This is a test note."


def test_read_file_missing():
    with pytest.raises(FileNotFoundError):
        read_file("missing_file.txt")


def test_read_file_empty(tmp_path):
    file_path = tmp_path / "empty.txt"
    file_path.write_text("", encoding="utf-8")

    with pytest.raises(ValueError):
        read_file(str(file_path))


def test_read_file_wrong_type(tmp_path):
    file_path = tmp_path / "notes.pdf"
    file_path.write_text("Fake PDF content", encoding="utf-8")

    with pytest.raises(ValueError):
        read_file(str(file_path))