C = input("輸入密文:")

for i in range(26):
    print(chr(ord('A') + i) + ": ", C.count(chr(ord('A') + i)))