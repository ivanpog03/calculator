import os
def clear_console():
    os.system('cls')
def calculating(num1, num2, op):
    if op=="+":
        answer=num1+num2
        print(answer)
        return answer
    elif op=="-":
        answer=num1-num2
        print(answer)
        return answer
    elif op=="*":
        answer=num1*num2
        print(answer)
        return answer
    elif op=="/":
        answer=num1-num2
        print(answer)
        return answer

def co(inin, answer):
    if inin=="y":
        n2=input("Type in the new second number")
        n2=int(n2)
        op=input("Type in the new operation")
        newanswer=calculating(answer, n2, op )
        we=input(f"your answer is: {newanswer}. y to cont f to stop")
        co(we, newanswer)
    elif inin=="f":
        print("GO FUCK YOURSELF YOU SUCKER")
        clear_console()
        print("Welcome to Calculator.")
        firstnum=input("Type in the first number")
        firstnum=int(firstnum)
        secondnum=input("Type in the second number")
        secondnum=int(secondnum)
        operation=input("Type in the operation: +, -, *, /")
        answer=calculating(firstnum, secondnum, operation)
        cont=input((f"ANSWER: {answer}. If you want to continue to work with the answer, press y, else press f"))
        co(cont, answer)


print("Welcome to Calculator.")
firstnum=input("Type in the first number")
firstnum=int(firstnum)
secondnum=input("Type in the second number")
secondnum=int(secondnum)
operation=input("Type in the operation: +, -, *, /")
answer=calculating(firstnum, secondnum, operation)
cont=input((f"ANSWER: {answer}. If you want to continue to work with the answer, press y, else press f"))
co(cont, answer)


