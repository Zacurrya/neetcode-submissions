class DynamicArray:
    
    def __init__(self, capacity: int):
        self.array = [None] * capacity
        self.size = 0
        self.capacity = capacity

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.set(self.size, n)
        self.size += 1

    def popback(self) -> int:
        i = self.size - 1
        element = self.get(i)
        self.size -= 1
        return element

    def resize(self) -> None:
        self.capacity *= 2 # doubles capacity
        new_array = [None] * self.capacity
        new_array[:self.size] = self.array[:self.size]
        self.array = new_array

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity