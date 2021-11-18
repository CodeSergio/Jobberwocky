from schemas import jobpost, jobalert
import jobberwocky_backend as be
from fastapi import FastAPI, status
from starlette.responses import RedirectResponse

app = FastAPI()

@app.get(
    path="/searchexternal/{searchterms}",
    status_code=status.HTTP_200_OK, 
    description='''this is a REST API to search for jobpostings 
    in the jobberwocky-extra-source external API. 
    You can search introducing words like Python or Java'''
    )
async def get_external_job(searchterms: str):
    result = await be.search_external_job(searchterms)
    return result

@app.get(
    path="/searchinternal/{searchterms}",
    status_code=status.HTTP_200_OK, 
    description='''this is a REST API to search for jobpostings 
    in the jobberwocky internal API. 
    You can search introducing words like Python or Java'''
    )
async def get_internal_job(searchterms: str):
    result = await be.search_internal_job(searchterms)
    return result

@app.get(
    path="/searchall/{searchterms}",
    status_code=status.HTTP_200_OK, 
    description='''this is a REST API to search for jobpostings 
    consolidating results from jobberwocky's internal and external APIs. 
    You can search introducing words like Python or Java'''
    )
async def get_all_jobs(searchterms: str):
    result = await be.search_all_jobs(searchterms)
    return result

@app.post(
    path="/insertjob/",
    response_model=jobpost,
    status_code=status.HTTP_201_CREATED, 
    description='''this is a REST API to insert a new jobposting 
    in the jobberwocky dataset.''')
async def post_job(jobpost: jobpost):
    await be.insert_job(jobpost.name, jobpost.salary, jobpost.country, jobpost.skills)
    return jobpost

@app.post(
    path="/insertalert/", 
    response_model=jobalert,
    status_code=status.HTTP_201_CREATED, 
    description='''this is a REST API to insert a new job alerts.''')
async def post_job_alert(jobalert: jobalert):
    await be.insert_jobalert(jobalert.alert_term, jobalert.email)
    return jobalert

@app.get(
    path="/",
    status_code=status.HTTP_200_OK, 
    description='''This path is only for redirecting the root URL to the APIs documentation'''
    )
async def redirect():
    return RedirectResponse(url="/docs/")