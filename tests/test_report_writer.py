from pathlib import Path

from src.tools.report_writer import save_report


def test_save_report(tmp_path):
    analysis = {
        "word_count": 10,
        "sentence_count": 2,
        "paragraph_count": 1,
        "average_words_per_sentence": 5,
        "difficulty": "Easy",
        "keywords": ["ai", "learning"]
    }

    summary = "This is a summary."
    quiz = "Q1: What is AI? Answer: Artificial Intelligence."
    concepts = "Hard concept: Machine learning."

    report_path = save_report(
        analysis=analysis,
        summary=summary,
        quiz=quiz,
        concepts=concepts,
        output_dir=str(tmp_path)
    )

    saved_file = Path(report_path)

    assert saved_file.exists()
    assert saved_file.suffix == ".md"

    content = saved_file.read_text(encoding="utf-8")

    assert "StudyMate AI Report" in content
    assert "This is a summary." in content
    assert "Machine learning" in content