# AI Debugging Assistant

AI Debugging Assistant is a Python-based tool that analyzes Python error messages and provides clear, simplified explanations along with suggested fixes using an LLM (Gemini API).

## Features
- Runs a target Python file and captures runtime errors
- Identifies the root cause of the error
- Explains errors in simple, human-readable language
- Suggests specific fixes

## Project Structure
- `main.py` — controls the program workflow
- `parser.py` — runs the target file and captures error output
- `analyzer.py` — sends errors to Gemini and generates explanations
- `addTest.py` — sample file used for testing

## Setup

1. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate

Requirements
google-genai
