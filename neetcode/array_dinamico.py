class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arr = capacity * [0]
        self.size = 0


    def get(self, i: int) -> int:
        return self.arr[i]
         

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()

        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:   
        self.size -= 1
        return self.arr[self.size]

    def resize(self) -> None:
        self.capacity *= 2
        novo_array = self.capacity * [0]

        for i in range(0, self.size):
            novo_array[i] = self.arr[i]
        self.arr = novo_array

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity