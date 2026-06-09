class MinStack:

    def __init__(self):
        self.data = [2147483648]*10000
        self.i = 0
        

    def push(self, val: int) -> None:
        self.data[self.i] = val
        self.i+=1

    def pop(self) -> None:
        self.data[self.i] = 2147483648
        self.i-=1

    def top(self) -> int:
        return self.data[self.i-1]

    def getMin(self) -> int:
        mx = 2147483648
        for i in range(self.i):
            if self.data[i]<mx:
                mx = self.data[i]
        return mx