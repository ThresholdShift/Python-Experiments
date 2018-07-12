import math

#a function to take a string and determine if it's a palindrome
def isPalindrome(NumString):
    if NumString[1] == 'b':
        NumString = NumString[2:] #test if it's a binary number with '0b' header, and remove it
    
    for i in range(math.ceil(len(NumString)/2)):
        if NumString[i] != NumString[len(NumString)-i-1]:
            return False

    return True


def flip(num):
    numList = list(str(num))

    for i in range(math.floor(len(numList)/2)):
        buffer = numList[i]
        numList[i] = numList[len(numList)-1-i]
        numList[len(numList)-1-i] = buffer

    numStr = ''.join(numList)
    return int(numStr)\



num = 61

for i in range(1,20):
    palin = flip(num)
    nextNum = num + palin
    print(i,' ~~~ ', num, ' + ', palin, ' = ', nextNum)
    num = nextNum
    if(isPalindrome(str(num))):
        print('palindrome')

