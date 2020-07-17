class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * self.capacity
        self.pointer = 0

    def append(self, item):
        if self.pointer == self.capacity:
            self.pointer = 0
        self.storage[self.pointer] = item
        self.pointer += 1

    def get(self):
        return [item for item in self.storage if item is not None]
