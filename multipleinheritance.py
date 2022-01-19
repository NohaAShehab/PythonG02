class A:
    pass
    def __init__(self):
        print("Class A constructor called")
        print("---------------------------------------")
        self.name= "Ali"
        self.id= 1


class B:
    def __init__(self):
        print("Class B constructor called")
        print("---------------------------------------")
        self.email= "iti@gmail.com"

class C(A, B):
    def __init__(self):
        print("C constructor called ")
        # super().__init__()  #
        super(C, self).__init__()
        B.__init__(self)



c_obj = C()
print("fjklsdjfkl")