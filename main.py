print("hello aldas")
import os
import random
import time 
import inputD
time.sleep(2)
os.system('cls' if os.name == 'nt' else 'clear')

score = 0
win = 0
o = 0
def main(dif):
    global win
    global o 
    global score
    id =0
    dif = int(dif)
    for i in inputD.dif:
        
        if i == dif :
            o+=1
            print(inputD.question[id])
            print("""введите ответ""")
            swap = int(random.uniform(1 ,4))
            if swap == 1 : 
                print("   1 :"+inputD.answer[id][0]) 
            elif swap == 2:
                print("   1 :"+inputD.answer[id][1]) 
            else: 
                print("   1 :"+inputD.answer[id][2]) 

            if swap == 2 : 
                print("   2 :"+ inputD.answer[id][0]) 
            elif swap == 1: 
                print("   2 :"+inputD.answer[id][2] )     
            else : print("   2 :"+inputD.answer[id][1] ) 

            if swap == 3 : 
                print("   3 :"+inputD.answer[id][0] ) 
            elif swap == 2 :
                print("   3 :"+inputD.answer[id][2])
            elif swap == 1: print("   3 :"+inputD.answer[id][1])
            userI = input()
            if userI == "сменить":
                score -=dif *8
                break
            if userI == str(swap):
                print("!!!молодец хорошая кися, ты победил!!!")   
                score += dif * 10
                win += 1 
            else: 
                score -= dif * 10
                print("ты обосрался")  
            time.sleep(2)  
            os.system('cls' if os.name == 'nt' else 'clear')
            

        id +=1 




while 1 :
    score = 0
    win = 0
    userI = input("""выберите сложность
            1 lite
            2 midle
            3 nerd 
            
    """)
    os.system('cls' if os.name == 'nt' else 'clear')

    if str(userI) ==str(1 )or str(userI) ==str(2) or str(userI) ==str(3):
        main(userI)
        print("you score = " + str(score))
        print("ты ответил правильно на " + str(win) + "из" + str(o))
    else : print(" ты рукажоп) введи ")
    input("press enter to contine")
    os.system('cls' if os.name == 'nt' else 'clear')


