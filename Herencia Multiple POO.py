class A():
    def __init__(self):
        print("Soy la clase A")

    def a(self):
        print("Soy el metodo a")

class B():
    def __init__(self):
        print("Soy la clase B")

    def b(self):
        print("Soy el metodo b")

class C(B,A):
    def c(self):
        print("Soy la clase C")
        
