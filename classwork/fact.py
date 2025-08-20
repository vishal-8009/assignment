class Factorial:
    def __init__(self, num):
        self.num = num

    def get_fact(self):
        if self.num < 0:
            return "Factorial is not defined for negative numbers"
        return self._get_fact(self.num)

    def _get_fact(self, n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * self._get_fact(n - 1)

n = int(input("Enter a number to calculate its factorial: "))
fact_obj = Factorial(n)
print(fact_obj.get_fact())