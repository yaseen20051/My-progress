


def check_answer(answers, co_answers, counter):
     if answers[counter] == co_answers[counter]:
         print("Correct!! :)")
     else:
        print("False!! :(")


def result_fn(answers, co_answers, counter, result):
    if counter == 4:
        print("Your answers   :",end="")
        for i in range(0,4):
            print(answers[i]+" ",end="")
        print("\ncorrect answers:", end="")
        for i in range(0,4):
            print(co_answers[i]+" ",end="")
        return result
    if answers[counter] == co_answers[counter]:
        result = result + 3
        return result
    else:
        return result


def Quiz():
    print("Hi!! :)")
    ready=str(input("Ready for the Quiz ???!!! (Yes or No)").capitalize())
    if ready=="Yes":
      questions = ["200+298?", "100+138?", "15*22?", "15/3?"]
      counter = 0
      result = 0
      answers = [["A.498", "B.489", "C.300", "D.499"], ["A.140", "B.238", "C.138", "D.235"],
                 ["A.310", "B.210", "C.330", "D.350"], ["A.2", "B.3", "C.15", "D.5"]]
      co_answers = ["A", 'B', "C", "D"]
      player_answers = ['', '', '', '']
      for i in questions:
          print(i)
          for x in answers[counter]:
              print(x + "  ", end="")
          while player_answers[counter] not in co_answers:
              player_answers[counter] = str(input("\nplease choose from(A,B,C,D)\nChoose the correct answer : ")).upper()
          check_answer(player_answers, co_answers, counter)
          result = result_fn(player_answers, co_answers, counter, result)
          counter += 1
          print("\n----------------------------")

      print("\nQuiz  done :) \nYou got " + str(result_fn(player_answers, co_answers, counter, result)) + " out of 12")

    else:
        print("it's okay take your time :)")