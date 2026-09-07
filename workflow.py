"""
AI Study Pack Generator - Workflow Orchestration
"""

from prompts import (
    PLANNING_PROMPT,
    CONTENT_PROMPT,
    ASSESSMENT_PROMPT,
    REVIEW_PROMPT,
    REFINEMENT_PROMPT,
)
from ai_utils import generate_json


def planning_stage(topic, level, goal, duration):
    prompt = PLANNING_PROMPT.format(
        topic=topic, level=level, goal=goal, duration=duration
    )
    return generate_json(prompt)


def content_stage(topic, level, plan):
    prompt = CONTENT_PROMPT.format(
        topic=topic, level=level, plan=plan
    )
    return generate_json(prompt)


def assessment_stage(topic, level, content, quiz_count=6):
    prompt = ASSESSMENT_PROMPT.format(
        topic=topic, level=level, content=content, quiz_count=quiz_count
    )
    return generate_json(prompt)


def review_stage(plan, content, assessment):
    prompt = REVIEW_PROMPT.format(
        plan=plan, content=content, assessment=assessment
    )
    return generate_json(prompt)


def refinement_stage(plan, content, assessment, review):
    prompt = REFINEMENT_PROMPT.format(
        plan=plan,
        content=content,
        assessment=assessment,
        review=review,
    )
    return generate_json(prompt)


def run_study_workflow(topic, level, goal, duration, quiz_count=6):
    """Run the complete multi-stage study-pack workflow."""
    plan = planning_stage(topic, level, goal, duration)
    content = content_stage(topic, level, plan)
    assessment = assessment_stage(topic, level, content, quiz_count=quiz_count)
    review = review_stage(plan, content, assessment)

    approved = bool(review.get("approved", False))

    if approved:
        final_pack = {
            "plan": plan,
            "content": content,
            "assessment": assessment,
            "review": review,
            "refined": False,
        }
    else:
        refined = refinement_stage(plan, content, assessment, review)
        final_pack = {
            "plan": plan,
            "content": refined.get("content", content),
            "assessment": refined.get("assessment", assessment),
            "review": review,
            "refined": True,
        }

    return final_pack
