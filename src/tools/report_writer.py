"""
report_writer.py

This tool creates and saves the final Markdown report.

The report includes:
- basic text analysis
- AI-generated summary
- AI-generated quiz
- hard and easy concepts
"""

from pathlib import Path
from datetime import datetime


def save_report(
    analysis: dict,
    summary: str,
    quiz: str,
    concepts: str,
    output_dir: str = "reports"
) -> str:
    """
    Saves the final study report as a Markdown file.

    Args:
        analysis: Dictionary containing text analysis results.
        summary: AI-generated summary.
        quiz: AI-generated quiz questions and answers.
        concepts: AI-generated hard/easy concept explanation.
        output_dir: Folder where the report should be saved.

    Returns:
        Path to the saved report.
    """

    reports_folder = Path(output_dir)
    reports_folder.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_path = reports_folder / f"study_report_{timestamp}.md"

    keywords = ", ".join(analysis.get("keywords", []))

    report_content = f"""# StudyMate AI Report

## 1. Text Analysis

- Word count: {analysis.get("word_count")}
- Sentence count: {analysis.get("sentence_count")}
- Paragraph count: {analysis.get("paragraph_count")}
- Average words per sentence: {analysis.get("average_words_per_sentence")}
- Difficulty level: {analysis.get("difficulty")}
- Important keywords: {keywords}

---

## 2. AI Summary

{summary}

---

## 3. Quiz Questions

{quiz}

---

## 4. Hard and Easy Concepts

{concepts}
"""

    report_path.write_text(report_content, encoding="utf-8")

    return str(report_path)