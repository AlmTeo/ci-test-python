# SRE Prep - GitHub Actions Health Check Project

This is a simple CI/CD pipeline project realised with GitHub Actions.
Scope of the project is experimenting with Site Reliability Engineer (SRE) actions:

- automatic execution of a Python script on every 'git push'
- checking the functionality of an external web service (health check)
- saving the result in a .json file
- automatic validation of the content
- testing with 'unittest'
- saving the file as a CI artifact
- failing the pipeline in specific cases
