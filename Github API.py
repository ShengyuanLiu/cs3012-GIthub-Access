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
    owner = repo.owner
    repo_contributors = []
    repo_contributions = []
    contributors = repo.get_contributors()
    print("Preparing to print the contributors and each of their contributions:")
    for contributor in contributors:
            if(contributor!=owner):
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
          print("His/her repository's amount is " +str(repoNumbers))
          repo_count.append(str(repoNumbers))


    return repo_count





repo=start()
(contributors,contributions) = getTheContributors(repo)
# print the greatest contributors and contributions
print("\nThe contributors who gives the most contributions is " +contributors[0].name+" and his/her contribution time is:"+contributions[0])
repo_count = getTheContributorsRepo(contributors)

# to print each contributor's repository amount
# count=0
# while count<len(repo_count):
#   theRepo=repo_count[count]
#   print("Each contributor's repository amount is "+str(theRepo))
#   count+=1

