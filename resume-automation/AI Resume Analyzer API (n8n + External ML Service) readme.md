# 📄 AI Resume Analyzer API (n8n + External ML Service)

## 🚀 Overview

This project is a **Resume Analysis Automation Workflow** built using **n8n**.

It exposes a webhook endpoint that:

1. Accepts a resume PDF path
2. Accepts a job description
3. Forwards both to an external AI/ML resume analysis service
4. Returns the analysis result as an API response

This workflow acts as a lightweight orchestration layer between a frontend/client and a resume analysis engine.

---

## 🧠 What This Project Demonstrates

- Webhook-based API design
- n8n as an orchestration layer
- Microservice-style architecture
- AI/ML backend integration
- JSON payload handling
- Clean separation of automation and ML logic

---

## 🛠 Tech Stack

- **n8n** – Workflow orchestration
- **Webhook Node** – Public API endpoint
- **HTTP Request Node** – Backend service call
- External Resume Analysis API (running on Docker/local backend)

---

## 🔄 Workflow Architecture

```text
Client / Frontend
        ↓
POST /resume-analyze (Webhook)
        ↓
Forward Data to AI Backend
        ↓
Return AI Analysis Response
```

---

## 📌 How It Works

### 1️⃣ Webhook Endpoint

- **Method:** `POST`
- **Path:** `/resume-analyze`
- **Response Mode:** Last Node

The webhook accepts JSON input:

```json
{
  "pdfPath": "/path/to/resume.pdf",
  "jobDescription": "Job description text here"
}
```

---

### 2️⃣ HTTP Request Node

The workflow forwards the request to:

```
http://host.docker.internal:5050/analyze
```

With the following body:

```json
{
  "pdfPath": "{{$json.body.pdfPath}}",
  "jobDescription": "{{$json.body.jobDescription}}"
}
```

This external service handles:
- Resume parsing
- Job-description matching
- Scoring
- Skill gap analysis
- Keyword alignment

---

## 📂 Project File

- `resume analyzer.json`  
  Exported n8n workflow file :contentReference[oaicite:0]{index=0}

---

## ⚙️ Setup Instructions

### 1️⃣ Import Workflow
- Open n8n
- Click **Import**
- Upload `resume analyzer.json`

### 2️⃣ Ensure Backend Service Is Running

Your AI resume analysis backend must be running at:

```
http://host.docker.internal:5050/analyze
```

If using Docker:
- Ensure correct network configuration
- Confirm port `5050` is exposed

### 3️⃣ Activate Workflow
Toggle the workflow to **Active**

---

## 🧪 Testing the API

You can test using Postman or curl:

```bash
curl -X POST http://localhost:5678/webhook/resume-analyze \
  -H "Content-Type: application/json" \
  -d '{
        "pdfPath": "/resumes/sample.pdf",
        "jobDescription": "Looking for a Machine Learning Engineer..."
      }'
```

---

## 🎯 Use Cases

- Resume scoring systems
- ATS compatibility checking
- AI-powered job matching
- Skill gap analysis platforms
- Recruitment automation systems

---

## 🏗 Architectural Design

This project follows a clean separation:

| Layer | Responsibility |
|-------|---------------|
| n8n | API orchestration |
| Backend AI Service | Resume analysis logic |
| Client | UI / Resume upload |

This makes the system:
- Modular
- Scalable
- Easy to extend
- Microservice-friendly

---

## 🚀 Future Improvements

- Add authentication (API keys / JWT)
- Add file upload handling (instead of file path)
- Add rate limiting
- Add logging & analytics
- Deploy backend to cloud (AWS/GCP)
- Add scoring visualization endpoint

---

## 🧠 Why This Is Resume-Worthy

This project shows:

- API-first thinking
- Automation + AI integration
- Backend orchestration
- Production-style architecture
- Real-world job matching application

It reflects system design skills beyond basic ML modeling.

---

## 📜 License

Open-source and free to use.
