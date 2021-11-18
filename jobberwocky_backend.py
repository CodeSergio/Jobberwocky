from gmail_client import send_gmail
import configparser
import requests
import json
import pandas as pd

parser = configparser.ConfigParser()
parser.read("config.txt")
job_dataset = parser.get("config", "job_dataset")
alert_dataset = parser.get("config", "alert_dataset")
external_api = parser.get("config", "external_api")
sender_address = parser.get("config", "sender_address")
sender_pass = parser.get("config", "sender_pass")

async def search_external_job(searchterms: str):
    searchterms=searchterms.strip()
    data_external=requests.get(external_api+searchterms).json()
    job_dict={}
    result=[]
    for name, salary, country, skills in data_external:
        job_dict={  'name':name, 
                    'salary':salary, 
                    'country': country, 
                    'skills': skills, 
                    'Origin':'External'}
        result.append(job_dict)    
    return result

async def search_internal_job(searchterms: str):
    searchterms=searchterms.strip()
    df = pd.read_json(job_dataset)
    df["Origin"]="Internal"
    name = df["name"].str.contains(searchterms, case = False)
    result = df[name].to_dict('records')
    return result

async def search_all_jobs(searchterms: str):
        jobs_external = await search_external_job(searchterms)
        jobs_internal = await search_internal_job(searchterms)
        all_jobs = jobs_external + jobs_internal
        return all_jobs

async def insert_job(name, salary, country, skills):
    dicc={
            "name": name,
            "salary": salary,
            "country": country,
            "skills": skills
            }

    a_file = open(job_dataset, "r")
    json_object = json.load(a_file)
    a_file.close()
    json_object.append(dicc)

    with open(job_dataset, "w") as write_file:
        json.dump(json_object, write_file, indent=4)
   
    await send_alerts(name, salary, country, skills)
    return(name, salary, country, skills)


async def insert_jobalert(alert_term, email):
    alert_term = alert_term.strip()
    email = email.strip().lower()
    dicc={
            "alert_term": alert_term,
            "email": email
            }
    a_file = open(alert_dataset, "r")
    json_object = json.load(a_file)
    a_file.close()
    json_object.append(dicc)
    with open(alert_dataset, "w") as write_file:
        json.dump(json_object, write_file, indent=4)
    
    return(alert_term, email)

async def send_alerts(name, salary, country, skills):
    alerts=pd.read_json(alert_dataset)
    for index, row in alerts.iterrows():
        print(index)
        alert_term = row['alert_term']
        receiver_address = row['email']
        if name.lower().find(alert_term.lower()) != -1:
            subject='You have new job postings related to ' + alert_term
            mail_content = 'Name: '+ name  + '\n' +'Salary: '+ str(salary) + '\n' +'Country: '+ country + '\n'+'Skills: '+ str(skills)                       
            send_gmail(sender_address, sender_pass, receiver_address, subject, mail_content)
