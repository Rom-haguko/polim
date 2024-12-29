class Father:
    def __init__(self, mood='neutral'):
        self.mood = mood

    def greet(self):
        return 'Hello!'

    def be_strict(self):
        self.mood = 'strict'

class Mother:
    def __init__(self, mood='neutral'):
        self.mood = mood

    def greet(self):
        return 'Hi, honey!'

    def be_kind(self):
        self.mood = 'kind'

class Daughter(Mother, Father):
    pass

class Son(Father, Mother):
    pass

px1 = Daughter()
print(px1.greet())
px1.be_strict()
print(px1.mood)
px1.be_kind()
print(px1.mood)

px2 = Son()
print(px2.greet())
px2.be_kind()
print(px2.mood)
px2.be_strict()
print(px2.mood)
