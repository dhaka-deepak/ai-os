# AI OS

A fully local AI Operating System powered by Large Language Models.

AI OS is a desktop assistant capable of understanding natural language, planning tasks, executing tools, remembering conversations, controlling desktop applications, creating files, running terminal commands, and serving as the foundation for autonomous AI agents.

Everything runs locally using Ollama, ensuring privacy and offline functionality.

---

# Features

### Phase 1 (Completed)

* Local AI Chat using Ollama
* Electron Desktop Application
* React Frontend
* FastAPI Gateway
* Planner → Executor Agent Architecture
* Persistent Memory (PostgreSQL)
* Conversation History
* Open Desktop Applications
* Create and Read Files
* Execute Terminal Commands
* Completely Offline

---

# Architecture

```
React + Electron
        │
        ▼
Gateway Service
(FastAPI)
        │
        ▼
Assistant Agent
        │
        ▼
Planner Agent
        │
        ▼
Execution Plan (JSON)
        │
        ▼
Executor Agent
        │
        ▼
Tool Executor
        │
 ┌──────┼──────────┐
 │      │          │
 ▼      ▼          ▼
Apps  Terminal   Files
        │
        ▼
      Ollama
```

---

# Technology Stack

## Frontend

* React
* Electron
* JavaScript

## Backend

* Python
* FastAPI
* Ollama

## Database

* PostgreSQL

## AI

* Qwen
* Ollama

---

# Project Structure

```
frontend-electron/
gateway-service/
agent-service/
memory-service/
```

---

# Getting Started

Clone the repository

```bash
git clone https://github.com/<username>/ai-os.git
```

Start Ollama

```bash
ollama serve
```

Run Memory Service

```bash
uvicorn main:app --reload --port 8002
```

Run Agent Service

```bash
uvicorn main:app --reload --port 8001
```

Run Gateway

```bash
uvicorn main:app --reload --port 8000
```

Run Frontend

```bash
npm install
npm run dev
```

---

# Current Capabilities

The assistant understands natural language and can:

* Chat with a local LLM
* Remember previous conversations
* Open desktop applications
* Run PowerShell commands
* Create and read files
* Generate execution plans
* Execute multi-step workflows

---

# Roadmap

## Phase 2

* Multi-Agent System
* Code Generation Agent
* Browser Automation
* Voice Assistant
* RAG
* Plugin Architecture

## Phase 3

* Autonomous Task Execution
* AI Workflow Builder
* Docker Integration
* Git Integration
* Project Generation

## Phase 4

* AI Developer
* AI DevOps
* AI Research Assistant
* Cross-device Synchronization

---

# Contributing

Contributions, ideas, bug reports, and feature requests are welcome.

Feel free to fork the repository and submit pull requests.

---

# License

MIT License
