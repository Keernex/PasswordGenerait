import random

def RandomNumbers(NumReqDig):
    listrandom = []
    listSymbol = [9,8,7,6,5,4,3,2,1,0]
    for i in range(NumReqDig):
        listrandom.append(random.randint(0, len(listSymbol)-1))
    listrandomSymbol = []
    for j in listrandom:
        listrandomSymbol.append(listSymbol[j])
    return listrandomSymbol

def RandomSmolBk(NumReqDig):
    listrandom = []
    listSymbol = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
    for i in range(NumReqDig):
        listrandom.append(random.randint(0, len(listSymbol)-1))
    listrandomSymbol = []
    for j in listrandom:
        listrandomSymbol.append(listSymbol[j])
    return listrandomSymbol

def RandomBigBk(NumReqDig):
    listrandom = []
    listSymbol = ["Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"]
    for i in range(NumReqDig):
        listrandom.append(random.randint(0, len(listSymbol)-1))
    listrandomSymbol = []
    for j in listrandom:
        listrandomSymbol.append(listSymbol[j])
    return listrandomSymbol

def RandomSpezSM(NumReqDig):
    listrandom = []
    listSymbol = ["!","@","#","$","%","&","*","/","<",">"]
    for i in range(NumReqDig):
        listrandom.append(random.randint(0, len(listSymbol)-1))
    listrandomSymbol = []
    for j in listrandom:
        listrandomSymbol.append(listSymbol[j])
    return listrandomSymbol

def KL(kilkist):
    l=random.randint(0, kilkist)
    return l

#Введена кількість символів
kilkist=int(input())
#Введені да или нет
num1=0
num2=0
num3=0
num4=0
namber=2
smolbk=2
bigbk=2
spezSM=2
NSBS=namber+smolbk+bigbk+spezSM
#Числа
if namber == 2:
    if NSBS>5:
        num1=KL(kilkist)
        kilkist=kilkist-num1
        NSBS=NSBS-1
    else:
        num1=kilkist
    Sm_1=RandomNumbers(num1)
    print(len(Sm_1))

#Маленькіє букви
if smolbk == 2:
    if NSBS>5:
        num2=KL(kilkist)
        kilkist=kilkist-num2
        NSBS=NSBS-1
    else:
        num2=kilkist
    Sm_2=RandomSmolBk(num2)
    print(len(Sm_2))

#Большие букви
if bigbk == 2:
    if NSBS>5:
        num3=KL(kilkist)
        kilkist=kilkist-num3
        NSBS=NSBS-1
    else:
        num3=kilkist
    Sm_3=RandomBigBk(num3)
    print(len(Sm_3))

#Спец Символи
if spezSM == 2:
    if NSBS>5:
        num4=KL(kilkist)
        kilkist=kilkist-num4
        NSBS=NSBS-1
    else:
        num4=kilkist
    Sm_4=RandomSpezSM(num4)
    print(len(Sm_4))
#воно просто міняє місцями вже згенеровані символи
l=[]
while True:
    Password= Sm_1 + Sm_2 + Sm_3 + Sm_4
    random.shuffle(Password)
    
    print("Бівшие паролі: ",*l)
    r=""
    for i in Password:
        r=r+str(i)
    print("Щойно згенерований: ",r)
    a=input("Эщо Y/N:")
    if a=="Y":
        l.append(r)
        r=""
    else:
        break
