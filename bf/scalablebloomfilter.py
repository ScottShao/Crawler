from bf.bloomfilter import  BloomFilter


class ScalableBloomFilter(object):
    SMALL_SET_GROWTH = 2
    LARGE_SET_GROWTH = 4

    def __init__(self, initial_capacity=100, error_rate=0.001, mode=SMALL_SET_GROWTH):
        if error_rate <= 0 or error_rate > 1
            raise ValueError("Error_Rate must be a decimal less than 0.")
        self.capacity = initial_capacity
        self.error_rate = error_rate
        self.mode = mode
        self.filters = []

    def __len__(self):
        return sum(f.count for f in self.filters)