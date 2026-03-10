# multi-agent-ai-research-assistant
Developed a Multi-Agent AI Research Assistant that automatically analyzes a topic, gathers web information, summarizes key insights, and generates structured research reports. Built with Python and FastAPI using a modular agent architecture including planner, research, summarization, and report generation agents.

An AutoGPT-inspired multi-agent AI system that automatically researches a topic, gathers relevant information, summarizes findings, and generates a structured research report.

This project demonstrates Agentic AI architecture, backend API development, and automated knowledge synthesis using Python.

🚀 Features

Multi-Agent AI architecture

Autonomous task planning

Web-based information retrieval

Automatic text summarization

Structured report generation

REST API backend

Modular and scalable system design

System Architecture

The system uses multiple specialized AI agents working together:

User Query
    ↓
Planner Agent
    ↓
Research Agent (Web Search)
    ↓
Summarizer Agent
    ↓
Writer Agent
    ↓
Final Research Report
Each agent performs a specific task in the research pipeline.

⚙️ Technologies Used

Python

FastAPI

REST APIs

Requests / BeautifulSoup

React.js (Frontend)

Vector embeddings

Agent-based AI architecture

🛠 Installation

Clone the repository:

git clone https://github.com/yourusername/multi-agent-ai-research-assistant.git

Navigate to the backend folder:

cd backend

Install dependencies:

pip install -r requirements.txt

Run the server:

python -m uvicorn main:app --reload

API Documentation

After running the server open:

http://127.0.0.1:8000/docs

We will see the interactive FastAPI Swagger UI to test endpoints.

📊 Example API Request

Input:

POST /research
{
  "topic": "Artificial Intelligence in Healthcare"
}

Output:

{
  "plan": [
    "Search information",
    "Collect articles",
    "Summarize data",
    "Generate report"
  ],
  "summary": "AI improves diagnosis, drug discovery, and personalized medicine.",
  "report": "Detailed research report..."
}

🎯 Real-World Applications

Automated research assistance

Market research analysis

Content generation

Academic research support

Knowledge management systems

📌 Future Improvements

Integration with LLM APIs

Vector database for RAG

Multi-agent reasoning

Autonomous research workflows

Real-time web search integration
