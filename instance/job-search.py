import requests
import json
url = "https://jsearch.p.rapidapi.com/search"

from sqlalchemy import create_engine, text, inspect
engine = create_engine('sqlite:///db.sqlite', pool_pre_ping=True)
inspector = inspect(engine)
url_e = engine.url

# checking if the connection is made
try:
    with engine.connect() as conn:
       results = conn.execute(text("SELECT desired_job, work_experience, education_level, industry_skills, job_location, salary_range, willing_to_relocate, desired_job_type, job_requirements FROM profile WHERE user_id = user_id"))
       for result in results:
        print(result)

        formatted_item = {
            "job_titles": result[0],
            "query": f"{result[0] in result[4]}",
        }

        user_profile = {
            "work_experience": result[1],
            "education_level": result[2],
            "industry_skills": result[3],
            "job_country": result[4],
            "salary_range": result[5],
            "willing_to_relocate": result[6],
            "job_employment_type": result[7],
        }
        

    print(f" Successfully Connected to the database: {url_e.database}")
except Exception as ex:
    print(f" Sorry Could not connect to the database: {ex}")

headers = {
	"X-RapidAPI-Key": "d87469a432mshb55766581cdb310p140576jsnd3ef94343b6e",
	"X-RapidAPI-Host": "jsearch.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=formatted_item)

prased_response = json.loads(response.text)



#print(type(prased_response))

"""
for key, value in prased_response.items():
    print("Inspecting item with key:", key)
    print("Item value:", value)
    if isinstance(value, dict) and 'job_title' in value:
        print("Job title found:", value['job_title'])
    else:
        print("Job title not found in this item.")
"""

job_listings = []
# getting job titles
if 'data' in prased_response:
    for job_listing in prased_response['data']:
        if 'job_title' in job_listing:
            print(job_listing['job_title'])
            print(job_listing['employer_name'])
            print()
            print(job_listing['employer_logo'])
            print()
            print(job_listing['job_apply_link'])
            print()
            print(job_listing['job_country'])
            print(job_listing['job_employment_type'])
            print(job_listing['job_required_skills'])
            print(job_listing['job_required_experience'])
            print(job_listing['job_required_education'])
            job_data = {
                #"job_title": job_listing['job_title'],
                "job_country": job_listing['job_country'],
                "job_employment_type": job_listing['job_employment_type'],
                "job_required_skills": job_listing['job_required_skills'],
                "job_required_experience": job_listing['job_required_experience'],
                "job_required_education_level": job_listing['job_required_education']
            }
            job_listings.append({'job_data': job_data})
            #print(job_listing['salary_range'])
    #job_bata = prased_response['data']

"""
#matching algorithm
def calculate_matching_score(user_profile, job_data):
    score = 0
    # criteria and weights
    criteria_weights = {
        'job_country': 0.5,
        'job_employment_type': 0.5,
        'job_required_skills': 0.3,
        'job_required_experience': 0.3,
        'job_required_education_level': 0.2,
    }
    #print("User Profile:", user_profile)
    #print("Job Data:", job_data)


    # Calculate score based on criteria
    for criterion, weight in criteria_weights.items():
        #print(f"Checking criterion: {criterion}")
        if criterion in user_profile and criterion in job_data['job_data']:
            #print(f"Criterion '{criterion}': User Profile - {user_profile[criterion]}, Job Data - {job_data['job_data'][criterion]}")
            if user_profile[criterion] == job_data['job_data'][criterion]:
                score += weight
                print(f"Matching criterion: {criterion}, Weight: {weight}, Score: {score}")
    return score
def match_jobs(user_profile, job_listings):
    matched_jobs = []
    for job_listing in job_listings:
        
        score = calculate_matching_score(user_profile, job_listing)
        matched_jobs.append((job_listing, score))

    # Sort matched jobs by score in descending order
    matched_jobs.sort(key=lambda x: x[1], reverse=True)
    #print(job_listings)
    return matched_jobs

# Match user profile with job listings
matched_jobs = match_jobs(user_profile, job_listings)
for job, score in matched_jobs:
    print(f"Job Title: {job_data['job_title']}")
    #print(f"Employer Name: {job['employer_name']}")
    print(f"Matching Score: {score}")
    print()
"""
