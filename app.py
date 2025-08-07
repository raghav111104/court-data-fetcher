from flask import Flask, render_template, request, flash, send_file
from scraper import fetch_case_data
from database import init_db, log_query
import requests
from io import BytesIO

app = Flask(__name__)
app.secret_key = "secret_key_for_flash"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        case_type = request.form["case_type"]
        case_number = request.form["case_number"]
        filing_year = request.form["filing_year"]
        captcha_text = request.form["captcha"]

        try:
            # Fetch real case data
            case_data, raw_html = fetch_case_data(case_type, case_number, filing_year, captcha_text)

            # Save query and raw HTML to database
            log_query(case_type, case_number, filing_year, raw_html)

            return render_template("index.html", result=case_data)

        except Exception as e:
            flash(f"Error: {str(e)}")

    return render_template("index.html", result=None)

# Route to serve captcha image
@app.route("/captcha")
def get_captcha():
    captcha_url = "https://services.ecourts.gov.in/ecourtindia_v6/captcha.jpg"
    response = requests.get(captcha_url)
    return send_file(BytesIO(response.content), mimetype='image/jpeg')

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
