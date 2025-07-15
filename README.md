# RemoteOK Job Scraper with Email Notifications

This Python project fetches remote job listings from RemoteOK.com based on specific keywords and sends email alerts when new jobs matching your criteria are found.

---

## Features

-  Pulls jobs from RemoteOK's public API.
-  Filters jobs by tags/keywords (e.g., "network", "engineer", "cybersecurity")
-  Sends email notifications with job details
-  Avoids duplicate alerts using a local JSON file
-  Clean and modular project structure

---

## Setup

### 1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/job-scraper.git
cd job-scraper
```

### 2. **Install Dependencies**

```bash
pip install requests
```

### 3. **Edit Configuration**

Open `config.py` and update:

```python
KEYWORDS = ["network", "engineer", "cybersecurity"]

EMAIL_SENDER = "your_email@gmail.com"
EMAIL_PASSWORD = "your_app_password"
EMAIL_RECEIVERS = ["you@example.com", "colleague@example.com"]
```

> 💡 Use a [Gmail App Password](https://myaccount.google.com/apppasswords) instead of your regular password if you use 2FA.

---

## Usage

Run the main script:

```bash
python main.py
```

If new jobs match your criteria, you’ll receive an email with job titles, companies, and direct links.

---

## 📁 File Structure

```
job-scraper/
├── config.py        # Keyword & email config
├── scraper.py       # Pulls jobs from RemoteOK
├── notifier.py      # Sends email alerts
├── main.py          # Orchestrates everything
├── job_data.json    # Stores sent job links
├── README.md        # You’re reading it
```

---

## 📄 License

MIT License — free to use, modify, and share.

---

## Contributing

Feel free to fork this repo, suggest changes, or open issues. Pull requests are welcome!
