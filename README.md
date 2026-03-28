# AI Debugging Assistant

AI Debugging Assistant is a Python-based tool that runs a target Python file, captures runtime errors, and generates simplified explanations with suggested fixes using the Gemini API.

## Features
- Executes Python files and captures runtime errors
- Identifies root causes from tracebacks
- Converts complex errors into simple explanations
- Suggests actionable fixes

## Project Structure
- `main.py` — controls program workflow
- `parser.py` — runs target file and captures errors
- `analyzer.py` — sends errors to Gemini for analysis
- `addTest.py` — sample test file

## Requirements
- Python 3.10+
- google-genai

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export GEMINI_API_KEY="your_api_key_here"
