# Jobberwocky APIs

## How to Install on Windows:
```bash
$ mkdir jobberwocky
$ cd jobberwocky
$ py -m venv venv 
$ pip install -r requirements.txt
$ venv Scripts\activate.bat
$ git clone https://github.com/avatureassessment/jobberwocky-extra-source.git
$ cd jobberwocky-extra-source
$ docker build . -t avatureexternaljobs
$ docker run -p 8081:8080 
```

## How to Install on Linux:
```bash
$ mkdir jobberwocky
$ cd jobberwocky
$ python -m venv venv
$ pip install -r requirements.txt
$ source venv/bin/activate
$ git clone https://github.com/avatureassessment/jobberwocky-extra-source.git
$ cd jobberwocky-extra-source
$ docker build . -t avatureexternaljobs
$ docker run -p 8081:8080 
```
## How to run the webserver:
```bash
$ cd jobberwocky
$ uvicorn main:app --host 0.0.0.0 --port 8080 --reload
```
## Swagger
http://0.0.0.0:8080/ \
This is the swagger documentation of this set of APIs, you can test the APIs here.

This set of APIs provides a the following endpoints:

## GET:
http://0.0.0.0:8080/searchexternal \
Searchs for jobpostings in the JobberwockyExternalJobs API \
Example result:
```json
[
  {
    "name": "Jr Python Developer",
    "salary": 28000,
    "country": "USA",
    "skills": [
      "Python",
      "OOP"
    ],
    "Origin": "External"
  }
]
```


http://0.0.0.0:8080/searchinternal \
Searchs for jobpostings in the Jobberwocky Internal API 
Example result: 
```json
[
  {
    "name": "Software developer Ssr. Cobol",
    "salary": 100000,
    "country": "Mexico",
    "skills": [
      "Go",
      "microservices"
    ],
    "Origin": "Internal"
  }
]
```

http://0.0.0.0:8080/searchall/ \
Searchs for jobpostings consolidating results from jobberwocky's internal and external APIs. 
Example result:
```json
[
  {
    "name": "Jr Java Developer",
    "salary": 24000,
    "country": "Argentina",
    "skills": [
      "Java",
      "OOP"
    ],
    "Origin": "External"
  },
  {
    "name": "SSr Java Developer",
    "salary": 34000,
    "country": "Argentina",
    "skills": [
      "Java",
      "OOP",
      "Design Patterns"
    ],
    "Origin": "External"
  },
  {
    "name": "Sr Java Developer",
    "salary": 44000,
    "country": "Argentina",
    "skills": [
      "Java",
      "OOP",
      "Design Patterns"
    ],
    "Origin": "External"
  },
  {
    "name": "Jr Java Developer",
    "salary": 24000,
    "country": "Argentina",
    "skills": [
      "Java",
      "OOP"
    ],
    "Origin": "Internal"
  },
  {
    "name": "SSr Java Developer",
    "salary": 34000,
    "country": "Germany",
    "skills": [
      "Java",
      "OOP",
      "Design Patterns"
    ],
    "Origin": "Internal"
  },
  {
    "name": "Sr Java Developer",
    "salary": 44000,
    "country": "Chile",
    "skills": [
      "Java",
      "OOP",
      "Design Patterns"
    ],
    "Origin": "Internal"
  }
]
```

## POST:
http://0.0.0.0:8080/insertjob/ \
Inserts a new jobposting in the jobberwocky's internal dataset

http://0.0.0.0:8080/insertalert/ \
Inserts a subscription to receive email alerts on new jobpostings based on a certain term 

