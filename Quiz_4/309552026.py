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
    # print(seed.len)
    return seed

def Bit(num):
    zero = BitArray(length=8)
    target = BitArray(bin=bin(num))
    for i in range(target.len):
        zero[-i-1] = target[-i-1]
    return zero

if __name__ == '__main__':
    image = Image.open("Xpipe.png")
    image = Image.open("pipe.png")

    ### Part 1
    print("Show keys when seed = 0b01101000010 and tap = 8:")
    tap = 8
    seed = BitArray(bin='0b01101000010')
    key = seed
    for i in range(10):
        key = LFSR(tap, key)
        print(key.bin, int(key[key.len - 1]))

    ### Part 2 將pipe.png加密並還原
    image = Image.open("pipe.png")
    tap = 16
    seed = BitArray(bin='0b01101000010100010000')
    # 加密
    key = seed
    for i in range(image.width):
        for j in range(image.height):
            RGB = list(image.getpixel((i, j)))
            for k in range(3):
                key = Generate(tap, 8, key)
                RGB[k] = (Bit(RGB[k]) ^ key[-8:]).uint
            image.putpixel((i, j), tuple(RGB))
    # 還原
    key = seed
    for i in range(image.width):
        for j in range(image.height):
            RGB = list(image.getpixel((i, j)))
            for k in range(3):
                key = Generate(tap, 8, key)
                RGB[k] = (Bit(RGB[k]) ^ key[-8:]).uint
            image.putpixel((i, j), tuple(RGB))
    image.show()

    ### Part 3 將Xpipe.png還原
    image = Image.open("Xpipe.png")
    key = seed
    for i in range(image.width):
        for j in range(image.height):
            RGB = list(image.getpixel((i, j)))
            for k in range(3):
                key = Generate(tap, 8, key)
                RGB[k] = (Bit(RGB[k]) ^ key[-8:]).uint
            image.putpixel((i, j), tuple(RGB))
    image.show()