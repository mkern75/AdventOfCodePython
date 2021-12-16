import math

file = open("./year2021/data/day16.txt", "r")
lines = [line.rstrip('\n') for line in file]


def hex2bin(hex_seq):
    bin_seq = bin(int(hex_seq, 16))[2:]
    while len(bin_seq) < 4 * len(hex_seq):
        bin_seq = "0" + bin_seq
    return bin_seq


# returns pair: packet, remaining_bits
# a packet is a tuple of (version, type_id, literal_value, list_of_sub_packets)
def parse(bit_seq):
    version = int(bit_seq[:3], 2)
    bit_seq = bit_seq[3:]
    type_id = int(bit_seq[:3], 2)
    bit_seq = bit_seq[3:]

    if type_id == 4:
        literal = ""
        while bit_seq[0] == "1":
            literal += bit_seq[1:5]
            bit_seq = bit_seq[5:]
        literal += bit_seq[1:5]
        bit_seq = bit_seq[5:]
        return (version, type_id, int(literal, 2), []), bit_seq

    sub_packets = []
    length_type_id = bit_seq[0]
    bit_seq = bit_seq[1:]

    if length_type_id == "0":
        total_length = int(bit_seq[:15], 2)
        bit_seq = bit_seq[15:]
        while total_length > 0:
            sub_packet, new_bits = parse(bit_seq)
            sub_packets += [sub_packet]
            total_length -= len(bit_seq) - len(new_bits)
            bit_seq = new_bits
    else:
        number_sub_packets = int(bit_seq[:11], 2)
        bit_seq = bit_seq[11:]
        for i in range(number_sub_packets):
            sub_packet, new_bits = parse(bit_seq)
            sub_packets += [sub_packet]
            bit_seq = new_bits

    return (version, type_id, None, sub_packets), bit_seq


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


hex_seq = lines[0]
bin_seq = hex2bin(hex_seq)
packet, _ = parse(bin_seq)
print(sum_versions(packet))
print(evaluate(packet))
