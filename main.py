from parse_resume import ResumeParser
import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

my_secret_key = os.getenv("SECRET_KEY")

if __name__ == "__main__":
    resume_parser = ResumeParser(my_secret_key)
    print(resume_parser.parse_resume('Austin_career_journey.pdf'))