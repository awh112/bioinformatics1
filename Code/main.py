from DNA import *

dir = input("Enter the directory of the input file: ")

file = open(dir, 'r')

input = file.read()

outputFile = open(dir + "_output", 'w')
outputFile.write(PatternStartIndices(input, "CTTGATCAT"))
outputFile.close()

print(PatternStartIndices(input, "CTTGATCAT"))