import requests
import json


def scrape_jobs(role, location):
    resp = requests.get("https://remoteok.com/api",
                        headers={"User-Agent": "Mozilla/5.0"})
    jobs_data = resp.json()

    seen = set()
    try:
        with open("job_data.json") as f:
            for item in json.load(f):
                if "link" in item:
                    seen.add(item["link"])
    except FileNotFoundError:
        pass

    new = []
    for job in jobs_data[1:]:  # Skip site metadata
        link = job.get("url")
        if not link or link in seen:
            continue

        title = job.get("position", "").lower()
        tags = " ".join(job.get("tags", [])).lower()
        job_location = job.get("location", "remote").lower()

        if (role.lower() in title or role.lower() in tags) and location.lower() in job_location:
            entry = {
                "title": job["position"],
                "company": job["company"],
                "location": job.get("location", "remote"),
                "link": link
            }
            new.append(entry)
            seen.add(link)

    # Save updated seen links
    with open("job_data.json", "w") as f:
        json.dump([{"link": link} for link in seen], f, indent=4)

    return new
