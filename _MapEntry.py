# USING Python3
class _MapEntry:
    # Entry constructor consisting of a key and value
    def __init__(self, key, value):
        self.key = key
        self.value = value

    # Get the entry key value
    def getKey(self):
        return self.key

    # Set the entry key value
    def setKey(self, value):
        self.key = value

    # Get the entry key value
    def getValue(self):
        return self.value

    # Set the entry key value
    def setValue(self, value):
        self.value = value