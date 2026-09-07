import streamlit as st
from workflow import run_study_workflow

st.set_page_config(
    page_title="AI Study Pack Generator",
    page_icon="📚",
    layout="wide",
)

st.title("📚 AI Study Pack Generator")
st.write(
    "Generate a personalized study pack through a multi-stage AI workflow: "
    "Planning → Content → Assessment → Review → Refinement."
)

with st.sidebar:
    st.header("Study Settings")
    topic = st.text_input("Topic", placeholder="e.g. Machine Learning")
    level = st.selectbox(
        "Education Level",
        ["Beginner", "Intermediate", "Advanced"],
    )
    goal = st.selectbox(
        "Study Goal",
        [
            "Exam Preparation",
            "Concept Understanding",
            "Quick Revision",
            "Assignment Preparation",
        ],
    )
    duration = st.selectbox(
        "Study Duration",
        ["30 minutes", "1 hour", "2 hours", "3 hours", "5+ hours"],
    )

generate = st.button("🚀 Generate Study Pack", type="primary", use_container_width=True)

if generate:
    if not topic.strip():
        st.error("Please enter a study topic.")
        st.stop()

    try:
        with st.status("Running AI workflow...", expanded=True) as status:
            st.write("🧠 Stage 1/5 — Creating study plan...")
            plan = None

            # Run the workflow as one reliable transaction.
            result = run_study_workflow(
                topic=topic.strip(),
                level=level,
                goal=goal,
                duration=duration,
            )

            st.write("✅ Stage 1 — Planning completed")
            st.write("✅ Stage 2 — Content generation completed")
            st.write("✅ Stage 3 — Assessment completed")
            st.write("✅ Stage 4 — Review completed")

            if result.get("refined"):
                st.write("🔧 Stage 5 — Refinement completed")
            else:
                st.write("✨ Stage 5 — Refinement not required")

            status.update(label="Study pack generated successfully!", state="complete")

        st.success("Your personalized study pack is ready!")

        review = result["review"]
        st.subheader("🔎 AI Quality Review")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Quality Score", f'{review.get("quality_score", 0)}/100')
        with col2:
            st.metric("Refined", "Yes" if result.get("refined") else "No")

        if review.get("strengths"):
            with st.expander("Strengths"):
                for item in review["strengths"]:
                    st.write(f"• {item}")

        if review.get("issues"):
            with st.expander("Review Issues"):
                for item in review["issues"]:
                    st.write(f"• {item}")

        content = result["content"]
        st.divider()
        st.header(f'📖 {content.get("title", topic)}')
        st.write(content.get("overview", ""))

        st.subheader("🎯 Learning Objectives")
        for item in result["plan"].get("learning_objectives", []):
            st.write(f"• {item}")

        st.subheader("📘 Study Notes")
        for section in content.get("sections", []):
            with st.expander(section.get("heading", "Topic")):
                st.write(section.get("explanation", ""))
                if section.get("key_points"):
                    st.markdown("**Key Points**")
                    for point in section["key_points"]:
                        st.write(f"• {point}")
                if section.get("example"):
                    st.markdown("**Example**")
                    st.write(section["example"])

        if content.get("key_terms"):
            st.subheader("🔑 Key Terms")
            for term in content["key_terms"]:
                if isinstance(term, dict):
                    st.write(f"**{term.get('term', '')}** — {term.get('definition', '')}")
                else:
                    st.write(f"• {term}")

        st.subheader("📝 Assessment")
        assessment = result["assessment"]

        st.markdown("### MCQs")
        for i, q in enumerate(assessment.get("mcqs", []), 1):
            st.write(f"**{i}. {q.get('question', '')}**")
            for option in q.get("options", []):
                st.write(f"- {option}")
            with st.expander("Show answer"):
                st.write(f"**Answer:** {q.get('answer', '')}")
                st.write(q.get("explanation", ""))

        st.markdown("### Short Questions")
        for i, q in enumerate(assessment.get("short_questions", []), 1):
            st.write(f"**{i}. {q.get('question', '')}**")
            with st.expander("Show answer"):
                st.write(q.get("answer", ""))

        st.markdown("### True / False")
        for i, q in enumerate(assessment.get("true_false", []), 1):
            st.write(f"**{i}. {q.get('statement', '')}**")
            with st.expander("Show answer"):
                st.write(f"**Answer:** {q.get('answer', '')}")
                st.write(q.get("explanation", ""))

        if content.get("summary"):
            st.subheader("📌 Quick Summary")
            st.write(content["summary"])

    except Exception as e:
        st.error(f"Unable to generate the study pack: {e}")
        st.info(
            "Check that GEMINI_API_KEY is configured in Streamlit Secrets "
            "and that the required packages are installed."
        )
