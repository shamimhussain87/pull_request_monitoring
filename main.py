import datetime
from github import Github
import sys

username = os.getenv('USER_NAME')
USER_NAME= username.lower()
total_prs = os.getenv('TOTAL_PRS')
TOTAL_PRS= total_prs.lower()
try:
      total_prs = int(total_prs)
except:
      print("total prs must be integer")
      exit()

date = None
if len(sys.argv)==4:
      date = sys.argv[3]

if username=='':
      print("username cannot be null")
      sys.exit(1)

user_reg_date = ''
if date!=None:
      try:
            year, month, day = map(int, date.split('-'))
            user_reg_date = datetime.date(year, month, day)
            user_reg_date = datetime.datetime.strptime(user_reg_date.__str__(), '%Y-%m-%d')
      except:
            print("not a valid date")
            sys.exit(1)

# First create a Github instance:
# using an access token
g = Github("ghp_hhhAOpby980mhTSamQFsLmLUhRSr0PDF73QwiKi4d")
try:
      g.get_user(username) == True
      # print("user exists")
except:

      print("user does not exits.Please try again....")
      exit()

count = 0
f = open("demofile.txt", "r")
line = f.read()
if user_reg_date=='':
      try:
            user_reg_date = g.get_user(username).created_at
      except:
            print("user doesnot exists or entered wrong username .Please tr again ...")
            sys.exit(1)

# print("Loading ..........................")
def pulls(repo, requests, maxD,
          user_reg_date):  # function parameters refer to global variables which compute time and requests of all repos combined
      # Github Enterprise with custom hostname
      pulls = repo.get_pulls(state="all", sort='created', base='main')  # get all pull requests

      totalRequests = 0  # function param => calculating time difference of this repo only
      maxDate = ""  # function param
      for pr in pulls:
            if pr.created_at>=user_reg_date:
                  if (repo.get_pull(pr.number).user.login == username):
                        totalRequests += 1
                        requests += 1
                        maxDate = repo.get_pull(pr.number).created_at
                  if requests >= int(total_prs):
                        break

      if maxDate == "":  # check if no pulls are made by that specific user or no pulls exists in this specific repo at all
            # print("No pull request in " + repo.name);
            return requests, maxD  # returning tuple

      if maxD != None:  # if function maxDate is greater or equal to the global maxDate -> replace it with new date
            if maxDate >= maxD:
                  maxD = maxDate
      else:
            maxD = maxDate
      return requests, maxD


maxDate = None
totalRequests = 0
for repo in g.get_user().get_repos(sort="ascending"):  # get all repositories
      if line.__contains__(repo.name):
            # print("skipping repo "+repo.name)
            continue

      totalRequests, maxDate = pulls(repo, totalRequests, maxDate,
                                     user_reg_date)  # Get all pull requests based on the repository names and receiving tuples to populate total requests(of all repos) and dates(min,max of all repos)
      if totalRequests >= int(total_prs):
            break

if (totalRequests < int(total_prs)):
      print("User has not made any pull request yet or the pull requests are less than " + total_prs.__str__())
elif (maxDate != None):
      print(username + " made " + totalRequests.__str__() + " pull requests in ", (maxDate - user_reg_date).days, " days")
