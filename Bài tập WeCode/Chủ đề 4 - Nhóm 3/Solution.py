def moving(x, y, char):
    if char == 'L':
        y -= 1
    elif char == 'R':
        y += 1
    elif char == 'U':
        x -= 1
    elif char == 'D':
        x += 1
    return x, y


def isRobotSafe(rowNum, columnNum, string):
    count = 0
    for row in range(rowNum):
        for column in range(columnNum):
            x, y = row, column
            for index in range(len(string)):
                x, y = moving(x, y, string[index])
                if x not in range(rowNum) or y not in range(columnNum):
                    count += 1
                    break
    if count == rowNum * columnNum:
        return False
    return True


height, width = [int(x) for x in input().split()]
string = input()
print("Safe") if isRobotSafe(height, width, string) else print("Unsafe")
