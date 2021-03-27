from bitstring import BitArray

if __name__ == '__main__':
    Bits_1 = BitArray(bin='0b01111')
    Bits_2 = BitArray(bin='0b11111')
    print("Sequence 1: ", end="")
    for i in range(100):
        print(int(Bits_1[-1]), end="")
        Bits_1[0] = Bits_1[3] ^ Bits_1[4]
        Bits_1 = Bits_1 >> 1

    print("\nSequence 2: ", end="")
    for i in range(100):
        print(int(Bits_2[-1]), end="")
        temp = Bits_2 >> 1
        temp[0] = Bits_2[2] ^ Bits_2[4]
        temp[1] = Bits_2[0] ^ Bits_2[1]
        Bits_2 = temp