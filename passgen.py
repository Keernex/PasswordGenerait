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
h=int(input())
l=RandomNumbers(h)
