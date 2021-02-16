
def findCircleNum(M):
    # Write your code here
    circle_count = 0
    circled = set()
    for row in range(len(M)):
        col = 0
        while col <= row + 1:
            if col in circled:
                continue
            if (M[row][col] == 1) and (col not in circled):
                circled.add(col)
                break
            col += 1
    return len(circled)

m = [[1,1,0],[1,1,0],[0,0,1]]

result = findCircleNum(m)
print(result)
