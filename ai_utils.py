"""Groq API helper functions with automatic retry logic."""

import json
import os
import time
from groq import Groq


def get_client():
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        try:
            import streamlit as st
            api_key = st.secrets["GROQ_API_KEY"]
        except Exception:
            api_key = None

    if not api_key:
        raise RuntimeError(
            "GROQ_API_KEY is missing. Add it to Streamlit Secrets."
        )

    return Groq(api_key=api_key)


def generate_json(prompt, model="openai/gpt-oss-120b", max_retries=3):
    """Generate JSON content using Groq's high-speed API."""
    client = get_client()

    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {
                        "role": "system",
                        "content": "You are a helpful assistant that outputs strictly valid JSON.",
                    },
                    {"role": "user", "content": prompt},
                ],
                response_format={"type": "json_object"},
                temperature=0.4,
            )

            text = response.choices[0].message.content.strip()
            return json.loads(text)

        except Exception as e:
            if attempt < max_retries - 1:
                time.sleep((attempt + 1) * 2)
                continue
            raise RuntimeError(f"Groq API Error: {e}") from e
