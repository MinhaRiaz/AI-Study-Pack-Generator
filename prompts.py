"""Prompts for the five AI workflow stages."""

PLANNING_PROMPT = """
You are an expert instructional designer.

Create a personalized study plan.

Topic: {topic}
Education level: {level}
Study goal: {goal}
Available study duration: {duration}

Return ONLY valid JSON with:
{{
  "learning_objectives": [],
  "topics": [],
  "time_allocation": [],
  "difficulty": "",
  "strategy": ""
}}
"""

CONTENT_PROMPT = """
You are an expert teacher.

Create accurate, beginner-friendly study content using the plan below.

Topic: {topic}
Education level: {level}

Study plan:
{plan}

Return ONLY valid JSON with:
{{
  "title": "",
  "overview": "",
  "sections": [
    {{
      "heading": "",
      "explanation": "",
      "key_points": [],
      "example": ""
    }}
  ],
  "key_terms": [],
  "summary": ""
}}
"""

ASSESSMENT_PROMPT = """
You are an educational assessment expert.

Create an assessment based ONLY on the study content below.

Topic: {topic}
Education level: {level}

Study content:
{content}

Return ONLY valid JSON with:
{{
  "mcqs": [
    {{
      "question": "",
      "options": ["", "", "", ""],
      "answer": "",
      "explanation": ""
    }}
  ],
  "short_questions": [],
  "true_false": []
}}

Create exactly {quiz_count} MCQs.
"""

REVIEW_PROMPT = """
You are a strict academic reviewer.

Review the study plan, content, and assessment for:
- factual accuracy
- completeness
- learning-objective coverage
- appropriate difficulty
- assessment quality
- clarity and organization

Study plan:
{plan}

Content:
{content}

Assessment:
{assessment}

Return ONLY valid JSON:
{{
  "approved": true,
  "quality_score": 0,
  "strengths": [],
  "issues": [],
  "recommendations": []
}}

Set approved to true only if the material is sufficiently accurate,
complete, clear, and appropriate.
"""

REFINEMENT_PROMPT = """
You are the final quality-improvement stage of an AI study-pack generator.

Improve the content and assessment according to the review feedback.
Preserve correct information and fix only genuine weaknesses.

Study plan:
{plan}

Current content:
{content}

Current assessment:
{assessment}

Review:
{review}

Return ONLY valid JSON:
{{
  "content": {{
    "title": "",
    "overview": "",
    "sections": [],
    "key_terms": [],
    "summary": ""
  }},
  "assessment": {{
    "mcqs": [],
    "short_questions": [],
    "true_false": []
  }}
}}
"""
