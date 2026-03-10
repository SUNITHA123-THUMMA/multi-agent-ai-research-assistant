from fastapi import FastAPI
from pydantic import BaseModel

from agents.planner_agent import create_plan
from agents.research_agent import research_topic
from agents.summarizer_agent import summarize_text
from agents.writer_agent import generate_report

app = FastAPI()

class ResearchRequest(BaseModel):
    topic: str

@app.post("/research")
def run_research(request: ResearchRequest):

    topic = request.topic

    plan = create_plan(topic)

    research_data = research_topic(topic)

    summary = summarize_text(research_data)

    report = generate_report(topic, summary)

    return {
        "plan": plan,
        "research": research_data,
        "summary": summary,
        "report": report
    }