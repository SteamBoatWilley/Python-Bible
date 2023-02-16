a = 250

def f1():
    global a
    a = 100 #global
    print(a)

def f2():
    a = 50 #local
    print(a)

f1()
f2()
print(a) #overridden the global 250 value in f1 with the "global" key word

# Two types of Scope - Global & Local
#Python functions create local scopes
#Loops and if statements do not 