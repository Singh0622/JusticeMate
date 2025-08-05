# JusticeMate: AI-Powered Legal Assistant Web App

JusticeMate is a web application that helps users understand their legal rights, draft formal complaint letters, mediate disputes, and translate complex legal language into plain, easy-to-understand text. It leverages Google’s Gemini 1.5-flash AI model for generating legal insights and suggestions under the Indian legal context.

---

## Features

- Summarize user’s legal rights under Indian law  
- Draft formal complaint letters tailored for Indian context  
- Summarize conflicting parties’ positions and provide mediation solutions  
- Translate complex legalese into plain language for better understanding  

---

## Tech Stack

- **Backend:** Python, Flask, Google Generative AI (Gemini) SDK  
- **Frontend:** Your choice (supports plain HTML/CSS/JavaScript or any frontend framework)  
- **API:** RESTful endpoints to communicate between frontend and backend  
- **Environment:** `.env` file for securely storing API keys  
- **Deployment:** Suitable for deployment on cloud platforms like Render, Fly.io, Heroku, etc.

---

## Setup Instructions

### Prerequisites

- Python 3.8 or above  
- An API key for Google Gemini (or your AI model provider)  
- Git (optional, for cloning the repo)  

### Installation

1. Clone the repository (or download the project files):git clone https://github.com/Singh0622/justicemate.git
cd justicemate

2. Create and activate a virtual environment (recommended):

python -m venv venv
source venv/bin/activate # On Linux/macOS
venv\Scripts\activate # On Windows

3. Install dependencies:
pip install -r requirements.txt

4. Create a `.env` file in the project root with your Gemini API key:
GEMINI_API_KEY=your_real_api_key_here

---

## Running the App Locally

Start the Flask server:
python app.py

By default, the app will run on `http://localhost:5000/`.  
You can connect your frontend by making HTTP POST requests to `/api/justicemate`.

---

## API Usage

### Endpoint
- `POST /api/justicemate`

### Request JSON

| Field             | Description                                    | Example                         |
|-------------------|------------------------------------------------|---------------------------------|
| `issue_description`| Description of the legal issue                  | `"Accident due to oil spill..."`|
| `help_type`       | Type of help required: `"rights"`, `"complaint"`, `"mediation"`, `"legalese-to-plain"` | `"complaint"`                   |
| `opposing_party`  | (Optional) Description of opposing party's position for mediation | `"Party 2 description..."`      |

### Response JSON

| Field   | Description               |
|---------|---------------------------|
| `result`| AI-generated legal response|

---

## Frontend Integration

You can use any frontend technology to interact with this app.  
Example JavaScript snippet to call the API:

fetch('http://localhost:5000/api/justicemate', {
method: 'POST',
headers: { 'Content-Type': 'application/json' },
body: JSON.stringify({
issue_description: userIssue,
help_type: selectedHelpType,
opposing_party: opposingParty || ''
})
})
.then(response => response.json())
.then(data => {
console.log('JusticeMate response:', data.result);
});

---

## Deployment

- Deploy the Flask app to platforms like Render, Fly.io, or Heroku.  
- Store your `GEMINI_API_KEY` securely as environment variables on the platform.  
- Optionally, deploy your frontend separately or serve via Flask’s static files.

---

## Security and Best Practices

- Keep your API keys secure and never expose them publicly.  
- Use HTTPS for secure communication in production.  
- Enable CORS responsibly if frontend and backend are on different origins.  
- Add rate limiting or CAPTCHA if you expect heavy usage to prevent abuse.

---

## License

This project is open source under the [MIT License](LICENSE).

---

## Acknowledgments

- Google Generative AI for providing Gemini language models.  
- Flask for the lightweight web framework.  
- Inspiration from many open source AI-assisted legal tools.

---

If you have any questions or want to contribute, please open an issue or submit a pull request.

---
