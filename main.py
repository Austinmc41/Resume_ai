import os
from google import genai
from dotenv import load_dotenv
from parse_resume import ResumeParser
from scrape_jobs import JobScraper

load_dotenv()  # take environment variables from .env.

my_secret_key = os.getenv("SECRET_KEY")

if __name__ == "__main__":
    gemini = genai.Client(api_key=my_secret_key)
    resume_parser = ResumeParser(gemini)
    parsed_resume = resume_parser.parse_resume('Austin_career_journey.pdf')
    job_titles = resume_parser.get_job_titles(parsed_resume)
    print(JobScraper.get_jobs(job_titles))
