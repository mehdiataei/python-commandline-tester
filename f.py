def return_str(string):
    return string

def nothing():
    pass


def add(a,b):
    return a+b

def addList(a):
    sum = 0
    for i in a:
        sum += i

    return sum


def addMixedTypes(a, b):

    sum = 0

    for i in b:
        sum += i

    return sum + a



class Addition(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def update_params(self,a,b):
        self.a = a
        self.b = b
    
    def result(self):
        return (self.a + self.b)
        
