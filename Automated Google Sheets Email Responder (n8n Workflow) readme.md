# 📩 Automated Google Sheets Email Responder (n8n Workflow)

## 🚀 Overview

This project is an event-driven automation workflow built using **n8n**.  
It automatically sends a welcome email whenever a new row is added to a connected Google Sheet (typically from a Google Form submission).

After sending the email, the workflow updates the same row to prevent duplicate responses.

---

## 🧩 Features

- ✅ Detects new Google Sheet entries in real-time (polling every minute)
- ✅ Sends personalized emails dynamically
- ✅ Prevents duplicate email sends
- ✅ Automatically updates sheet status
- ✅ Fully automated once activated

---

## 🛠 Tech Stack

- **n8n** – Workflow Automation
- **Google Sheets API**
- **SMTP Email Service**
- Google Forms (optional integration source)

---

## 🔄 Workflow Architecture

```text
Google Sheets Trigger
        ↓
        IF (Sent != Y)
        ↓
     Send Email
        ↓
 Update Sheet (Sent = Y)
```

---

## 📌 How It Works

### 1️⃣ Google Sheets Trigger
- Polls every minute
- Triggers when a new row is added
- Connected via OAuth2 authentication

### 2️⃣ IF Condition
Checks:

```javascript
$json.Sent == "Y"
```

- If `Sent = Y` → Workflow stops
- If `Sent` is empty → Continue to email

### 3️⃣ Send Email Node
Dynamic fields used:

```javascript
To: {{$json.Email}}

Body:
{{$json.Name}}, nice to meet you, welcome aboard
```

Email is sent using configured SMTP credentials.

### 4️⃣ Update Google Sheet
Updates:
- `Sent = Y`
- Matches row using `Timestamp`

This ensures emails are never sent twice.

---

## 📊 Required Google Sheet Structure

| Column Name | Required | Description |
|-------------|----------|-------------|
| Timestamp   | ✅       | Unique row identifier |
| Name        | ✅       | User's name |
| Email       | ✅       | Recipient email |
| Phone       | Optional | User phone |
| Message     | Optional | Additional message |
| Sent        | ✅       | Email status flag |

---

## ⚙️ Setup Instructions

### 1️⃣ Import Workflow
- Open n8n
- Click **Import Workflow**
- Upload the provided `My workflow.json`

### 2️⃣ Configure Credentials
You must connect:
- Google Sheets OAuth2
- Google Sheets Trigger OAuth2
- SMTP credentials

### 3️⃣ Verify Sheet Columns
Ensure:
- `Sent` column exists
- `Timestamp` column exists
- Sheet name matches exactly

### 4️⃣ Activate Workflow
Click **Activate** to start automation.

---

## 🔐 Security Notes

- Do NOT commit credentials to GitHub
- Store secrets securely
- Use environment variables in production
- Restrict Google Sheet access permissions

---

## 📁 Project File

- `Automated Google Sheets Email Responder (n8n Workflow)` – Exported n8n workflow file

---

## 🎯 Use Cases

- Contact form auto-responder
- Event registration confirmation
- Newsletter onboarding
- Internship application acknowledgment
- Hackathon participant confirmation

---

## 🚀 Future Improvements

- Add HTML email templates
- Add retry logic for failed emails
- Add logging system
- Integrate Slack/Discord notifications
- Add email delivery tracking

---

## 🧠 What This Project Demonstrates

- Event-driven automation
- API integrations
- Conditional logic handling
- Idempotency control
- Real-world workflow orchestration

---

## 📜 License

This project is open-source and free to use.
