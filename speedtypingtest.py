import random
import time

alfabetet = 'abcdefghijklmnopqrstuvwxyz'

print('Welcome to the speed typing test')
print('Today we will be testing your typing speed')
def lagOrd():
    ran = random.randint(10, 20)
    ord = ''
    for i in range(ran):
        ran2 = random.randint(0, len(alfabetet)-1)
        ord += alfabetet[ran2]
    return ord
ord = lagOrd()
print(ord)
print('Lets see how fast you can type ', ord)
def stoppTest(t0):
    t1 = time.time()
    t = t1-t0
    return t
def startTest():
    t0 = time.time()
    print('Write word under here: ')
    ordet = str(input())
    if ordet == ord:
        t = stoppTest(t0)
    else:
        print('Start over again')
        klar()
    return t
def klar():
    klar = str(input('Ready? Press enter'))
    if klar == '':
        return startTest()
tid = klar()
print('Your time: ', tid)
