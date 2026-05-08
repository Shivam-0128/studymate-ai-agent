"""
text_analyzer.py

This tool performs basic text analysis without using AI.

It calculates:
- word count
- sentence count
- paragraph count
- important keywords
- simple difficulty level
"""

import re
from collections import Counter


STOP_WORDS = {
    "the", "is", "are", "a", "an", "and", "or", "to", "of", "in", "on",
    "for", "with", "that", "this", "it", "as", "by", "from", "be", "can",
    "will", "not", "usually", "into", "their", "they", "them", "has",
    "have", "was", "were", "at", "but", "if", "then"
}


def analyze_text(text: str) -> dict:
    """
    Analyzes study notes and returns basic statistics.

    Args:
        text: Study notes as plain text.

    Returns:
        A dictionary containing text statistics.
    """

    if not text or not text.strip():
        raise ValueError("Text cannot be empty.")

    words = re.findall(r"\b[a-zA-Z]+\b", text.lower())
    sentences = re.split(r"[.!?]+", text)
    paragraphs = [p for p in text.split("\n\n") if p.strip()]

    meaningful_words = [
        word for word in words
        if word not in STOP_WORDS and len(word) > 2
    ]

    keyword_counts = Counter(meaningful_words)
    keywords = [word for word, count in keyword_counts.most_common(10)]

    word_count = len(words)
    sentence_count = len([s for s in sentences if s.strip()])
    paragraph_count = len(paragraphs)

    average_words_per_sentence = (
        word_count / sentence_count if sentence_count > 0 else 0
    )

    if average_words_per_sentence < 12:
        difficulty = "Easy"
    elif average_words_per_sentence < 20:
        difficulty = "Medium"
    else:
        difficulty = "Hard"

    return {
        "word_count": word_count,
        "sentence_count": sentence_count,
        "paragraph_count": paragraph_count,
        "keywords": keywords,
        "average_words_per_sentence": round(average_words_per_sentence, 2),
        "difficulty": difficulty,
    }