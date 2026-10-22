
<div align="center">

# 🤖 AI Bug Report Analyzer

### Turn messy bug reports into clear, structured insights.

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1000&color=8B5CF6&center=true&vCenter=true&width=650&lines=AI-Powered+Bug+Report+Analysis;FastAPI+%7C+LangGraph+%7C+Gemini;Making+Debugging+Smarter" alt="Animated project title" />

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![Gemini](https://img.shields.io/badge/Google_Gemini-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white)

**AI-Powered Development Tool | Python | LLM Workflows**

</div>

---

## ✨ About the Project

AI Bug Report Analyzer is an AI-powered application designed to help developers analyze bug reports and organize technical information into a more structured format.

Built with Python, FastAPI, LangGraph, and Google Gemini, this project explores how AI workflows can support the software debugging process.

## 🚀 Key Features

- 🤖 AI-assisted bug report analysis
- 🧠 LangGraph-based workflow
- ⚡ FastAPI backend
- 💻 Web interface
- 🔧 Extensible project architecture

*Note: Features are subject to testing and depend on the current implementation.*

## 🛠️ Tech Stack

- **Language:** Python
- **Backend:** FastAPI
- **AI Workflow:** LangGraph
- **LLM:** Google Gemini
- **Frontend:** HTML, CSS, JavaScript

## 📂 Project Structure

```text
AI-Bug-Report-Analyzer/
├── static/
├── agents.py
├── graph.py
├── main.py
├── schemas.py
├── requirements.txt
├── .env.example
└── .gitignore
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/NargisNizam/AI-Bug-Report-Analyzer.git
cd AI-Bug-Report-Analyzer
```

### 2. Create a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create your local `.env` file using `.env.example`, then add the required API credentials.

```powershell
Copy-Item .env.example .env
```

**Security:** Never upload your real API key or `.env` file to GitHub.

### 5. Run the application

```bash
uvicorn main:app --reload
```

When the server starts successfully, open:

- API documentation: http://127.0.0.1:8000/docs
- Health check: http://127.0.0.1:8000/health

## 🔄 Workflow

1. Submit a bug report.
2. Process the request through the backend.
3. Run the AI workflow.
4. Generate a structured response for review.

## 🗺️ Future Improvements

- [ ] Improve error handling and response reliability
- [ ] Add automated tests
- [ ] Improve the frontend experience
- [ ] Evaluate the quality of AI-generated results

## 👩‍💻 Author

**Nargis Nizam**

GitHub: [@NargisNizam](https://github.com/NargisNizam)

---

<div align="center">

### 💜 Building smarter AI-powered developer tools.

</div>
