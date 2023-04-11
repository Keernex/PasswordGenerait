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


while True:
    while True:
      try:
        kilkist = int(input("Enter password length: "))
        break
      except ValueError:
        print("Please enter a valid integer.")

    while True:
      number = str.lower(input("Include numbers? (y/n) -> "))
      if number=="y" or number=="+" or number=="yes":
        number=2
        break
      elif number=="n" or number=="-" or number=="no":
        number=1
        break

    while True:
      smolbk = str.lower(input("Include lower letters? (y/n) -> "))
      if smolbk=="y" or smolbk=="+" or smolbk=="yes":
        smolbk=2
        break
      elif smolbk=="n" or smolbk=="-" or smolbk=="no":
        smolbk=1
        break

    while True:
      bigbk = str.lower(input("Include upper letters? (y/n) -> "))
      if bigbk=="y" or bigbk=="+" or bigbk=="yes":
        bigbk=2
        break
      elif bigbk=="n" or bigbk=="-" or bigbk=="no":
        bigbk=1
        break

    while True:
      spezSM = str.lower(input("Include special characters? (y/n) -> "))
      if spezSM=="y" or spezSM=="+" or spezSM=="yes":
        spezSM=2
        break
      elif spezSM=="n" or spezSM=="-" or spezSM=="no":
        spezSM=1
        break
    j=kilkist
    l=[]
    while True:
        kilkist=j
        NSBS=number+smolbk+bigbk+spezSM
        num1=0
        num2=0
        num3=0
        num4=0
        Sm_1=[]
        Sm_2=[]
        Sm_3=[]
        Sm_4=[]

        if number == 2:
            if NSBS>5:
                num1=KL(kilkist)
                kilkist=kilkist-num1
                NSBS=NSBS-1
            else:
                num1=kilkist
            Sm_1=RandomNumbers(num1)

        if smolbk == 2:
            if NSBS>5:
                num2=KL(kilkist)
                kilkist=kilkist-num2
                NSBS=NSBS-1
            else:
                num2=kilkist
            Sm_2=RandomSmolBk(num2)

        if bigbk == 2:
            if NSBS>5:
                num3=KL(kilkist)
                kilkist=kilkist-num3
                NSBS=NSBS-1
            else:
                num3=kilkist
            Sm_3=RandomBigBk(num3)

        if spezSM == 2:
            if NSBS>5:
                num4=KL(kilkist)
                kilkist=kilkist-num4
                NSBS=NSBS-1
            else:
                num4=kilkist
            Sm_4=RandomSpezSM(num4)
        
        Password= Sm_1 + Sm_2 + Sm_3 + Sm_4
        random.shuffle(Password)
        r=""
        for i in Password:
            r=r+str(i)
        print("Previous passwords: ",*l)
        print("Password been generated: ",r)
        print()
        print("Generate password with the same data - 1\nGenerate a password with other data - 2\nEnd - 3")
        while True:
            choice = str.lower(input("Enter 1,2 or 3 -> "))
            if int(choice)==1:
                l.append(r)
                break
            elif int(choice)==2:
                choice=2
                break
            elif int(choice)==3:
                choice=3
                break
        if choice == 2:
            break
        elif choice == 3:
            break
    if choice == 3:
        break
