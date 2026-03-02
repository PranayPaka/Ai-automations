# 🤖 Human-in-the-Loop AI Email Automation (IMAP + OpenAI + Approval System)

## 🚀 Overview

This project is a **Human-in-the-Loop AI Email Automation System** built using **n8n**.

It automatically:
1. Reads incoming emails via IMAP
2. Summarizes the email using AI
3. Generates a professional response using an LLM
4. Sends the AI-generated reply for human approval
5. Sends the final email only after approval

This ensures automation speed while maintaining human control.

---

## 🧠 Why This Project Matters

This workflow demonstrates:

- AI-powered email summarization
- AI-generated professional replies
- Human approval before execution
- Secure outbound email handling
- Real-world AI workflow orchestration

Perfect example of **safe AI automation for business environments**.

---

## 🛠 Tech Stack

- **n8n** – Workflow Automation
- **IMAP** – Email Trigger
- **SMTP** – Outgoing Emails
- **OpenAI (gpt-4o-mini / deepseek-chat)** – AI Summarization & Reply Generation
- LangChain nodes inside n8n

---

## 🔄 Workflow Architecture

```text
IMAP Email Trigger
        ↓
 Convert HTML → Markdown
        ↓
 AI Summarization (≤100 words)
        ↓
 AI Email Writer (Professional Reply)
        ↓
 Set Email Text
        ↓
 Send Approval Email (Human Review)
        ↓
 IF Approved?
        ↓
 Send Final Email to Original Sender
```

---

## 📌 How It Works

### 1️⃣ Email Trigger (IMAP)

- Monitors inbox for new emails
- Extracts:
  - `from`
  - `to`
  - `subject`
  - `textHtml`

---

### 2️⃣ Markdown Conversion

Converts incoming HTML email into Markdown format for better AI processing.

---

### 3️⃣ Email Summarization Chain

Uses LLM to:

```
Write a concise summary in max 100 words.
```

This reduces long email threads into structured summaries.

---

### 4️⃣ AI Email Generation

System prompt:

> You are an expert at answering emails.  
> Be professional, concise, business-focused.  
> Never exceed 100 words.

The AI generates only the email body (no subject).

---

### 5️⃣ Human Approval Step

An approval email is sent internally containing:

- 📩 Original message
- 🤖 AI-generated response
- Approval mechanism

This ensures:
- No incorrect responses
- No hallucinated information sent automatically
- Full business control

---

### 6️⃣ Conditional Check (Approved?)

If:

```javascript
$json.data.approved == true
```

Then:
- Send final email to original sender

Otherwise:
- Workflow stops

---

## 📂 Project File

- `Very simple Human in the loop system email with AI e IMAP.json`  
  (Exported n8n workflow)

---

## 🔐 Security & Safety Features

- Human approval gate before sending
- Professional AI constraints
- Word limit enforcement (≤100 words)
- Controlled SMTP sending
- Business-ready response formatting

---

## 🎯 Use Cases

- Business customer support
- Sales inquiry responses
- Client communication drafting
- Internal approval workflows
- AI-assisted executive inbox management

---

## ⚙️ Setup Instructions

### 1️⃣ Import Workflow
- Open n8n
- Click **Import**
- Upload the provided JSON file

### 2️⃣ Configure Credentials
You must connect:

- IMAP Email Credentials
- SMTP Credentials
- OpenAI API Credentials

### 3️⃣ Activate Workflow
Toggle **Active** once everything is configured.

---

## 🚀 Future Improvements

- Add sentiment analysis
- Add priority classification
- Add CRM integration
- Add Slack approval option
- Add multi-user approval routing
- Add audit logging

---

## 🧠 What This Demonstrates

This project showcases:

- Responsible AI implementation
- Human-in-the-loop architecture
- LLM orchestration
- Business automation workflows
- Safe AI deployment patterns

---

## 📜 License

Open-source and free to use.
