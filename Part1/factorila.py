
class Factorial:
    def __init__(self, n):
        self.n = n
     
    def compute(self):
        if self.n == 0:
            return 1
        else:
            return self.n * Factorial(self.n - 1).compute()
   
