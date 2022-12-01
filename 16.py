import sys
from typing import List

day = __file__.split('.')[0]
import copy
import math


class LiteralPacket:
    def __init__(self, version, type_id, value):
        self.version = version
        self.type_id = type_id
        self.value = value

    @property
    def version_sum(self):
        return self.version

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"<LiteralPacket v{self.version}: {self.value}>"

class OperationPacket:
    def __init__(self, version, type_id, packets):
        self.version = version
        self.type_id = type_id
        self.packets = packets

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"<OperationPacket v{self.version}, {self.type}: {self.packets}>"

    @property
    def version_sum(self):
        return self.version + sum(x.version_sum for x in self.packets)

    @property
    def type(self):
        return {
            0: 'sum',
            1: 'product',
            2: 'min',
            3: 'max',
            5: 'gt',
            6: 'lt',
            7: 'eq',
        }[self.type_id]

    @property
    def value(self):
        if self.type_id == 0:
            return sum(x.value for x in self.packets)
        elif self.type_id == 1:
            if len(self.packets) == 1:
                return self.packets[0].value
            else:
                product = 1
                for x in self.packets:
                    product *= x.value
                return product
        elif self.type_id == 2:
            return min(x.value for x in self.packets)
        elif self.type_id == 3:
            return max(x.value for x in self.packets)
        elif self.type_id == 5:
            return 1 if self.packets[0].value > self.packets[1].value else 0
        elif self.type_id == 6:
            return 1 if self.packets[0].value < self.packets[1].value else 0
        elif self.type_id == 7:
            return 1 if self.packets[0].value == self.packets[1].value else 0

def generate_packet(bits):
    ret = None

    # Header
    version = int(bits[:3], 2)
    type_id = int(bits[3:6], 2)
    bits = bits[6:]

    if type_id == 4:
        payload = ''
        last_nibble = False
        while not last_nibble:
            nibble = bits[:5]
            last_nibble = nibble[0] == '0'
            payload += nibble[1:]
            bits = bits[5:]
        ret = LiteralPacket(version, type_id, int(payload, 2))
    else:
        size_mode = bits[0]
        packets = []
        if size_mode == '0':  # Bit Length
            size = int(bits[1:16], 2)
            sub_bits = bits[16:16+size]
            while sub_bits:
                packet, sub_bits = generate_packet(sub_bits)
                packets.append(packet)
            bits = bits[16+size:]
        else:  # Packet Count
            count = int(bits[1:12], 2)
            bits = bits[12:]
            while len(packets) < count:
                packet, bits = generate_packet(bits)
                packets.append(packet)
        ret = OperationPacket(version, type_id, packets)

    return ret, bits


def part1(data):
    bits = bin(int(data[0], 16))[2:]
    bits = bits.zfill(math.ceil(len(data[0]) / 2 * 8))

    packet, _ = generate_packet(bits)
    print(packet)
    return packet.version_sum


def part2(data):
    bits = bin(int(data[0], 16))[2:]
    bits = bits.zfill(math.ceil(len(data[0]) / 2 * 8))

    packet, _ = generate_packet(bits)
    print(packet)
    return packet.value


if __name__ == "__main__":
    with open(f"{day}.txt", encoding='utf-8', errors='ignore') as f:
        input_data = [line.rstrip() for line in f]

    test_input = \
"""C200B40A82""".split('\n')


    test1_answer = 14
    test1_result = part1(test_input)

    if test1_result == test1_answer:
        print(f"First Question Test Passed")
    else:
        print(f"First Question Test FAILED, Got {test1_result}, expected {test1_answer}")

    print("Answer 1: ", part1(copy.copy(input_data)))

    test2_answer = 3
    test2_result = part2(test_input)

    if test2_result == test2_answer:
        print(f"Second Question Test 1 Passed")
    else:
        print(f"Second Question Test 1 FAILED, Got {test2_result}, expected {test2_answer}")

    print("Answer 2: ", part2(copy.copy(input_data)))
