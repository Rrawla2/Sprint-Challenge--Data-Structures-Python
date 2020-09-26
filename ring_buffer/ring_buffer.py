class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.ring_buffer = []
        self.current_index = 0

    def append(self, item):
        # if the list is not full capacity, append new item to the end
        if len(self.ring_buffer) < self.capacity:
            self.ring_buffer.append(item)

        # else the list is full capacity, remove the oldest and insert new item in it's place
        else:
            self.ring_buffer[self.current_index] = item
            self.current_index += 1

        if self.current_index == self.capacity:
            self.current_index = 0

    def get(self):
        # return the list
        return self.ring_buffer
