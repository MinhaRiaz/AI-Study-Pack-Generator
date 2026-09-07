import streamlit as st
import time
from workflow import (
    planning_stage,
    content_stage,
    assessment_stage,
    review_stage,
    refinement_stage,
)

st.set_page_config(
    page_title="AI Study Pack Generator",
    page_icon="📚",
    layout="wide",
)

st.title("📚 AI Study Pack Generator")
st.caption("Planning → Content Generation → Assessment → Review → Refinement")

# --- SIDEBAR INPUTS ---
with st.sidebar:
    st.header("Study Settings")
    topic = st.text_input("Topic", placeholder="e.g. Machine Learning")
    level = st.selectbox(
        "Education Level",
        ["Beginner", "Intermediate", "Advanced"],
    )
    duration = st.selectbox(
        "Learning duration",
        ["30 minutes", "1 hour", "1 week", "2 weeks", "1 month"],
        index=2
    )
    
    goal = st.text_area(
        "Learning goals",
        value="Build a strong foundation and prepare for practical projects.",
        height=100
    )
    
    sections = st.multiselect(
        "Study-pack sections",
        ["Notes", "Flashcards", "Quiz", "Study Plan", "Exam Tips"],
        default=["Notes", "Flashcards", "Quiz", "Study Plan", "Exam Tips"]
    )
    
    quiz_questions_count = st.slider(
        "Quiz questions",
        min_value=1,
        max_value=20,
        value=6
    )

generate = st.button("🧪 Generate Study Pack", type="primary", use_container_width=True)

# --- WORKFLOW EXECUTION WITH PROGRESS BAR ---
if generate:
    if not topic.strip():
        st.error("Please enter a study topic.")
        st.stop()

    try:
        # Progress Bar and Status Message Holders
        progress_bar = st.progress(0)
        status_box = st.empty()

        # Stage 1: Planning
        status_box.info("Stage 1/5: Planning in progress...")
        progress_bar.progress(10)
        
        plan = planning_stage(topic=topic.strip(), level=level, goal=goal, duration=duration)
        
        status_box.info("Stage 1/5: Planning completed")
        progress_bar.progress(20)
        time.sleep(0.4)

        # Stage 2: Content
        status_box.info("Stage 2/5: Content Generation in progress...")
        progress_bar.progress(35)
        
        content = content_stage(topic=topic.strip(), level=level, plan=plan)
        
        status_box.info("Stage 2/5: Content Generation completed")
        progress_bar.progress(40)
        time.sleep(0.4)

        # Stage 3: Assessment / Quiz
        status_box.info("Stage 3/5: Assessment & Quiz generation in progress...")
        progress_bar.progress(55)
        
        assessment = assessment_stage(
            topic=topic.strip(),
            level=level,
            content=content,
            quiz_count=quiz_questions_count
        )
        
        status_box.info("Stage 3/5: Assessment completed")
        progress_bar.progress(60)
        time.sleep(0.4)

        # Stage 4: Review
        status_box.info("Stage 4/5: Quality Reviewing...")
        progress_bar.progress(75)
        
        review = review_stage(plan=plan, content=content, assessment=assessment)
        
        status_box.info("Stage 4/5: Review completed")
        progress_bar.progress(80)
        time.sleep(0.4)

        # Stage 5: Refinement
        quality_score = review.get("quality_score", 0)
        approved = bool(review.get("approved", False))

        if not approved or quality_score < 70:
            status_box.info("Stage 5/5: Refining study pack...")
            progress_bar.progress(90)
            refined = refinement_stage(plan, content, assessment, review)
            content = refined.get("content", content)
            assessment = refined.get("assessment", assessment)
            is_refined = True
        else:
            is_refined = False
        
       
       

        progress_bar.progress(100)
        status_box.success("✅ Workflow completed successfully!")
        time.sleep(1)
        
        # Clear status box & progress bar for clean layout
        status_box.empty()
        progress_bar.empty()

        # --- DISPLAY RESULTS ---
        st.subheader("🔎 Study Pack Details")
        st.metric("Refined", "Yes" if is_refined else "No")

        st.divider()

        if "Study Plan" in sections and plan:
            st.subheader("📌 Study Plan")
            for obj in plan.get("learning_objectives", []):
                st.write(f"• {obj}")

        if "Notes" in sections and content:
            st.subheader(f'📖 {content.get("title", topic)}')
            st.write(content.get("overview", ""))
            for section in content.get("sections", []):
                with st.expander(section.get("heading", "Topic")):
                    st.write(section.get("explanation", ""))
                    if section.get("key_points"):
                        st.markdown("**Key Points**")
                        for point in section["key_points"]:
                            st.write(f"• {point}")

        if "Flashcards" in sections and content.get("key_terms"):
            st.subheader("🎴 Flashcards")
            cols = st.columns(2)
            for i, term in enumerate(content["key_terms"]):
                with cols[i % 2]:
                    if isinstance(term, dict):
                        st.info(f"**{term.get('term', '')}**\n\n{term.get('definition', '')}")
                    else:
                        st.info(f"• {term}")

        if "Quiz" in sections and assessment:
            st.subheader("📝 Assessment & Quiz")
            st.markdown("### Multiple Choice Questions")
            for i, q in enumerate(assessment.get("mcqs", []), 1):
                st.write(f"**{i}. {q.get('question', '')}**")
                for option in q.get("options", []):
                    st.write(f"- {option}")
                with st.expander("Show answer"):
                    st.write(f"**Answer:** {q.get('answer', '')}")
                    st.write(q.get("explanation", ""))

        if "Exam Tips" in sections and content.get("summary"):
            st.subheader("💡 Exam Tips & Summary")
            st.success(content["summary"])

    except Exception as e:
        st.error(f"Unable to generate the study pack: {e}")
