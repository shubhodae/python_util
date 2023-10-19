
class Test:
    i = 10

    def __str__(self):
        return str(self.i)

    def __add__(self, val):
        t = Test()
        t.i = self.i * val
        return t
    
    def __iadd__(self, val):
        self.i = self.i * val
        return self
    

k = Test()
print(k)
print(type(k))
print(id(k))
k = k + 10
print(k)
print(type(k))
print(id(k))
k += 10
print(k)
print(type(k))
print(id(k))