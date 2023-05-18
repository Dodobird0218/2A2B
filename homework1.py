import random

#function
def get_random_algorithm():
     while True:
          final_answers = random.sample(range(10), 4)
          if final_answers[0] == 0:
               continue
          else:
               break
     final_answer = ''.join(map(str, final_answers))
     return final_answer

def interactive():
     user_ans = input("\033[37mplease enter your answer: ")
     if (len(user_ans) != 4) or (len(set(user_ans)) != 4):
          print('\033[91mwrong input type! please enter again!')
          return False
     elif str.isdigit(user_ans) == False:
          print('\033[91mwrong input type! please enter again!')
          return False
     elif user_ans[0] == '0':
          print('\033[91mwrong input type! please enter again!')
          return False
     return user_ans

def check(final_ans, user_ans):
     a = 0
     b = 0
     for i in range(0,4):
          for j in range(0,4):
               if final_ans[i] == user_ans[j]:
                    if i == j:
                         a = a + 1
                    else:
                         b = b + 1
     return a, b

#main
if __name__ == '__main__':
     ans = get_random_algorithm()
     print('ans:', ans)
     while True:
          user_ans = interactive()
          if user_ans == False:
               continue
          a, b = check(ans, user_ans)
          if a == 4:
               print('you got it!')
               break
          else:
               print(f'{a}A{b}B')

#6th commit