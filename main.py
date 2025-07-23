import os
import smtplib
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

# Environment variables
SMTP_ADDRESS = os.getenv("SMTP_ADDRESS")
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# URL to monitor
URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
HEADERS = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

# Fetch and parse the webpage
response = requests.get(url= URL,headers= HEADERS)
soup = BeautifulSoup(response.text, "html.parser")

# Find and clean price
price_text = soup.find(name="span", class_="aok-offscreen").getText()  # e.g., "$99.99"
price = float(price_text.split()[0].replace("$",""))
print(f"Current price: ${price}")

# Price check and send email if condition met
TARGET_PRICE = 100  # Set your desired threshold

if price < TARGET_PRICE:
    subject = "Price Drop Alert! 🎉"
    body = f"The price is now ${price}!\n\nCheck the deal here: {URL}"
    message = f"Subject: {subject}\n\n{body}"

    try:
        with smtplib.SMTP(SMTP_ADDRESS, 587) as connection:
            connection.starttls()
            connection.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            connection.sendmail(
                from_addr=EMAIL_ADDRESS,
                to_addrs=EMAIL_ADDRESS,
                msg=message.encode('utf-8')
            )
        print("✅ Email sent successfully!")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
else:
    print("No alert sent. Price hasn't dropped yet.")
