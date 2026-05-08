from pathlib import Path

from src.agent import StudyMateAgent


class MockAIClient:
    """
    Fake AI client used for testing.

    We use this so tests do not call the real Gemini API.
    """

    def generate_summary(self, notes):
        return "Mock summary."

    def generate_quiz(self, notes):
        return "Mock quiz with answer key."

    def detect_concepts(self, notes):
        return "Mock hard and easy concepts."


def test_agent_workflow(tmp_path):
    notes_file = tmp_path / "notes.txt"
    notes_file.write_text(
        "Artificial intelligence is useful. Machine learning uses data.",
        encoding="utf-8"
    )

    agent = StudyMateAgent(ai_client=MockAIClient())

    result = agent.run(str(notes_file))

    assert result["summary"] == "Mock summary."
    assert result["quiz"] == "Mock quiz with answer key."
    assert result["concepts"] == "Mock hard and easy concepts."
    assert result["analysis"]["word_count"] > 0

    report_path = Path(result["report_path"])
    assert report_path.exists()