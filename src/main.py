"""
main.py

This is the starting point of the StudyMate AI Agent.

The user gives a .txt file path.
The agent analyzes the file and creates a Markdown report.
"""

import sys

from src.agent import StudyMateAgent


def main():
    """
    Starts the StudyMate AI Agent from the command line.
    """

    print("StudyMate AI Agent")
    print("------------------")

    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        file_path = input("Enter the path to your .txt study notes file: ")

    try:
        agent = StudyMateAgent()
        result = agent.run(file_path)

        print("\nAnalysis completed successfully.")
        print(f"Word count: {result['analysis']['word_count']}")
        print(f"Sentence count: {result['analysis']['sentence_count']}")
        print(f"Paragraph count: {result['analysis']['paragraph_count']}")
        print(f"Difficulty: {result['analysis']['difficulty']}")
        print(f"\nReport saved at: {result['report_path']}")

    except Exception as error:
        print("\nAn error occurred:")
        print(error)


if __name__ == "__main__":
    main()