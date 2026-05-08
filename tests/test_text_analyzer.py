import pytest

from src.tools.text_analyzer import analyze_text


def test_analyze_text_success():
    text = "Artificial intelligence is useful. Machine learning uses data."

    result = analyze_text(text)

    assert result["word_count"] > 0
    assert result["sentence_count"] == 2
    assert result["paragraph_count"] == 1
    assert "difficulty" in result
    assert isinstance(result["keywords"], list)


def test_analyze_text_empty():
    with pytest.raises(ValueError):
        analyze_text("")