import random
def RandomSpezSM(NumReqDig):
    listrandom = []
    listSymbol = ["!","@","#","$","%","&","*","/","<",">"]
    for i in range(NumReqDig):
        listrandom.append(random.randint(0, len(listSymbol)-1))
    listrandomSymbol = []
    for j in listrandom:
        listrandomSymbol.append(listSymbol[j])
    return listrandomSymbol
h=int(input())
l=RandomNumbers(h)
