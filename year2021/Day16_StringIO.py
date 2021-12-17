from io import StringIO  # learning something new ...
import math

file = open("./year2021/data/day16.txt", "r")
lines = [line.rstrip('\n') for line in file]


def hex2bin(hex_seq):
    bin_seq = bin(int(hex_seq, 16))[2:]
    while len(bin_seq) < 4 * len(hex_seq):
        bin_seq = "0" + bin_seq
    return bin_seq


# parses a string stream and returns a packet and all its sub-packets
# returns pair: packet, bit_io (string stream after reading the current packet)
# a packet is a tuple of (version, type_id, literal_value, list_of_sub_packets)
def parse(bit_io):
    version = int(bit_io.read(3), 2)
    type_id = int(bit_io.read(3), 2)

    if type_id == 4:
        literal = ""
        group = bit_io.read(5)
        while group[0] == "1":
            literal += group[1:]
            group = bit_io.read(5)
        literal += group[1:]
        return (version, type_id, int(literal, 2), []), bit_io

    sub_packets = []
    length_type_id = bit_io.read(1)

    if length_type_id == "0":
        total_length = int(bit_io.read(15), 2)
        start_pos = bit_io.tell()
        while bit_io.tell() - start_pos < total_length:
            sub_packet, bit_io = parse(bit_io)
            sub_packets += [sub_packet]
    else:
        number_sub_packets = int(bit_io.read(11), 2)
        for _ in range(number_sub_packets):
            sub_packet, bit_io = parse(bit_io)
            sub_packets += [sub_packet]

    return (version, type_id, None, sub_packets), bit_io


def sum_versions(packet):
    version, _, _, sub_packets = packet
    return version + sum(sum_versions(sub_packet) for sub_packet in sub_packets)


def evaluate(packet):
    version, type_id, literal, sub_packets = packet
    if type_id == 0:
        return sum(evaluate(sub_packet) for sub_packet in sub_packets)
    elif type_id == 1:
        return math.prod(evaluate(sub_packet) for sub_packet in sub_packets)
    elif type_id == 2:
        return min(evaluate(sub_packet) for sub_packet in sub_packets)
    elif type_id == 3:
        return max(evaluate(sub_packet) for sub_packet in sub_packets)
    elif type_id == 4:
        return literal
    elif type_id == 5:
        return 1 if evaluate(sub_packets[0]) > evaluate(sub_packets[1]) else 0
    elif type_id == 6:
        return 1 if evaluate(sub_packets[0]) < evaluate(sub_packets[1]) else 0
    elif type_id == 7:
        return 1 if evaluate(sub_packets[0]) == evaluate(sub_packets[1]) else 0


bit_io = StringIO(hex2bin(lines[0]))
packet, _ = parse(bit_io)
print(sum_versions(packet))
print(evaluate(packet))
