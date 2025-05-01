import re
import datetime
import json
import os
from google import genai
from dotenv import load_dotenv
from parse_resume import ResumeParser
from scrape_jobs import JobScraper

load_dotenv()  # take environment variables from .env.

my_secret_key = os.getenv("SECRET_KEY")

def clean_job_descs(jobs):
    for job in job_list:
        if isinstance(job['description'], str):
            job['description'] = re.sub(r'\s{2,}', '\n', job['description'])
            job['description'] = re.sub(r'[^\x00-\x7F]+', '', job['description'])

def convert_dates_iso(jobs):
    for job in job_list:
        date_posted = job["date_posted"]
        if isinstance(date_posted, float):
            job["date_posted"] = datetime.date(year=1970, month=1, day=1).isoformat()
        else:
            job["date_posted"] = date_posted.isoformat()


if __name__ == "__main__":
    gemini = genai.Client(api_key=my_secret_key)
    resume_parser = ResumeParser(gemini)
    parsed_resume = resume_parser.parse_resume('Austin_career_journey.pdf')


    job_titles = resume_parser.get_job_titles(parsed_resume)
    job_list = JobScraper.get_jobs(job_titles)

    convert_dates_iso(job_list)
    clean_job_descs(job_list)




    jobs = [{"jobs": job_list}]

    with open("jobs.json", "w") as f:
        json.dump(jobs, f)
