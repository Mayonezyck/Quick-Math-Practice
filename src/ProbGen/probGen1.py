import random
class probGen1():
    def __init__(self, n, difficulty=0):
        self.n = n
        self.difficulty = difficulty
        operation = ['+', '-', '*'] #This difficulty doesn't have division
        print(difficulty)
        self.operation = operation[0:difficulty+1]
        print(self.operation)
    
    def _generateQuestions(self):
        Questions = {}
        for _ in range(self.n):
            num1 = random.randint(1,9)
            num2 = random.randint(1,9)
            op = random.randint(0,self.difficulty)
            operation = self.operation[op]
            match operation:
                case '+':
                    key = str(num1) + ' + ' + str(num2)
                    val = num1 + num2
                case '-':
                    if not num1 > num2:
                        temp = num2
                        num2 = num1
                        num1 = temp
                    key = str(num1) + ' - ' + str(num2)
                    val = num1 - num2
                case '*':
                    key = str(num1) + ' * ' + str(num2)
                    val = num1 * num2
            Questions[key] = val
        return Questions

                
    def _getOperation(self):
        return self.operation
    
