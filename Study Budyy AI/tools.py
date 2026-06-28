from agents import function_tool


@function_tool
def explain_topic(topic: str):

    return f"""
    Explanation of {topic}:

    {topic} is explained in a simple way
    so students can understand easily.
    """


@function_tool
def create_study_plan(subject: str, days: int):

    return f"""
    Study Plan:

    Subject: {subject}

    Day 1: Learn basics
    Day 2: Practice examples
    Day 3: Revision

    Total days: {days}
    """
@function_tool
def recommend_resources(topic: str):

    return f"""
    Learning resources for {topic}:

    1. Official documentation
    2. Beginner friendly tutorials
    3. Practice exercises
    4. Previous year questions
    5. Online learning videos
    """
from agents import function_tool


@function_tool
def improvement_suggestion(subject: str, topic: str, score: int):

    if score < 50:
        feedback = """
You are weak in this topic.
- Revise basics
- Watch beginner videos
- Practice daily exercises
"""

    elif score < 80:
        feedback = """
Good progress.
- Focus on weak areas
- Solve more practice problems
- Revise regularly
"""

    else:
        feedback = """
Excellent performance.
- Keep practicing
- Try advanced questions
- Revise weekly
"""

    return f"""
Subject: {subject}
Topic: {topic}
Score: {score}

Improvement Plan:
{feedback}
"""