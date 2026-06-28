from agents import Agent, Runner
from tools import explain_topic, create_study_plan, recommend_resources, improvement_suggestion
from config import OPENAI_API_KEY
import os


os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY


study_agent = Agent(
    name="Study Buddy AI",

    instructions="""
    You are Study Buddy AI.
    You help students understand concepts
    and create study plans.
    """,

tools=[
    explain_topic,
    create_study_plan,
    recommend_resources,
    improvement_suggestion
]
)


def ask_agent(question):

    result = Runner.run_sync(
        study_agent,
        question
    )

    return result.final_output