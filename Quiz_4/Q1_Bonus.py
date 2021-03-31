from bitstring import BitArray
from PIL import Image

def LFSR(tap, seed):
    xor = seed << 1
    xor[-1] = seed[0] ^ seed[seed.len - 1 - tap]
    return xor

def Generate(tap, step, seed):
    for i in range(step):
        xor = seed << 1
        xor[-1] = seed[0] ^ seed[seed.len - 1 - tap]
        seed = xor
    return seed

def Bit(num):
    zero = BitArray(length=8)
    target = BitArray(bin=bin(num))
    for i in range(target.len):
        zero[-i-1] = target[-i-1]
    return zero

if __name__ == '__main__':
    image = Image.open(input("png File name: "))

    tap = 16
    seed = BitArray(bin='0b01101000010100010000')
    key = seed
    for i in range(image.width):
        for j in range(image.height):
            RGB = list(image.getpixel((i, j)))
            for k in range(3):
                key = Generate(tap, 8, key)
                RGB[k] = (Bit(RGB[k]) ^ key[-8:]).uint
            image.putpixel((i, j), tuple(RGB))
    image.show()