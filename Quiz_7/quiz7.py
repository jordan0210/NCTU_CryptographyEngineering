from bitarray.util import urandom

if __name__ == "__main__":
    file = open("result","w+")
    data = urandom(5120000)
    file.write(data.to01())