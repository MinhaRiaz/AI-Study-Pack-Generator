# 📚 AI Study Pack Generator

A Streamlit AI application that generates personalized study packs using a five-stage AI workflow.

## Workflow

1. Planning
2. Content Generation
3. Assessment
4. Review
5. Refinement

## Project Structure

- `app.py` — Main Streamlit application
- `workflow.py` — Workflow orchestration
- `prompts.py` — AI prompts for each stage
- `ai_utils.py` — Gemini API helper
- `requirements.txt` — Python dependencies

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Set your Gemini API key as an environment variable:

```bash
GEMINI_API_KEY=your_api_key
```

For Streamlit Community Cloud, add the key under **App Settings → Secrets**:

```toml
GEMINI_API_KEY = "your_api_key"
```

Run locally:

```bash
streamlit run app.py
```

Never commit your API key to GitHub.
