# StudyMate AI Agent

StudyMate AI Agent is a Python-based AI study assistant. It reads study notes from a `.txt` file, analyzes the text, generates a summary, creates quiz questions, identifies hard and easy concepts, and saves the result as a Markdown report.

The system uses local Python tools for file reading, text analysis, and report writing. It uses the Gemini API for AI-generated summary, quiz, and concept explanation.

## Features

- Read study notes from a `.txt` file
- Validate file input
- Count words, sentences, and paragraphs
- Extract important keywords
- Estimate basic text difficulty
- Generate an AI summary using Gemini API
- Generate quiz questions and answer key using Gemini API
- Identify hard and easy concepts using Gemini API
- Save the final result as a Markdown report
- Includes automated tests using pytest

## Project Structure

```text
studymate-ai-agent/
│
├── src/
│   ├── main.py
│   ├── agent.py
│   ├── config.py
│   │
│   ├── ai/
│   │   └── gemini_client.py
│   │
│   └── tools/
│       ├── file_reader.py
│       ├── text_analyzer.py
│       └── report_writer.py
│
├── tests/
│   ├── test_agent.py
│   ├── test_file_reader.py
│   ├── test_text_analyzer.py
│   └── test_report_writer.py
│
├── data/
│   └── sample_notes.txt
│
├── reports/
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md