class strings(object):
    def __init__(self,value):
        self.value = value
        self.len=len(value)
    def __add__(self,other):
        return strings(self.value+other.value)
c1=strings('hello')
c2=strings(' world')
print((c1+c2).value)
