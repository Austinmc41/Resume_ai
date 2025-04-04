import json
from typing import List

import pymupdf4llm

class ResumeParser:

    def __init__(self, client):
        self.client = client

    def parse_resume(self, pdf):
        response = self.client.models.generate_content(
            model="gemini-2.0-flash",
            contents="""I will provide a resume in Markdown format. Your task is to extract relevant information and structure it into a JSON object with the following fields: work_experience, skills, projects, and education. Each field should be an array of structured objects containing relevant details.
JSON Structure Example:
{
"work_experience": [
{
"company": "Company Name",
"position": "Job Title",
"start_date": "YYYY-MM",
"end_date": "YYYY-MM or Present",
"description": "Brief description of responsibilities and achievements."
}
],
"skills": ["Skill1", "Skill2", "Skill3"],
"projects": [
{
"name": "Project Name",
"description": "Brief description of the project.",
"technologies": ["Tech1", "Tech2"]
}
],
"education": [
{
"institution": "University Name",
"degree": "Degree Earned",
"start_date": "YYYY-MM",
"end_date": "YYYY-MM"
}
]
}
Ensure that dates are in YYYY-MM format, and all lists contain relevant structured objects. Do not include unnecessary information. Only extract relevant details from the resume.

Here is the Markdown resume:
        """ + pymupdf4llm.to_markdown(pdf)
        ).text
        return json.loads(response[response.find('{'):response.rfind('}') + 1], strict=False)

    def get_job_titles(self, resume) -> List:
        job_titles = self.client.models.generate_content(
            model="gemini-2.0-flash",
            contents=("Given their resume below, give some suggested job titles that this person should apply to. "
                      "Do not add any preamble or conclusion, only return a comma-delineated a list.\n")
                     + str(resume)
        ).text.split(',')
        return [jt.strip() for jt in job_titles]
