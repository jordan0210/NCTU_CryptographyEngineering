from bitstring import BitArray

def LFSR(key):
    nextKey = BitArray(length=8)
    for i in range(7):
        nextKey[i] = key[i] ^ key[i+1]
    nextKey[7] = key[7] ^ nextKey[0]
    return nextKey

if __name__ == "__main__":
    C = ["11000111", "11001110", "11000110", "11010100", "11001001",
        "11001111", "11101111", "10110000", "01010100", "01010001",
        "01000010", "01011101", "01010000", "01110000", "00011100",
        "10110001", "01010111", "01010101", "01011011", "01001011",
        "01100111", "00100011", "11100101"]
    seed = BitArray(bin='0b10000000')

    key = seed
    print("PlainText = ", end='')
    for i in range(len(C)):
        P = chr((BitArray(bin=C[i]) ^ key).uint)
        print(P, end='')
        key = LFSR(key)

    # Check the max len of key cycle
    keys = []
    key = seed
    keys.append(key.bin)
    while True:
        key = LFSR(key)
        if (key.bin in keys):
            break
        else:
            keys.append(key.bin)
    print("\nmaximal length =", len(keys))