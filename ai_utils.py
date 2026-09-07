"""Gemini API helper functions with automatic retry logic."""

import json
import os
import time
from google import genai
from google.genai.errors import APIError


def get_client():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        try:
            import streamlit as st
            api_key = st.secrets["GEMINI_API_KEY"]
        except Exception:
            api_key = None

    if not api_key:
        raise RuntimeError(
            "GEMINI_API_KEY is missing. Add it to Streamlit Secrets."
        )

    return genai.Client(api_key=api_key)


def generate_json(prompt, model="gemini-3.8-flash", max_retries=3):
    """Generate JSON content with built-in retry handling for 503/429 errors."""
    client = get_client()

    for attempt in range(max_retries):
        try:
            response = client.models.generate_content(
                model=model,
                contents=prompt,
                config={
                    "response_mime_type": "application/json",
                    "temperature": 0.4,
                },
            )

            text = response.text.strip()
            return json.loads(text)

        except APIError as e:
            # Check for 503 (Unavailable) or 429 (Rate Limit Exceeded)
            if e.code in (503, 429) and attempt < max_retries - 1:
                wait_time = (attempt + 1) * 3  # Wait 3s, then 6s, etc.
                time.sleep(wait_time)
                continue
            raise e
        except json.JSONDecodeError as exc:
            raise RuntimeError("The AI returned an invalid JSON response.") from exc
