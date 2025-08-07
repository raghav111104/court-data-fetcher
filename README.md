# 🏛️ Court Data Fetcher

This project fetches real-time court case data from the **e-Courts India portal** by accepting user input (case type, number, year, and CAPTCHA), and scrapes the result using Python, Flask, and BeautifulSoup.

---

## 📌 Features

- 🔍 Search cases using:
  - Case Type (e.g., Crl.A)
  - Case Number (e.g., 123)
  - Filing Year (e.g., 2022)
  - CAPTCHA (manual input required)
- 📤 CAPTCHA image fetched dynamically from the court website
- 🧠 Scrapes:
  - Petitioner
  - Respondent
  - Filing Date
  - Next Hearing Date
  - Latest Order (PDF link)
- 💾 Logs all queries into a local SQLite database (`case_data.db`)
- 🔁 Error handling for incorrect CAPTCHA or case not found

---

## ⚙️ Tech Stack

- **Frontend**: HTML, Jinja2 templates  
- **Backend**: Python Flask  
- **Scraping**: Requests, BeautifulSoup  
- **Database**: SQLite (`sqlite3`)

---

## 🚀 How to Run Locally

1. **Clone the Repository**
   ```bash
   git clone https://github.com/raghav111104/court-data-fetcher.git
   cd court-data-fetcher
Create Virtual Environment (Optional)

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate  # For Windows
Install Dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run the App

bash
Copy
Edit
python app.py
Open in Browser

cpp
Copy
Edit
http://127.0.0.1:5000
📝 Screenshot

Replace screenshot.png with your actual file name if different.

⚠️ Limitations
🔐 CAPTCHA must be manually entered (no OCR or bypass)

🧪 Data depends on availability from e-Courts

🛑 Not for production — demo/learning purpose only

👨‍💻 Author
Raghav Daga
