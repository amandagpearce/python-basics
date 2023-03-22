class Test:
    staticVariable = 0
    instanceVariable = 0

    def __init__(self):
        print('Constructor running')
        self.instanceVariable += 1
        Test.staticVariable += 1


t1 = Test()
print('First Object Created')
print('Instance Variable:', t1.instanceVariable)
print('Static Variable:', t1.staticVariable)

t2 = Test()
print('Second Object Created')
print('Instance Variable:', t2.instanceVariable)
print('Static Variable:', t2.staticVariable)
print('Static variable with class reference', Test.staticVariable)
