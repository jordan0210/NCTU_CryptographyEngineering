from bitstring import BitArray

if __name__ == '__main__':
    Bits = BitArray(bin='0b01000')
    print("1000 init:", end="")
    for i in range(100):
        print(int(Bits[-1]), end="")
        Bits[0] = Bits[1] ^ Bits[4]
        Bits = Bits >> 1

    Bits = BitArray(bin='0b01111')
    print("\n1111 init:", end="")
    for i in range(100):
        print(int(Bits[-1]), end="")
        Bits[0] = Bits[1] ^ Bits[4]
        Bits = Bits >> 1

    Bits = BitArray(bin='0b00110')
    print("\n0110 init:", end="")
    for i in range(100):
        print(int(Bits[-1]), end="")
        Bits[0] = Bits[1] ^ Bits[4]
        Bits = Bits >> 1