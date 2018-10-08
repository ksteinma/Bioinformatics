import math

def affine_align(match, mismatch, opening, extend, first, second):
    """
    When run, this program will prompt for a file name for a file within
    the same folder. After entering the filename, the program will print
    output containing the global alignment.
    """
    #used to represent negative infinity inside matrices
    infinity = -1*math.inf
    
    #lengths used for iterating and forming matrices
    l1 = len(first)
    l2 = len(second)
    
    #initialize matrices to zeros
    #M is for aligning i and j --> source diagonal
    M = [[0 for y in range(l1)] for x in range(l2+1)]
    #Ix is for gapping i --> source above (gap)
    Ix = [[0 for y in range(l1)] for x in range(l2+1)]
    #Iy is for gapping j --> source left (gap)
    Iy = [[0 for y in range(l1)] for x in range(l2+1)]

    #initialize with penalties
    M[0][0] = 0
    Ix[0][0] = infinity
    Iy[0][0] = infinity
    for i in range(1,l1): 
        M[0][i] = infinity # first row is negative inf
        Ix[0][i] = infinity # first row is negative inf
        Iy[0][i] = -1*opening - (i-1)*extend # first row is gapping

    for j in range(1,l2+1): 
        M[j][0] = infinity # first column is negative inf
        Ix[j][0] = -1*opening - (j-1)*extend # first column is gapping
        Iy[j][0] = infinity # first column is negative inf

    #generate the remaining matrix values
    for i in range(l2):
        for j in range(l1-1):
            #match or mismatch
            if (first[j] == second[i]):
                s = match
            else:
                s = -1*mismatch
            M[i+1][j+1] = max((M[i][j] + s), (Ix[i][j]+s), (Iy[i][j] + s))
            Ix[i+1][j+1] = max((M[i][j+1] - opening), (Ix[i][j+1] - extend))
            Iy[i+1][j+1] = max((M[i+1][j] - opening), (Iy[i+1][j] - extend))

    #start at largest of M(m,n), I(m,n)
    output1 = ''
    output2 = ''
    i = l2;
    j = l1-1;

    #while we have not reached index 0,0 (end of traversal)
    #traverse in reverse to find alignment
    while (i!=0 or j!=0):
        #find the max
        current = max((M[i][j]), (Ix[i][j]), (Iy[i][j]))
        if (current == M[i][j]):
            #match
            i = i-1
            j = j-1
            output1 = first[j] + output1
            output2 = second[i] + output2
        elif (current == Ix[i][j]):
            #gap i
            i = i-1
            output1 = '_' + output1
            output2 = second[i] + output2
        else:
            #gap j
            j = j-1
            output1 = first[j] + output1
            output2 = '_' + output2
           
    print(output1)
    print(output2)

def main():
    filename = input('Please enter the filename that you would like to read sequences from:\n')
    content = open(filename, 'r')
    numbers = content.readline()
    numbers = numbers.split()
    match = int(numbers[0])
    mismatch = int(numbers[1])
    opening = int(numbers[2])
    extend = int(numbers[3])
    first = content.readline()
    second = content.readline()
    #call alignment
    affine_align(match, mismatch, opening, extend, first, second)



if __name__ == "__main__":
    main()
