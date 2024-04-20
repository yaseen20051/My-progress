import random
def game():
 choices=["Rock","Paper","Scissor"]
 choice=["r","p","s"]
 player_again="yes"
 for x in range (1000000):
  if player_again=="yes":
   player_result=0
   computer_result=0
   Player=None
   print("Choose (ROCK , PAPER , SCISSOR)")
   for i in range(1000):
     if (computer_result == 5 or player_result == 5):
       break
     try:
          while Player not in choice:
             Player= str(input("Player:")).lower()
          Computer = random.choice(choices)
          print("Computer:" + Computer)
          if ((Player == "r"  and Computer == 'Scissor') or (Player =="s" and Computer == "Paper") or (Player =="p" and Computer == "Rock")):
             print("Player won! :)")
             player_result+=1
          elif ((Player == "r" and Computer == 'Paper') or (Player == "s" and Computer == "Rock") or (Player == "p" and Computer == "Scissor")):
             print("Computer won ! :(")
             computer_result+=1
          else :
             print("Draw! :)")
     except ValueError as e:
         print(e)
     finally:
         print("Player\tComputer\n{}\t\t\t{}".format(player_result, computer_result))
         Player=None
   if player_result>computer_result :
     print("Player won ;) \nFinal Result :\nPlayer\tComputer\n{}\t\t\t{}".format(player_result,computer_result))
   if player_result<computer_result :
     print("Computer won :( \nFinal Result :\nPlayer\tComputer\n{}\t\t\t{}".format(player_result,computer_result))
   else :
     print("Computer Draw :( \nFinal Result :\nPlayer\tComputer\n{}\t\t\t{}".format(player_result,computer_result))
   player_again=input("Do you want to play again?!!! (yes or no)").lower()