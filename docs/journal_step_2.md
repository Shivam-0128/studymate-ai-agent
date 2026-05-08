# Journal Step 2 – 08.05

## Updated Description of the System Based on Implementation Progress

The system is now implemented as a working Python-based AI study assistant called **StudyMate AI Agent**. The goal of the system is to help students revise study notes more easily by converting a normal `.txt` notes file into a structured Markdown study report.

The system currently works as a local command-line application. The user provides the path to a `.txt` file. The agent reads the file, analyzes the text, sends the content to the Gemini API, receives AI-generated learning material, and saves the final report inside the `reports/` folder.

During implementation, the AI provider was changed from the originally planned Claude API to the Gemini API. The project goal stayed the same, but the AI client module was implemented as `gemini_client.py`.

The current workflow is:

1. The user runs the program from the command line.
2. The user provides a `.txt` study notes file.
3. The file reader tool validates and reads the file.
4. The text analyzer tool calculates word count, sentence count, paragraph count, keywords, and difficulty level.
5. The Gemini client sends prompts to the Gemini API.
6. Gemini generates a summary, quiz questions, answer key, and hard/easy concept explanation.
7. The report writer tool saves the final result as a Markdown report.
8. The user receives the path to the generated report.

The system has been tested with a sample notes file. It successfully generated a report, and all automated tests passed.

## Refined List of Programming Concepts Actually Used

The project now uses the following programming concepts:

1. Functions
2. Modules and packages
3. Classes
4. Object-oriented programming
5. Dependency injection for testing
6. File handling
7. String processing
8. Lists and dictionaries
9. Error handling
10. Environment variables
11. API integration
12. Automated testing with pytest
13. Git and GitHub version control

## Explanation of How These Concepts Are Applied

### Functions

Functions are used to separate the main tasks of the system.

Examples:

- `read_file()` reads the study notes file.
- `analyze_text()` calculates text statistics.
- `save_report()` creates and saves the Markdown report.
- `generate_summary()` sends a prompt to Gemini and returns a summary.
- `generate_quiz()` asks Gemini to create quiz questions.
- `detect_concepts()` asks Gemini to identify hard and easy concepts.

This makes the code easier to understand and test.

### Modules and Packages

The code is divided into different Python files and folders.

The `src/tools/` folder contains local tools such as the file reader, text analyzer, and report writer.

The `src/ai/` folder contains the Gemini client.

The `src/agent.py` file contains the main agent workflow.

This modular structure makes the project easier to maintain and extend.

### Classes

The main class used in the project is `StudyMateAgent`.

This class controls the complete workflow of the system. It receives the file path, calls the tools, calls the Gemini client, and returns the final result.

The `GeminiClient` class is responsible for communication with the Gemini API.

### Object-Oriented Programming

Object-oriented programming is used through the agent and AI client classes.

The `StudyMateAgent` object manages the workflow.

The `GeminiClient` object manages AI generation.

This separates responsibilities clearly.

### Dependency Injection for Testing

The `StudyMateAgent` can receive a custom AI client.

In the tests, a fake AI client called `MockAIClient` is used instead of the real Gemini API.

This allows the agent workflow to be tested without making real API calls.

### File Handling

File handling is used in two places.

First, the file reader tool reads the input `.txt` study notes file.

Second, the report writer tool creates and saves a `.md` Markdown report inside the `reports/` folder.

### String Processing

String processing is used to analyze the study notes.

The text analyzer splits text into words, sentences, and paragraphs. It also extracts keywords by removing common stop words.

String formatting is used to build the final Markdown report.

### Lists and Dictionaries

Lists are used to store keywords.

A dictionary is used to store text analysis results, such as word count, sentence count, paragraph count, keywords, average words per sentence, and difficulty level.

This makes the data easier to pass between the tools, agent, and report writer.

### Error Handling

The system handles common errors, including:

- missing file,
- empty file,
- unsupported file type,
- missing Gemini API key,
- failed program execution.

The main program uses `try` and `except` so that errors are shown clearly instead of crashing the application.

### Environment Variables

The Gemini API key is stored in a `.env` file.

The `.env.example` file shows the required configuration format without exposing the real API key.

The `.gitignore` file prevents `.env` from being uploaded to GitHub.

### API Integration

The system uses the Gemini API through the `google-genai` Python package.

The Gemini API is used for tasks that require language understanding and generation:

- creating a summary,
- generating quiz questions,
- producing an answer key,
- detecting hard and easy concepts.

### Automated Testing

The project uses `pytest`.

Tests currently check:

- successful file reading,
- missing file handling,
- empty file handling,
- unsupported file type handling,
- text analysis,
- report generation,
- full agent workflow using a mock AI client.

The latest test result was:

8 passed

### Git and GitHub

Git is used to track the development progress of the project.

GitHub is used to store the project repository online.

Current commits include:

- local tools and tests,
- Gemini workflow and working report generation.

## Description of How Tools Are Integrated into the System

The tools are integrated through the `StudyMateAgent` class.

The agent does not perform all tasks directly. Instead, it coordinates different tools.

The integration flow is:

1. `main.py` receives the file path from the command line.
2. `main.py` creates a `StudyMateAgent` object.
3. `StudyMateAgent` calls `read_file()` from `file_reader.py`.
4. `StudyMateAgent` sends the file content to `analyze_text()` from `text_analyzer.py`.
5. `StudyMateAgent` calls the `GeminiClient` methods:
   - `generate_summary()`
   - `generate_quiz()`
   - `detect_concepts()`
6. `StudyMateAgent` sends all results to `save_report()` from `report_writer.py`.
7. `save_report()` creates the Markdown file and returns the report path.
8. `main.py` displays the result to the user.

This design makes the system clear and extendable. More tools can be added later, such as an interactive quiz mode, PDF reader, or web interface.

## Current Status

At this stage, the main implementation is working.

Completed parts:

- project folder structure,
- local tools,
- Gemini API integration,
- command-line execution,
- Markdown report generation,
- automated tests,
- GitHub repository.

The next step is to improve the documentation, prepare deployment instructions, and add more testing details for the next submission stage.