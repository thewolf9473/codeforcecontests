import requests,json
import time
operation=int(input("""To get the rating of a user enter                     : 1
To get the standings of a user in past contests enter : 2
To get the list of upcoming rated contests enter      : 3\n"""))

if(operation == 1):
    handle = input("Enter codeforces handle : ")
    resp = requests.get("https://codeforces.com/api/user.rating?handle={}".format(handle))
    dat = resp.text
    dic = json.loads(dat)
    print("Your current rating is {}".format(dic['result'][-1]['newRating']))

elif(operation == 2):
    handle = input("Enter codeforces handle : ")
    count = int(input("How many past contests do you want to display : "))
    resp = requests.get("https://codeforces.com/api/user.rating?handle={}".format(handle))
    dat = resp.text
    dic = json.loads(dat)
    contests = dic['result']
    contests.reverse()
    
    if(count<len(contests)):
        contests = contests[:count]
    
    print('\n'+'-'*55+'\n')
    for contest in contests:
        print("Contest ID          : {}\nContest Name        : {}\nRank                : {}\nRatings Update Time : {}\nOld Rating          : {}\nNew Rating          : {}".format(contest['contestId'], contest['contestName'], contest['rank'], time.ctime(contest['ratingUpdateTimeSeconds']), contest['oldRating'], contest['newRating']))
        print('\n'+'-'*55+'\n')
elif(operation==3):
    resp = requests.get("https://codeforces.com/api/contest.list?gym=false")
    dat = resp.text
    dic = json.loads(dat)
    contests = dic['result']
    count = 0
    for contest in contests:
        if(contest['phase']=="FINISHED"):
            break
        count+=1
    contests = contests[:count]
    contests.reverse()
    print('\n'+'-'*55+'\n')
    for contest in contests:
        print("Contest ID   : {}\nContest Name : {}\nStart Time   : {}".format(contest['id'], contest['name'], time.ctime(contest['startTimeSeconds'])))
        print('\n'+'-'*55+'\n')


