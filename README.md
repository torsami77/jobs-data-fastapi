  

## Deliverables

  

Your submission should include the following components:
  

## Mock Data: [Mock Data](https://gitlab.com/textkernel-pub/jobfeed/assignments/jobs-data-assignment-samson-samuel/-/blob/main/api/src/database/seeds.py?ref_type=heads).

  

## Deployment Instructions:

### Prerequisite for local testing

- Docker

- Python3

- Pip3

- Make
- Environment Variables https://github.com/torsami77/jobs-data-fastapi/edit/main/env_sample?ref_type=heads

  

### Scripts: see Makefile in root for more details

- Run API test: ```Make test-api``` (Migrations included in docker)

- Run Migrations ```make migrations-up```

- Run API in Development Mode: ```make run-api-local``` (run migrations first)

- Swagger: http://127.0.0.1:8000/api/v1/docs

- Run instance of api container ```make build-run-api```(run migrations first)

- Build and Run UI in Docker ```make build-run-ui```

- UI: Route
Index/sign in: http://127.0.0.1:3000/
Signup (Customer): http://localhost:3000/sign-up/
Signin (Employee): http://localhost:3000/sign-up/employee
Userpage: http://localhost:3000/userpage

## Security Considerations:
### Some security improvements are 

- Defined Cross origin permissions

- Remove all hard coded env variables

- Implement application, package and security scans

- implement docker image security scan

  

## Additional Insights:

### There's alot of room for improvement with this project and few are listed below

- Complete the Front-end implementation  and test cases
- Add unit test to API and more Integration cases
- Add detail logging across API
- Fix CI/CD failures
- Implements GitOps for Deployment
