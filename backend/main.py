from fastapi import FastAPI
from pydantic import BaseModel

from backend.agents.planner_agent import create_plan
from backend.agents.research_agent import research_topic
from backend.agents.summarizer_agent import summarize_text
from backend.agents.writer_agent import write_report

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
