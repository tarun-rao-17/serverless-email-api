# 📧 Serverless Email API (Python + AWS SES)

A simple REST API built using the **Serverless Framework (Python)** that sends emails through **AWS SES**.  
It supports offline testing and includes error handling with appropriate HTTP response codes.

---

## 🚀 Features
- Built using **Serverless Framework**
- Runs **locally** using `serverless-offline`
- Uses **AWS SES** for sending emails
- Includes full **error handling** and status codes
- Simple JSON-based REST API

---

## 🧩 Project Structure

serverless-email-api/
├── handler.py # Lambda function (email logic)
├── serverless.yml # Serverless configuration
├── requirements.txt # Python dependencies
└── README.md # Documentation


---

## 🛠️ Setup Instructions

### 1️⃣ Clone the project
```bash
git clone https://github.com/<your-username>/serverless-email-api.git
cd serverless-email-api
pip install -r requirements.txt
npm install serverless-offline
serverless offline
Then send a POST request using Postman or curl:
POST http://localhost:3000/dev/send
{
  "message": "Email sent successfully",
  "response": {
    "MessageId": "12345..."
  }
}
❌ Error
{
  "message": "Error sending email",
  "error": "details..."
}
⚙️ Tech Stack

Python 3.9

Serverless Framework

AWS SES (Simple Email Service)

Serverless Offline
🧑‍💻 Author

Tarun Rao
📍 Bengaluru, India
