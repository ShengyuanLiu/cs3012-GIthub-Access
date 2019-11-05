import requests
import json
from github import Github

url = 'https://api.github.com/repos/sebastianbergmann/php-code-coverage'


print("Status:",requests.get(url).status_code)


def getTheContributors():
    curl='https://api.github.com/repos/sebastianbergmann/php-code-coverage/contributors'
    r=requests.get(curl)

    count=0
    while count<len(r.json()):
         theContributors=r.json()[count]['login']
         print(theContributors)
         count+=1
    return theContributors

getTheContributors()

def getTheCommits():
    curl = 'https://api.github.com/repos/sebastianbergmann/php-code-coverage/commits'
    r=requests.get(curl)





