def b():
    print("I am function ")



def abc():
    x = "israa"
    def innerfun():
        global x
        x = "test"
        print(x)
    innerfun()

abc()
print(x)