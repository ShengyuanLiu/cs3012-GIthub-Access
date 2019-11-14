import requests
import json
import pygal
from pygal.style import  LightColorizedStyle as LCS, LightStyle as LS
from github import Github
import getpass
import numpy as np


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
                   # print("Contributor:" + str(name)+"  Contribution:"+ str(contributionTime))
                   repo_contributors.append(contributor)
                   repo_contributions.append(contributionTime)
    # returns contributors in a list and his/her contributions in another list

    return repo_contributors,repo_contributions

def getTheContributorsRepo(contributors):
    repo_count=[]
    count=0
    print("Prepare to print the repo number:")
    for index in contributors:
       repoNumber = index.get_repos()
       repoNumbers=len(list(repoNumber))
       # print(repoNumbers)
       if repoNumbers != "None":
          print(index.name+" repository's amount is " +str(repoNumbers))
          repo_count.append(str(repoNumbers))

    # returns the repo amount in the list
    return repo_count



def getReceivedEvents(contributors):
    received_count=[]
    print("Prepare to print the recevied event amounts")
    for index in contributors:
        recevied = index.get_received_events()
        recevieds=len(list(recevied))
        push_event=list(index.get_received_events())
        print(push_event)
            # if push_event[count]['type']=='PushEvent':
            #        push+=1
        # count += 1
        # print(recevieds)
        if recevieds !="None":
            received_count.append(str(recevieds))

    return received_count


def getCommitts(contributors):
    commits=[]
    print("Prepare to print the commits amount of each contributor")
    for index in contributors:
        commit = index.get_commits()
        theCommits=list(commit)
        print(theCommits)

    return commits







def getStars(contributors):
    stars=[]
    print("Prepare to print the User's starred repo's amount")
    for index in contributors:
        star=index.get_starred()
        starAmounts =len(list(star))
        print(starAmounts)
        orgName=list(star)
        # print(orgName)
        stars.append(str(starAmounts))


    return stars










repo=start()
(contributors,contributions) = getTheContributors(repo)
# print the greatest contributors and contributions
print("\nThe contributors who gives the most contributions is " +contributors[0].name+" and his/her contribution time is:"+contributions[0])
repo_count = getTheContributorsRepo(contributors)
# received_count = getReceivedEvents(contributors)
starred_count=getStars(contributors)
# to print each contributor's repository amount
# count=0
# while count<len(repo_count):
#   theRepo=repo_count[count]
#   print("Each contributor's repository amount is "+str(theRepo))
#   count+=1

#get the contributors' code type
# if the result>2 means the user prefer to participate in other people's code development
# if the result<1 means the user prefer to develop his/her own code
# count=0
# while count<len(repo_count):
#     result=int(starred_count[count])/int(repo_count[count])
#     print("The result are "+str(result))
#     count+=1

commits=getCommitts(contributors)