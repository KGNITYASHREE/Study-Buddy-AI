import streamlit as st
from agent import ask_agent
from memory import create_database, save_student, save_progress


create_database()


st.title("📚 Study Buddy AI")

st.write("Your personal AI academic mentor")


st.subheader("Student Profile")


name = st.text_input("Name")

subject = st.text_input("Subject")

goal = st.text_input("Goal")

weak_topic = st.text_input("Weak Topic")


if st.button("Save Profile"):

    save_student(
        name,
        subject,
        goal,
        weak_topic
    )

    st.success("Profile saved!")


st.subheader("Learning Progress")


progress_subject = st.text_input("Progress Subject")

progress_topic = st.text_input("Completed Topic")

progress_score = st.number_input(
    "Score",
    min_value=0,
    max_value=100
)


if st.button("Save Progress"):

    save_progress(
        progress_subject,
        progress_topic,
        progress_score
    )

    st.success("Progress saved!")


question = st.text_input(
    "Ask your question"
)


if question:

    answer = ask_agent(question)

    st.write(answer)