import mmh3
from bitarray import bitarray
import math


class BloomFilter:

    def __init__(self, capacity, error_rate):
        self.capacity = capacity
        self.error_rate = error_rate
        self.bit_size = math.ceil(-capacity * math.log(error_rate) / (math.log(2) ** 2))
        self.hash_counts = math.ceil(self.bit_size / (capacity * math.log(2)))
        self.bit_array = bitarray(self.bit_size)

    def add(self, string):
        for salt in range(self.hash_counts):
            result = mmh3.hash(string, salt) % self.bit_size
            self.bit_array[result] = 1


    def contains(self, string):
        for salt in range(self.hash_counts):
            result = mmh3.hash(string, salt) % self.bit_size
            if self.bit_array[result] == 0:
                return False
        return True


