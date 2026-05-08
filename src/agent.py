"""
agent.py

This file contains the main StudyMateAgent.

The agent controls the full workflow:
1. Read the notes file.
2. Analyze the text.
3. Ask Gemini for summary.
4. Ask Gemini for quiz.
5. Ask Gemini for hard/easy concepts.
6. Save the final Markdown report.
"""

from src.tools.file_reader import read_file
from src.tools.text_analyzer import analyze_text
from src.tools.report_writer import save_report
from src.ai.gemini_client import GeminiClient


class StudyMateAgent:
    """
    Main agent class for the StudyMate AI Agent system.
    """

    def __init__(self, ai_client=None):
        """
        Creates the agent.

        Args:
            ai_client: Optional AI client. This is useful for testing.
        """

        self.ai_client = ai_client if ai_client is not None else GeminiClient()

    def run(self, file_path: str) -> dict:
        """
        Runs the full StudyMate workflow.

        Args:
            file_path: Path to the .txt study notes file.

        Returns:
            A dictionary containing analysis, AI outputs, and report path.
        """

        notes = read_file(file_path)

        analysis = analyze_text(notes)

        summary = self.ai_client.generate_summary(notes)

        quiz = self.ai_client.generate_quiz(notes)

        concepts = self.ai_client.detect_concepts(notes)

        report_path = save_report(
            analysis=analysis,
            summary=summary,
            quiz=quiz,
            concepts=concepts
        )

        return {
            "analysis": analysis,
            "summary": summary,
            "quiz": quiz,
            "concepts": concepts,
            "report_path": report_path
        }