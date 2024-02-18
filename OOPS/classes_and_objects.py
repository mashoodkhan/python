class myClass:
    print("Please Enter Add , Sub , Mul to do Operation")
    operation = input()
    val1 = int(input())
    val2= int(input())


    def addNum(self, a, b):
        c = a + b
        return c

    def subNum(self, a, b):
        c = a - b
        return c

    def mulNum(self, a, b):
        c = a * b
        return c

    def calculator(self, a, b):
        if self.operation == 'Add':
            return self.addNum(a, b)
        elif self.operation == 'Sub':
            return self.subNum(a, b)
        elif self.operation == 'Mul':
            return self.mulNum(a, b)


calc = myClass()
result = calc.calculator(calc.val1, calc.val2)
print(result)
