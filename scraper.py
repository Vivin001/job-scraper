# scraper.py

import requests
import json
from config import KEYWORDS
from urllib.parse import urljoin


def fetch_jobs():
    resp = requests.get("https://remoteok.com/api",
                        headers={"User-Agent": "Mozilla/5.0"})
    jobs_data = resp.json()

    seen = set()
    try:
        with open("job_data.json") as f:
            seen = set(item["link"] for item in json.load(f))
    except FileNotFoundError:
        pass

    new = []
    for job in jobs_data:
        link = job.get("url")
        if not link or link in seen:
            continue
        tags = job.get("tags", [])
        if any(keyword.lower() in " ".join(tags).lower() for keyword in KEYWORDS):
            entry = {
                "title": job["position"],
                "company": job["company"],
                "location": job.get("location", "remote"),
                "link": link
            }
            new.append(entry)
            seen.add(link)

    with open("job_data.json", "w") as f:
        json.dump([{"link": link} for link in seen], f, indent=4)

    return new
