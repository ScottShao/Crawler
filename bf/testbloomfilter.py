from bf.bloomfilter import BloomFilter
import sys
import math
# file: words2.txt, number of words: 235886, size of bloom filter:413KB, size of all strings:2434KB,
# error rate:0.000402736915289589saved 82.99576953915773% space
num_lines = sum(1 for line in open('words2.txt'))
ERROR_RATE = 0.001
bf = BloomFilter(num_lines, ERROR_RATE)
error = 0
mem_bytes_size = 0
with open('words2.txt', 'r') as file:
    for line in file:
        mem_bytes_size += len(line)
        if line in bf:
            error += 1
        bf.add(line)

print('file: words2.txt, number of words: ' + str(num_lines) + ', size of bloom filter:' + str(math.floor(bf.bit_size / 8 / 1024)) +
      'KB, size of all strings:' + str(math.floor(mem_bytes_size / 1024)) + 'KB, error rate:' + str(error / num_lines) +
      'saved ' + str(100 * (1 - bf.bit_size / 8 / mem_bytes_size)) +'% space')

# file: words1.txt, number of words: 354986, size of bloom filter:623KB, size of all strings:3625KB,
# error rate:0.00037184565025099583saved 82.81621824505096% space
num_lines = sum(1 for line in open('words.txt'))
ERROR_RATE = 0.001
bf = BloomFilter(num_lines, ERROR_RATE)
error = 0
mem_bytes_size = 0
with open('words.txt', 'r') as file:
    for line in file:
        mem_bytes_size += len(line)
        if line in bf:
            error += 1
        bf.add(line)
print('file: words1.txt, number of words: ' + str(num_lines) + ', size of bloom filter:' + str(math.floor(bf.bit_size / 8 / 1024)) +
      'KB, size of all strings:' + str(math.floor(mem_bytes_size/1024)) + 'KB, error rate:' + str(error / num_lines) +
      'saved ' + str(100 * (1 - bf.bit_size / 8 / mem_bytes_size)) +'% space')
