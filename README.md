# 💼 JobSrybe - Jobs to your Inbox (RemoteOK + Flask)

This Python project is a Flask-based web application that scrapes remote job listings from [RemoteOK.com](https://remoteok.com) based on **user-provided role and location**, and sends personalized job listings to the provided **email address**.

---

## Features

- ✅ Live job scraping from RemoteOK’s public API  
- ✅ User inputs (role, location, email) via web form  
- ✅ HTML-formatted email alerts with job title, company, location, and apply link  
- ✅ Prevents duplicate job notifications using a local `job_data.json` tracker  
- ✅ Clean modular structure (Flask + Email + Scraper logic)  
- ✅ Mobile-friendly UI  

---

##  How It Works

1. User opens the web form  
2. Enters: Name, Email, Desired Role, Preferred Location  
3. On submission:  
   - Jobs are fetched from RemoteOK API  
   - Filtered by the user input  
   - Sent to the email address as an HTML report  

---

##  Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Vivin001/job-scraper.git
cd job-scraper
```

### 2. Install Required Python Packages

```bash
pip install flask requests
```

### 3. Configure Gmail Settings

Edit `config.py`:

```python
EMAIL_SENDER = "your_email@gmail.com"
EMAIL_PASSWORD = "your_gmail_app_password"
```

> 💡 Use a [Gmail App Password](https://myaccount.google.com/apppasswords) (required if 2FA is enabled).

---

##  Run the App

```bash
python app.py
```

Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser and fill out the form to get job updates via email.

---

##  Project Structure

```
job-scraper/
├── app.py              # Flask web server
├── config.py           # Email credentials
├── scraper.py          # RemoteOK API fetch & filter
├── notifier.py         # Email sending logic
├── job_data.json       # Tracks already-sent jobs
├── templates/
│   ├── index.html      # User form (HTML)
│   └── success.html    # Success page after submission
├── README.md
```

---

##  Troubleshooting

- **Not receiving email?**
  - Double-check Gmail App Password
  - Make sure `EMAIL_SENDER` has enabled "Allow less secure apps" *(not needed if using App Password)*
  - Check spam folder

- **No job listings in email?**
  - Try broader role keywords (e.g., `Developer`, `Engineer`)
  - RemoteOK may not have matching listings at the moment

---

## 🖼 Sample UI

> 📬 Users submit this form to receive job alerts.

### 🔹 Job Search Form

<img width="900" height="500" alt="image" src="https://github.com/user-attachments/assets/da536481-fb2b-4673-bcf8-094edb88f9a0" />


### ✅ Success Page

<img width="900" height="338" alt="image" src="https://github.com/user-attachments/assets/5ce88ab0-1350-4ced-bee2-bbd6c6308dd2" />


---

## 📜 License

MIT License — feel free to use, modify, and share ⭐

---

## 🤝 Contributing

Got ideas or improvements? Open a PR or issue — contributions are welcome!
