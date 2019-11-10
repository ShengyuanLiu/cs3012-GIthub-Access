import requests
import json
import pygal
from pygal.style import  LightColorizedStyle as LCS, LightStyle as LS
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
                repo_to_use = input("Please put in repo you wish to interrogate\nThe input construction should be (owner_name/repo_name):")
                repo = g.get_repo(repo_to_use)
                error = False
            except:
                print("Incorrect repo (check whether if use wrong owner). Please try again")
        return repo



def getTheContributors(repo):
    repo_contributors = []
    repo_contributions = []
    contributors = repo.get_contributors()
    print("Preparing to print the contributors and each of their contributions:")
    for contributor in contributors:
            name = str(contributor.name)
            contributionTime = str(contributor.contributions)
            if name != "None":
                if contributionTime != "None":
                   print("Contributor:" + str(name)+"  Contribution:"+ str(contributionTime))
                   repo_contributors.append(contributor)
                   repo_contributions.append(contributionTime)
    # returns contributors in a list

    return repo_contributors,repo_contributions

# def getTheFollower():
#




repo=start()
(contributors,contributions) = getTheContributors(repo)
print("\nThe contributors who gives the most contributions is " +contributors[0].name+" and his/her contribution time is:"+contributions[0])

