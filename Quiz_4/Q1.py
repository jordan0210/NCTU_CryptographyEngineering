from bitstring import BitArray

def LFSR(tap, seed):
    xor = seed << 1
    xor[-1] = seed[0] ^ seed[seed.len - 1 - tap]
    return xor

if __name__ == '__main__':
    tap = int(input("tap= "))
    seed = BitArray(bin=input("seed= "))
    key = seed
    for i in range(10):
        key = LFSR(tap, key)
        print(key.bin, int(key[key.len - 1]))