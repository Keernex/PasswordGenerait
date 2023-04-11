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
