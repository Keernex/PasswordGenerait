import random
def RandomSmolBk(NumReqDig):
    listrandom = []
    listSymbol = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
    for i in range(NumReqDig):
        listrandom.append(random.randint(0, len(listSymbol)-1))
    listrandomSymbol = []
    for j in listrandom:
        listrandomSymbol.append(listSymbol[j])
    return listrandomSymbol
h=int(input())
l=RandomNumbers(h)
