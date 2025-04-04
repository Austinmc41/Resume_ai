from tqdm import tqdm
from jobspy import scrape_jobs

class JobScraper:

    @classmethod
    def get_jobs(cls, job_titles, locations=['Atlanta GA']):
        jobs = []
        for location in locations:
            for jt in tqdm(job_titles):
                try:
                    jobs.extend(scrape_jobs(
                        site_name=["indeed", "linkedin", "zip_recruiter", "glassdoor", "google", "bayt", "naukri"],
                        search_term=jt,
                        google_search_term=f"Remote {jt} jobs since yesterday" if location == 'remote' else f"{jt} jobs near {location} since yesterday",
                        location=location,
                        results_wanted=10,
                        hours_old=72,
                        country_indeed='USA',
                        is_remote=location == 'remote',
                        # linkedin_fetch_description=True # gets more info such as description, direct job url (slower)
                        # proxies=["208.195.175.46:65095", "208.195.175.45:65095", "localhost"],
                    ).to_dict(orient='records'))
                except Exception:
                    continue
        return jobs
