# Indeed Job Scraper with Email Notifications

This Python project scrapes job listings from Indeed.com based on specified keywords and location, and sends email notifications when new jobs matching your criteria are found.

---

## Features

- Scrapes jobs from Indeed using keywords like "Network Engineer" and "Cybersecurity"
- Filters jobs by location (e.g., "remote")
- Sends email notifications to multiple recipients with new job listings
- Avoids duplicate notifications by tracking previously sent jobs

---

## Setup

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

2. **Install dependencies:**

```bash
pip install requests beautifulsoup4
```

3. **Configure settings:**

- Open `config.py`
- Set your job `KEYWORDS` and `LOCATION`
- Enter your sender email (`EMAIL_SENDER`), app password (`EMAIL_PASSWORD`), and list of receiver emails (`EMAIL_RECEIVERS`)

> **Note:** For Gmail, use an [App Password](https://myaccount.google.com/apppasswords) instead of your main password.

---

## Usage

Run the main script to fetch new jobs and send email notifications:

```bash
python main.py
```

---

## File Structure

- `config.py` — Configuration settings (keywords, email info, etc.)  
- `scraper.py` — Scrapes job listings from Indeed  
- `notifier.py` — Sends email notifications  
- `main.py` — Runs scraper and notifier  
- `job_data.json` — Stores previously sent jobs to avoid duplicates  

---

## License

This project is licensed under the MIT License.

---

## Contributions

Feel free to open issues or submit pull requests!