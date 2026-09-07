"""Gemini API helper functions."""

import json
import os
from google import genai


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


def generate_json(prompt, model="gemini-3.6-flash"):
    client = get_client()

    response = client.models.generate_content(
        model=model,
        contents=prompt,
        config={
            "response_mime_type": "application/json",
            "temperature": 0.4,
        },
    )

    text = response.text.strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        raise RuntimeError(
            "The AI returned an invalid JSON response."
        ) from exc
