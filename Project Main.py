#
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Darwin White
#               Mark Bruner
#               Varun Wunnava
#               Sebastian Luna
# Section:      563
# Assignment:   Lab 10a Activity 1
# Date:         15 November 2021
#
""" This code uses a given input file of directions in order to direct a self
-driving car in driving on the street. Using the specific directions given
such as "turn left" or "contniue forward", the program creates a list of all
the directions and then follows them in order to get the passenger to the
destination. Each worded direction corresponds to its distance needed, kept in
another list. Furthermore, if the computer does not recognize a direction,
it will tell the passenger to take control to make sure nothin bad happens.
This code has been tested using the Easterwood2Coulter.txt file to make sure
it is sound and has no errors.
"""

import turtle

#Setting color
turtle.Screen().bgcolor("orange")

#This function reads in all of the data from the direction File and returns
# a list of strings containing the direction data
def ReadDirections(file):
    with open(file, "r") as inFile:
        instructions = inFile.read().split("\n")
        while ("" in instructions):
            instructions.remove("")
        for i in range(len(instructions)):
            instructions[i] = instructions[i].strip()
        return instructions
            
#This function uses the list of instructions and the pulls out all of the
# key words such as "Slight left" or "turn right" and returns a list
# of such
def GetKeywords(directions):
    indexCut = 0
    keywords = []
    for each in directions:
        skipFirst = True
        words = each.split()
        for word in words:
            if skipFirst:
                skipFirst = False
                continue
            for letter in range (65, 91):
                if (chr(letter) in word):
                    indexCut = each.index(word)
                    break
            if "Slight right" == each or "Slight left" == each:
                indexCut = 1000
            if "Turn right" == each or "Turn left" == each:
                indexCut = 1000
            if (indexCut != 0):
                break
        keywords.append(each[0:indexCut])
        indexCut = 0
    while ("" in keywords):
        keywords.remove("")
    for i in range(len(keywords)):
        keywords[i] = keywords[i].strip()
    return keywords

#This function uses the list of instructions and pulls out the number
# of miles needed to travel and returns a list of all the numbers
def GetMiles(directions):
    numbers = []
    for each in directions:
        if (ord(each[0]) < 65):
            numbers.append(each)
    for i in range(len(numbers)):
        if ("min" in numbers[i]):
            indexCut = numbers[i].index("min")
            numbers[i] = numbers[i][indexCut + 5: -1]
    for i in range(len(numbers)):
        if ("s" in numbers[i]):
            indexCut = numbers[i].index("s")
            numbers[i] = numbers[i][indexCut + 3: -1]
    return numbers

#This function converts each of the distance values of the direction file
# into all distances of the same unit in floats and returns a list of those 
# values
def ConvertNums(numbers):
    for i in range(len(numbers)):
        if ("ft" in numbers[i]):
            num = int(numbers[i][:-3])
            numInMiles = num / 5280
            numbers[i] = "{:.3f} mi".format(numInMiles)
    for i in range(len(numbers)):
        numbers[i] = float(numbers[i].strip("mi").strip())
    return numbers

#This function converts the float numbers in miles into more Turtle graphics
# friendly numbers to better showcase the path
def ConvertForTurtle(numbers):
    for i in range(len(numbers)):
        numbers[i] = numbers[i] * 50
    return numbers          

#This function splits the information into separate directions
def SplitDirections(keywords, numbers):
    firstKey = []
    secondKey = []
    firstNums = []
    secondNums = []
    for i in range(len(keywords)):
        if ("Drive" in keywords[i]):
            firstKey = keywords[0:i]
            secondKey = keywords[i:]
            firstNums = numbers[0:i]
            secondNums = numbers[i:]
    return firstKey, firstNums, secondKey, secondNums

#This function uses the list of keywords and numbers to map out the path 
# that the self-driving car will take and draws it in Turtle Graphics
def DrawPath(keywords, numbers):
    for i in range(len(keywords)):
        try:
            if ("follow" in keywords[i] or "Follow" in keywords[i]):
                turtle.down()
                continue
            if ("drive" in keywords[i] or "Drive" in keywords[i]):
                turtle.down()
                continue
            if ("right" in keywords[i] or "Right" in keywords[i]):
                if ("turn" in keywords[i] or "Turn" in keywords[i]):
                    turtle.right(90)
                    turtle.forward(numbers[i])
                    continue
                elif ("slight" in keywords[i] or "Slight" in keywords[i]):
                    turtle.right(20)
                    turtle.forward(numbers[i])
                    continue
            if ("left" in keywords[i] or "Left" in keywords[i]):
                if ("turn" in keywords[i] or "Turn" in keywords[i]):
                    turtle.left(90)
                    turtle.forward(numbers[i])
                    continue
                elif ("slight" in keywords[i] or "Slight" in keywords[i]):
                    turtle.left(20)
                    turtle.forward(numbers[i])
                    continue
            if ("continue" in keywords[i] or "Continue" in keywords[i]):
                turtle.forward(numbers[i])
                continue
            if ("head" in keywords[i] or "Head" in keywords[i]):
                turtle.forward(numbers[i])
        except:
            print("Could not recognize that direction. Please take control.")

#Main function to run the code
def Main():
    directions = ReadDirections("Easterwood2Coulter.txt")
    keywords = GetKeywords(directions)
    for each in keywords:
        if ("Pass by" in each or "Continue to follow" in each):
            keywords.remove(each)
    numbers = GetMiles(directions)
    mileNums = ConvertNums(numbers)
    turtleNums = ConvertForTurtle(mileNums)
    eachSet = SplitDirections(keywords, turtleNums)
    DrawPath(keywords, turtleNums)
    # DrawPath(eachSet[0], eachSet[1])
    input()
    # up()
    # clear()
    # DrawPath(eachSet[2], eachSet[3])
    # input()
    # up()
    # clear()
    

if __name__ == '__main__':
    Main()
    