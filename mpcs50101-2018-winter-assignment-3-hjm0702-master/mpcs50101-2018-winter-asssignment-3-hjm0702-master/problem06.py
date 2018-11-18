file = open("./points.txt", "r")
point = []
for line in file:
    line = line.strip()
    a = line.split(",")
    point.append(a[1:4])
# point.strip()
# print point

#dis0 = distance from origin
dis0 = 0.0
for i in range(len(point)):
    # print i
    for j in range(len(point[i])):
        dis0 = dis0 + (float(point[i][j]))**2
    print dis0**0.5
    dis0 = dis0 * 0

print "Point3 is the closest to the origin."

index = [0,1,2,3]
print range(len(point))
for i in range(len(point)):
    for j in index[i+1:4]:
        for m in range(len(point[i])):
            dis0 = dis0 + (float(point[i][m])-float(point[j][m]))**2
            # print i, j, m
        print dis0**0.5, "point", i+1, "between", "point", j+1
        dis0 = dis0 * 0
print "Point 1 to point 4 is the closest."

# for i in range(len(point)):
#     for m in range(len(point[i])):
#             dis0 = dis0 + (float(point[i][m])-float(point[i+1][m]))**2
#             print i, j, m, n
#     print dis0**0.5, "point", i+1, "between", "point", j+1
#     dis0 = dis0 * 0
    # dis0 = dis0 + float(point[i][j])^2
        # print point[i][j]
# print dis0
