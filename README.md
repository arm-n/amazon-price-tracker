````markdown
# 📉 Amazon Price Tracker with Email Alerts

This is a Python script that monitors the price of a product on Amazon and sends an email alert when the price drops below your specified target.

---

## ✅ Features

- Scrapes the current price of an Amazon product.
- Compares it with your target price.
- Sends an email notification if the price drops.
- Uses environment variables for secure credentials handling.
- Clean, modular, and readable code.

---

## 🛠 Requirements

- Python 3.7+
- Packages:
  - `requests`
  - `beautifulsoup4`
  - `python-dotenv`

You can install all requirements using:

```bash
pip install -r requirements.txt
````

---

## 📦 Installation & Setup

1. **Clone the Repository:**

```bash
git clone https://github.com/arm-ne/amazon-price-tracker.git
cd amazon-price-tracker
```

2. **Create `.env` File:**

Create a `.env` file in the root directory of the project and add your email credentials:

```
SMTP_ADDRESS=smtp.gmail.com
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_app_password_here
```


## 🔐 How to Create an App Password (Gmail)

If you use Gmail with 2-Step Verification enabled, you need to create an **App Password**:

1. Go to [Google Account Security Settings](https://myaccount.google.com/security).
2. Under "Signing in to Google", enable **2-Step Verification**.
3. Once enabled, you’ll see the **App Passwords** option.
4. Generate a new app password for "Mail" > "Windows Computer" (or custom).
5. Copy the 16-digit app password and paste it into `.env` as `EMAIL_PASSWORD`.

> Without an app password, Gmail will block sign-in from your script.

---

## 🧪 How to Use the Script

1. Open `main.py` in your IDE (like PyCharm or VSCode).
2. Update the following:

   * `URL`: the Amazon product link
   * `TARGET_PRICE`: your desired price threshold
3. Run the script:

```bash
python main.py
```

If the price is below your threshold, an email alert will be sent to your inbox.

---

## 📤 Email Example

```
Subject: Price Drop Alert! 🎉

The price is now $97.99!

Check the deal here: https://www.amazon.com/dp/B075CYMYK6
```

---

## ⚙️ Customization

* You can schedule this script using `cron` (Linux/macOS) or Task Scheduler (Windows) for automated price checks.
* Add logging or notifications via Telegram/Slack if needed.

---

## ⚠️ Disclaimer

* This script is for educational purposes.
* Amazon's layout may change over time, which may break the script.
* Use scraping responsibly and avoid frequent requests.

---

## 📬 License

MIT License – use freely, modify and contribute back if you like!



