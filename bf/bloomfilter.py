import mmh3
from bitarray import bitarray
import math


class BloomFilter(object):

    def __init__(self, capacity=100, error_rate=0.01):
        if not (0 < error_rate < 1):
            raise ValueError("Error_Rate must be between 0 and 1.")
        if not capacity > 0:
            raise ValueError("Capacity must be > 0")
        self.capacity = capacity
        self.error_rate = error_rate
        self.bit_size = math.ceil(-capacity * math.log(error_rate) / (math.log(2) ** 2))
        self.hash_counts = math.ceil(self.bit_size / (capacity * math.log(2)))
        self.bit_array = bitarray(self.bit_size)
        self.count = 0

    def add(self, string):
        if string in self:
            return False
        if self.count >= self.capacity:
            raise IndexError('Bloom filter has reached its capacity')
        for salt in range(self.hash_counts):
            result = mmh3.hash(string, salt) % self.bit_size
            self.bit_array[result] = 1
        self.count += 1
        return True

    def _contains_(self, string):
        for salt in range(self.hash_counts):
            result = mmh3.hash(string, salt) % self.bit_size
            if self.bit_array[result] == 0:
                return False
        return True

    def __len__(self):
        return self.count

# To do: 1. choose different hash functions according to the bits_size
#        2. write bloom filter to files
#        3. read bloom filter from files
#        4. test I/O operations


