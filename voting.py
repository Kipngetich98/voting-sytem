# Task to register leader name who want to participate in election
leader = []
for i in range(1, 6):
    leader_name = input("Enter your leader name :")
    leader.append(leader_name)
    n = len(leader)
    if n < 5 :
        print("You have been successfully registered")
    else :
        print("Maximum candidate have been enrolled")

# Task to register candidate who want to caste their vote   
voter = []
number = int(input("Enter total number of voters who wants to cast their vote :"))
for i in range(1,number + 1):
    voter_id = int(input("Enter voter id number :"))
    voter.append(voter_id)

while True :
    if voter ==[]:
        print("Voting session is over")
        max = leader[0]
        if leader[1] > max:
            max = leader[1]
            percent = (leader[1]/len(voter))*100
            print(leader[1],"has won","with",percent,"% votes")
            break
        elif leader[2] > max:
            max = leader[2]
            percent = (leader[2]/len(voter))*100
            print(leader[2],"has won","with",percent,"% votes")
            break
        elif leader[3] > max:
            max = leader[3]
            percent = (leader[3]/len(voter))*100
            print(leader[3],"has won","with",percent,"% votes")
            break
        elif leader[5] > max:
            max = leader[5]
            percent = (leader[5]/len(voter))*100
            print(leader[4],"has won","with",percent,"% votes")
            break
        else :
            percent = (leader[0]/len(voter))*100
            print(leader[0],"has won","with",percent,"% votes")
            break
         
         
    else :    
         voter_id = int(input("Enter your voter-id no :"))
         if voter_id in voter:
            print("You are a voter ")
            voter.remove(voter_id)
            print("========================================================\n")
            print("Here are the list of leader name :")
            print(" 1.leader-1 : ",leader[0],
                  "\n 2.leader-2 :",leader[1],
                  "\n 3.leader-3 :",leader[2], 
                  "\n 4.leader-4 :",leader[3],
                  "\n 5.leader-5 :",leader[4])
             
            vote = int(input("Cast your vote for leader 1 or leader2 or leader3 or leader4 or leader5  :\n"
             " Write only sr. no of leader(like 1 or 2 ) :\n"))
            print("===========================================================\n")
            if vote == 1:
               leader[0]+=1
               print("Thank you for casting your vote ")
            elif vote == 2:
               leader[1]+=1
               print("Thank you for casting your vote")
            elif vote == 3:
               leader[2]+=1
               print("Thank you for casting your vote")
            elif vote == 4:
               leader[3]+=1
               print("Thank you for casting your vote")
            elif vote == 5:
               leader[4]+=1
               print("Thank you for casting your vote")
            else :
                print("Leader is not found \n PLease enter correct leader number")
         
         
         else :
                
               print("You have already voted or invalid voter id  ")