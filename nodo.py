class Nodo:
    def __init__(self, data=None, next=None, last=None):
        self.data = data
        self.next = next
        self.last = last

    def set_data(self, data):
        self.data = data

    def set_next(self, next):
        self.next = next

    def set_last(self, last):
        self.last = last

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def get_last(self):
        return self.last
