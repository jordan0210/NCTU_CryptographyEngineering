import numpy as np
import math

def readFile(filename):
    file = open(filename, 'r')

    line = file.readline()
    data = ""
    while line:
        data += line
        line = file.readline()

    data = data.replace(" ", "").replace("\n", "")
    return data

def reorder(testdata):
    returnColumn = 0
    difference = 100
    for i in range(4, len(testdata)):
        if (len(testdata)%i == 0):
            row = int(len(testdata)/i)
            reorderTestdata = [['']*i for j in range(row)]
            for j in range(row):
                for k in range(i):
                    reorderTestdata[j][k] = testdata[(j*i + k)]

            frequence = 0
            for k in range(i):
                sum = 0
                for j in range(row):
                    if (reorderTestdata[j][k] in "AEIOU"):
                        sum += 1
                frequence += abs(sum - row * 0.4)
            if (frequence < difference):
                returnColumn = i
                difference = frequence

    returnRow = int(len(testdata)/returnColumn)
    returnMatrix = [['']*returnColumn for i in range(returnRow)]
    for i in range(returnRow):
        for j in range(returnColumn):
            returnMatrix[i][j] += testdata[(i*returnColumn + j)]
    return returnMatrix, returnColumn, returnRow

def getAnswer(frequence, data, column, row, first, second):
    check = [False]*row
    answer = [['']*column for i in range(row)]
    answer[0] = data[first]
    check[first] = True
    answer[1] = data[second]
    check[second] = True
    count = 2
    while (count < row):
        probability = [0]*row
        for i in range(row):
            if check[i]:
                continue
            for j in range(column):
                if (frequence[ord(answer[count-2][j]) - ord('A')][ord(answer[count-1][j]) - ord('A')][ord(data[i][j]) - ord('A')] == 0):
                    continue
                probability[i] += math.log10(26*frequence[ord(answer[count-2][j]) - ord('A')][ord(answer[count-1][j]) - ord('A')][ord(data[i][j]) - ord('A')])
        answer[count] = data[np.argmax(probability)]
        check[np.argmax(probability)] = True
        count += 1
    for line in np.array(answer).T:
        for char in line:
            print(char, end='')



if __name__ == "__main__":
    traindata = readFile("traindata.txt")

    frequence = np.zeros((26, 26, 26))
    A = ord('A')
    for i in range(len(traindata) - 2):
        frequence[ord(traindata[i]) - A][ord(traindata[i+1]) - A][ord(traindata[i+2]) - A] += 1

    for i in range(26):
        for j in range(26):
            sum = 0
            for k in range(26):
                sum += frequence[i][j][k]
            if (sum == 0):
                continue
            for k in range(26):
                frequence[i][j][k] = frequence[i][j][k]/sum

    print("Testcase 1:")
    data, column, row = reorder(readFile("testdata1.txt"))
    getAnswer(frequence, data, column, row, 5, 2)
    print("\nTestcese 2:")
    data, column, row = reorder(readFile("testdata2.txt"))
    getAnswer(frequence, data, column, row, 2, 5)