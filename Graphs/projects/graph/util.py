
# Note: This Queue class is sub-optimal. Why?
# dequeue is popping an item from the front of the array, which we means we need to shift everything over before we find and pop item - o(n). if we know our n's are going to be big then we could refactor to use a LL or python built-in deck (double ended queue). since our n's are small this is ok.


class Queue():  # FIFO
    def __init__(self):
        self.queue = []  # efficient if we declare size of an array upfront

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            # from front of an array we need to shift everything over so 0(n)
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)

    def __repr__(self):
        return {'Queue': self.queue}

    def __str__(self):
        return str(self.queue)


class Stack():  # LIFO
    def __init__(self):
        self.stack = []  # efficient if we declare size of an array upfront

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()  # from back of an array no shifts 0(1)
        else:
            return None

    def size(self):
        return len(self.stack)
