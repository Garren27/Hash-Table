# Using Python3
import _MapEntry

# Implements a hash table that uses double hashing for collision handling
class HashTable_DoubleHashing :

    # Initialize with a size and array of that size for the table
    def __init__(self, size):
        self.size = size
        self.hashTable = [None] * self.size

    # Puts a _MapEntry object in the hash table and returns the count of the probes it took to insert it
    def put(self, entry):
        key = entry.getKey()
        # Gets the index to insert a _MapEntry by using the hash function
        index = self.hashMethod(key)
        count = 0  # Track the probe count to return
        # If the first position is available insert there
        if self.hashTable[index] == None or self.hashTable[index].getValue() == "REMOVED":
            self.hashTable[index] = entry
            return count + 1
        else:
            inserted = False
            # Gets the step count to insert a _MapEntry by using the secondary hash function
            stepSize = self.doubleHashMethod(key)
            while inserted != True:
                index += stepSize
                count += 1
                if index >= self.size:
                    index = index - self.size # If we reach the end of the hash table then loop around to the start
                # If the position is available insert there
                if self.hashTable[index] == None or self.hashTable[index].getValue() == "REMOVED":
                    self.hashTable[index] = entry
                    return count

    # Gets the count for how many probes it took to find a key
    def get(self, key):
        # Gets the index to find a key by using the hash function
        index = self.hashMethod(key)
        originalIndex = index
        found = False
        # Gets the step count to insert a _MapEntry by using the secondary hash function
        stepSize = self.doubleHashMethod(key)
        count = 1

        # Loop until we've found the key or it isn't in the table
        while found != True:
            # If we've searched the whole table and the original index was 0 and it wasn't in the table
            if index >= self.size:
                index = index - self.size
                if index == originalIndex:
                    return count
            # If the value is None then no entries with that key are in the table
            if self.hashTable[index] == None:
                return count
            # If the keys match and the value isn't REMOVED than we've found a matching key
            if self.hashTable[index].getKey() == key and self.hashTable[index].getValue() != "REMOVED":
                #return self.hashTable[index].getValue()
                return count

            index += stepSize
            count += 1
            # If we've searched the whole table and it wasn't in the table
            if index == originalIndex:
                return count

    # Removes a _MapEntry by using its key from the hash table
    def remove(self, key):
        # Gets the index to remove a key by using the hash function
        index = self.hashMethod(key)
        originalIndex = index
        found = False
        # Gets the step count to insert a _MapEntry by using the secondary hash function
        stepSize = self.doubleHashMethod(key)

        # Loop until we have found the object or it does not exist
        while found != True:
            # If we've searched the whole table and the original index was 0 and it wasn't in the table exit
            if index >= self.size:
                index = index - self.size
                if index == originalIndex:
                    return None
            # If the value is None then no entries with that key are in the table
            if self.hashTable[index] == None:
                return None
            # If the key is the same as what we were looking for flag it with REMOVED
            if self.hashTable[index].getKey() == key:
                value = self.hashTable[index].getValue()
                self.hashTable[index].setValue("REMOVED")
                return value

            index += stepSize
            # If the index is equal to the original index then we've searched the whole table and its not in it
            if index == originalIndex:
                return None

    # Hash function to map the key to the hash table
    def hashMethod(self, key):
        return abs(hash(key)) % self.size

    # Secondary hash function to find a step count for the next position to place
    # key in the table if there is a collision
    def doubleHashMethod(self, key):
        return 1 + abs(hash(key)) % (self.size - 2)
