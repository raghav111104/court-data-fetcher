# 🏛️ Court Data Fetcher

This project fetches real-time court case data from the **e-Courts India portal** by accepting user input (case type, number, year, and CAPTCHA) and scrapes the result using Python, Flask, and BeautifulSoup.

---

## 📌 Features

- 🔍 Search cases using:
  - Case Type (e.g., Crl.A)
  - Case Number (e.g., 123)
  - Filing Year (e.g., 2022)
  - CAPTCHA (manual input required)
- 📤 CAPTCHA image fetched dynamically from the court website
- 🧠 Scrapes petitioner, respondent, filing date, hearing date, and latest PDF order
- 💾 Logs all queries into a local SQLite database (`case_data.db`)
- 🔁 Error handling for incorrect CAPTCHA or case not found

---

## ⚙️ Tech Stack

- **Frontend**: HTML, Jinja2 templates
- **Backend**: Python Flask
- **Scraping**: Requests, BeautifulSoup
- **Database**: SQLite (via `sqlite3`)

---

## 🚀 How to Run Locally

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/raghav111104/court-data-fetcher.git
   cd court-data-fetcher
