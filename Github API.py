import requests
import json
from github import Github
import getpass

def start():
        access = False
        while (not access):
            username = input("Please put in your username: ")
            password = getpass.getpass("Please input your password: ")
            try:
                g = Github(username, password)
                access = True
            except:
                print("Incorrect details try again")

        error = True
        while (error):
            try:
                repo_to_use = input("Please put in the git repo you wish to interrogate: ")
                repo = g.get_repo(repo_to_use)
                error = False
            except:
                print("Incorrect repo please try again")
        return repo



def getTheContributors(repo):
    repo_contributors = []
    contributors = repo.get_contributors()
    print("Preparing to print the contributors and each of their contributions:")
    for contributor in contributors:
            name = str(contributor.name)
            contributionTime = str(contributor.contributions)
            if name != "None":
                if contributionTime != "None":
                   print("Contributor:" + str(name)+"  Contribution:"+ str(contributionTime))
                   repo_contributors.append(contributor)
                   repo_contributors.append(int(contributionTime))
    # returns contributors in a list

    return repo_contributors






repo=start()
contributors = getTheContributors(repo)
print(contributors)

