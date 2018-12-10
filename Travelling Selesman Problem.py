
n = int(input())
coordinates = []
done = [0]

for x in range(n):

    x, y = [int(i) for i in input().split()]

    coordinates.append([x, y])

currentX = 0
ans = 0

for x in range(n-1):

    minDist = 283
    check = 0

    for i in range(n):

        if i == currentX or i in done:
            continue

        else:

            dist = ( ((coordinates[i][0] - coordinates[currentX][0]) ** 2) + ((coordinates[i][1] - coordinates[currentX][1]) ** 2 )) ** .5

            if dist < minDist:
                minDist = dist
                check = i

    ans += minDist
    currentX = check
    # print(currentX, minDist)
    done.append(currentX)

ans += ( ((coordinates[0][0] - coordinates[currentX][0]) ** 2) + ((coordinates[0][1] - coordinates[currentX][1]) ** 2 )) ** .5

print(round(ans))

