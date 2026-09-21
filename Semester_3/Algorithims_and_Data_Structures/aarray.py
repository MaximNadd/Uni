class Array:
    def __init__(self):
        self.data = []

    def add(self, value):
        self.data.append(value)

    def remove(self, value):
        if value not in self.data:
            raise ValueError(f"{value!r} not in array")
        self.data.remove(value)

    def print(self):
        print(self.data)