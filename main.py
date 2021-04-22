print("hello aldas")
import os
import random
import time 
import inputD
time.sleep(2)
os.system('cls' if os.name == 'nt' else 'clear')

userI = input("""выберите сложность
         1 lite
         2 midle
         3 herd """)

def main():
    id =0
    for i in inputD.dif:
        id +=1 
        if i == 1 :
            print(inputD.question[id])


def what(dif):
    if dif == 1:
        v = int(random.uniform(1,99))
        end = int(random.uniform(1,359))
        print("x + "+str(v)+" = "+str(end))
        while 1 :
            samp = int(random.uniform(1 ,3))
            print(""" варианты ответа""")
            if samp == 1 : 
                print("   1 +"+str(end) ) 
            else: 
                print("   1 :"+str(end + int(random.uniform(1, 35)))) 
            
            if samp == 2 : 
                print("   2 +"+str(end) ) 
            else: 
                print("   2 "+str(end + int(random.uniform(1, 25))) ) 

            if samp == 3 : 
                print("   3 +"+str(end) ) 
            else: print("   3 "+str(end + int(random.uniform(1, 50))) ) 
            
            
            userI = input("выберите ответ")
            
            if str(samp) == userI:
                print("молодец хорошая кися, ты победил")
                break
            elif samp == 1 or samp == 2 or samp == 3:
                print("ты проигрял")
                break
            else : print(" введи 1 или 2 или 3")








main()
#for i in range(0, 4):
#        
#    if userI == "1" :
#        print("ти пидор")
#        what(1)
#    elif userI == "2":
#        print ("ну вроде не дурак")
#    elif userI == "3": 
#        print("теперь ты НАСТОЯЩИЙ МУЖИК")
#    else : print("введите значение от 1 до 3")
#
