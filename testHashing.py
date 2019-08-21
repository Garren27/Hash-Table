# Using Python3
from HashTable_LinearProbing import HashTable_LinearProbing
from HashTable_DoubleHashing import HashTable_DoubleHashing
from _MapEntry import _MapEntry
import random

# Initialize and set variables to be used later
SIZE = 1000003
hashTableLinear = HashTable_LinearProbing(SIZE)
hashTableDouble = HashTable_DoubleHashing(SIZE)
data = [None] * SIZE

# Create the data for the hash tables by randomly selecting numbers between 1 and 1000000000
# to populate the array
for i in range(0, SIZE):
    key = random.randint(1, 1000000000)
    value = 0
    data[i] = _MapEntry(key, value)

# The different load values to test
load = [0.25, 0.5, 2/3.0, 0.75, 0.8, 0.9, 0.95]
print("Average Probes:")
startIndex = 0

# Loop through each load factor to populate the hash tables and do calculations
for i in range(0, 7):
    print("loadfactor =", load[i])
    endingIndex = int(load[i] * SIZE)

    # Put in the data
    for j in range(startIndex, endingIndex):
        hashTableLinear.put(data[j])
        hashTableDouble.put(data[j])

    # Create array of test data to check successful searches
    testData = [None] * int(0.01 * SIZE)
    for j in range(0, int(0.01 * SIZE)):
        entry = random.randint(0, endingIndex)
        testData[j] = data[entry]

    # Track the number of probes each table takes to find the key
    linearProbeCount = 0
    doubleProbeCount = 0
    for j in range(0, int(0.01 * SIZE)):
        linearProbeCount += hashTableLinear.get(testData[j].getKey())
        doubleProbeCount += hashTableDouble.get(testData[j].getKey())
    print("  Successful Search:")
    print("linear probing:   ", linearProbeCount / (0.01 * SIZE))
    print("double hashing:   ", doubleProbeCount / (0.01 * SIZE))

    # Track the number of probes each table takes to put the next set of keys in
    # and keep track of the new indexes
    startIndex = endingIndex
    endingIndex = startIndex + int(0.01 * SIZE)
    linearProbeCount = 0
    doubleProbeCount = 0
    for j in range(startIndex, endingIndex):
        linearProbeCount += hashTableLinear.put(data[j])
        doubleProbeCount += hashTableDouble.put(data[j])
    print("  Unsuccessful Search:")
    print("linear probing:   ", linearProbeCount / (0.01 * SIZE))
    print("double hashing:   ", doubleProbeCount / (0.01 * SIZE))
    startIndex = endingIndex

