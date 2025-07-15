# main.py

from scraper import fetch_jobs
from notifier import send_email


def main():
    print("Starting job scraper...")
    new_jobs = fetch_jobs()
    print(f"Found {len(new_jobs)} new job(s).")

    send_email(new_jobs)


if __name__ == "__main__":
    main()
