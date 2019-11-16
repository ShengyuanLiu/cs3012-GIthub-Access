import requests
import json
import re
from github import Github
import getpass
import numpy as np
import io
import csv

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



def getReceivedIssueEvents(contributors):
    received_count=[]
    issue_count=[]
    print("Prepare to print the recevied issue event amounts")
    for index in contributors:
        recevied = index.get_received_events()
        recevieds=len(list(recevied))
        # print(str(recevieds))
        received_count.append(recevieds)
        push_event=list(index.get_received_events())
        push_event=str(push_event)
        # print(push_event)
        theIssue=0
        if push_event!=[]:
              push_event_str="".join(push_event)
              # print(push_event_str)
              pattern=re.compile(r'IssuesEvent')
              result=pattern.findall(push_event_str)
              theIssue=len(result)
              print(theIssue)
              issue_count.append(str(theIssue))

        elif push_event==[]:
               # print(push_event_str)
               theIssue=0
               print(theIssue)
               issue_count.append(str(theIssue))


    return received_count,issue_count

def getReceivedWatchEvents(contributors):
    received_count=[]
    watch_count=[]
    print("Prepare to print the recevied watch event amounts")
    for index in contributors:
        recevied = index.get_received_events()
        recevieds=len(list(recevied))
        # print(str(recevieds))
        received_count.append(recevieds)
        push_event=list(index.get_received_events())
        push_event=str(push_event)
        # print(push_event)
        theIssue=0
        if push_event!=[]:
              push_event_str="".join(push_event)
              # print(push_event_str)
              pattern=re.compile(r'WatchEvent')
              result=pattern.findall(push_event_str)
              theIssue=len(result)
              print(theIssue)
              watch_count.append(str(theIssue))

        elif push_event==[]:
               # print(push_event_str)
               theIssue=0
               print(theIssue)
               watch_count.append(str(theIssue))


    return received_count,watch_count


def getStars(contributors):
    stars=[]
    print("Prepare to print the User's starred repo's amount")
    for index in contributors:
        star=index.get_starred()
        starAmounts =len(list(star))
        print(starAmounts)
        # orgName=list(star)
        # print(orgName)
        stars.append(str(starAmounts))


    return stars


def getCommits(repo):
    commits=[]
    print("Prepare to print the repo commits")
    theCommits=repo.get_commits()
    listCommits=list(theCommits)
    theLen=len(listCommits)
    print(listCommits)

    return commits






repo=start()
(contributors,contributions) = getTheContributors(repo)
# print the greatest contributors and contributions
print("\nThe contributors who gives the most contributions is " +contributors[0].name+" and his/her contribution time is:"+contributions[0])
# repo_count = getTheContributorsRepo(contributors)
(received_count,issue_count) = getReceivedIssueEvents(contributors)
# starred_count=getStars(contributors)
(received_count,watch_count) = getReceivedWatchEvents(contributors)
# commits_count=getCommits(repo)



def add_dict(d1,d2):
    result = d1.copy()
    result.update(d2)
    return result


#to loads to str

count=0
name=""
result1=0
result2=0
issues_count=""
watchs_count=""
total_event=""
wq=""
ra=""
theData=""
listData=[]
while count<len(contributors):
      name=contributors[count].name
      print(name)
      issues_count=issue_count[count]
      print(issues_count)
      watchs_count=watch_count[count]
      print(watchs_count)
      total_event=str(received_count[count])
      print(total_event)
      result1=int(issue_count[count])/int(received_count[count])
      if int(received_count[count])==0:
          result1=None

      wq=str(result1)
      print(wq)

      result2 = int(watch_count[count]) / int(received_count[count])
      if int(received_count[count]) == 0:
          result2 = None

      ra=str(result2)
      print(ra)
      theData={
          "username":name,
          "Issues Event":issues_count,
          "Watch Event":watchs_count,
          "Total Received":total_event,
          "Work quality":wq,
          "Repo authority":ra
      }
      data=dict(theData)
      jsonData = json.dumps(data)
      listData.append(data)
      # print(data)
      count+=1
      print(jsonData)

with open('data.json', 'w')as f:
    f.write(json.dumps(listData))


#change json file to csv

file=csv.writer(open("data.csv","w",newline=''))
file.writerow(["username","Issues_Event","Watch_Event","Total_Received","Work_quality","Repo_authority"])
x=listData
for x in x:
    file.writerow([x["username"],
                x["Issues Event"],
                x["Watch Event"],
                x["Total Received"],
                x["Work quality"],
                x["Repo authority"]])


# to print each contributor's repository amount
# count1=0
# while count1<len(repo_count):
#   theRepo=repo_count[count1]
#   print("Each contributor's repository amount is "+str(theRepo))
#   count1+=1


#get the contributors' code type
# if the result>2 means the user prefer to participate in other people's code development
# if the result<1 means the user prefer to develop his/her own code
# count2=0
# while count2<len(repo_count):
#     result=int(starred_count[count2])/int(repo_count[count2])
#     print("The result are: "+str(result))
#     count2+=1


#get the contributors' work quality within the last 90 days
# if result>0.2 means the contributor's work quality is not very good
# if 0<result<0.05 means the contributor has a great code ability
# if result=0 should check the user's event excalty
# count3=0
# while count3<len(received1_count):
#       result=int(issue_count[count3])/int(received1_count[count3])
#       print("The contributors' work quality result is: "+str(result))
#       count3+=1


#get the contributors' work quality within the last 90 days
# if result>0.2 means the contributor's work quality is not very good
# if 0<result<0.05 means the contributor has a great code ability
# if result=0 should check the user's event excalty
# count4=0
# while count4<len(received1_count):
#       result=int(watch_count[count4])/int(received2_count[count4])
#       print("The contributors' repo authority result is: "+str(result))
#       count4+=1