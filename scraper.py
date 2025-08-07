import requests
from bs4 import BeautifulSoup

def fetch_case_data(case_type, case_number, filing_year, captcha_text):
    session = requests.Session()

    # Step 1: Get the main page to get cookies
    url = "https://services.ecourts.gov.in/ecourtindia_v6/?p=casestatus/index&app_token=&app_name="

    response = session.get(url)
    if response.status_code != 200:
        raise Exception("Failed to load main page")

    # Step 2: Submit the form with data and captcha
    form_url = "https://services.ecourts.gov.in/ecourtindia_v6/?p=casestatus/index&app_token=&app_name="

    payload = {
        "case_type": case_type,
        "case_number": case_number,
        "case_year": filing_year,
        "captcha_code": captcha_text,
        "state_code": "24",        # Update as per your needs
        "dist_code": "1",          # Update as per your needs
        "court_code": "",          # Can be left blank
        "submit": "Search"
    }

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": url
    }

    post_response = session.post(form_url, data=payload, headers=headers)

    if "Petitioner" not in post_response.text:
        raise Exception("Captcha failed or case not found")

    # Step 3: Parse the HTML
    soup = BeautifulSoup(post_response.text, "html.parser")
    
    # Dummy fallback in case selectors change
    petitioner = soup.find("td", text="Petitioner").find_next_sibling("td").text.strip()
    respondent = soup.find("td", text="Respondent").find_next_sibling("td").text.strip()
    filing_date = soup.find("td", text="Filing Date").find_next_sibling("td").text.strip()
    next_hearing = soup.find("td", text="Next Hearing Date").find_next_sibling("td").text.strip()

    return {
        "petitioner": petitioner,
        "respondent": respondent,
        "filing_date": filing_date,
        "hearing_date": next_hearing,
        "latest_pdf": "#"  # You can extract PDF URL if available
    }, post_response.text  # Also return raw HTML for DB log
