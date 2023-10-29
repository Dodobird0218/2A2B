import random


# function
def get_random_algorithm()->str:
    while True:
        answer = random.sample(range(10), 4) #Generate a list by randomly selecting four numbers from 0 to 9
        if answer[0] == 0:
            continue
        else:
            break
    final_answer = "".join(map(str, answer)) #Concatenate the list into a string
    return final_answer


def interactive()->str:
    user_ans = input("\033[37mplease enter your answer: ")
    error = "\033[91mwrong input type! please enter again!"
    if (len(user_ans) != 4) or (len(set(user_ans)) != 4):
        print(error)
        return False
    elif str.isdigit(user_ans) == False:
        print(error)
        return False
    elif user_ans[0] == "0":
        print(error)
        return False
    return user_ans


def check(final_ans:str, user_ans:str)->int:
    a = 0
    b = 0
    for i in range(0, 4):
        for j in range(0, 4):
            if final_ans[i] == user_ans[j]:
                if i == j:
                    a = a + 1
                else:
                    b = b + 1
    return a, b


# main
if __name__ == "__main__":
    final_ans = get_random_algorithm()
#    print("ans:", final_ans)
    while True:
        user_ans = interactive()
        if user_ans == False:
            continue
        a, b = check(final_ans, user_ans)
        if a == 4:
            print("you got it!")
            break
        else:
            print(f"{a}A{b}B")


#final version