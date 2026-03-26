import math
def pattern(numRows, arr):
    for i in range(0,numRows):
        for j in range(0,3):
            if arr[i][j] == 0:
                if j == 1:
                    x = arr[i][j+1] - (arr[i][j-1])**2
                    return int(math.sqrt(x))
                elif j == 0:
                    x = arr[i][j+2] - (arr[j][j+1])**2
                    return int(math.sqrt(x))
                else :
                    x = (arr[i][j-2])**2 + (arr[i][j-1])**2
                    return int(x)
    return 0

if __name__ == "__main__":
    numRows = int(input())
    arr = [list(map(int, input().split())) for _ in range(numRows)]
    print(pattern(numRows, arr))