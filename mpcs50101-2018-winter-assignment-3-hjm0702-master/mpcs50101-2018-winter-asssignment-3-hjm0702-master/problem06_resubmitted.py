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
lengh_origin = []
for i in range(len(point)):
    # print i
    for j in range(len(point[i])):
        dis0 = dis0 + (float(point[i][j]))**2
    lengh_origin.append(dis0**0.5)
    # print dis0**0.5
    dis0 = dis0 * 0

answer1 = lengh_origin.index(min(lengh_origin))+1
print "Point", answer1, 'is the closest to the origin.'

length_each = []
first_points = []
second_points = []
index = [0,1,2,3]
# print range(len(point))
for i in range(len(point)):
    for j in index[i+1:4]:
        for m in range(len(point[i])):
            dis0 = dis0 + (float(point[i][m])-float(point[j][m]))**2
            # print i, j, m
        length_each.append(dis0**0.5)
        first_points.append(i+1)
        second_points.append(j+1)
        # print first_points, second_points
        # print dis0**0.5, "point", i+1, "between", "point", j+1
        dis0 = dis0 * 0

print "Point", first_points[length_each.index(min(length_each))], 'and Point', second_points[length_each.index(min(length_each))], 'is the closest'


# print "Point 1 to point 4 is the closest."

# for i in range(len(point)):
#     for m in range(len(point[i])):
#             dis0 = dis0 + (float(point[i][m])-float(point[i+1][m]))**2
#             print i, j, m, n
#     print dis0**0.5, "point", i+1, "between", "point", j+1
#     dis0 = dis0 * 0
    # dis0 = dis0 + float(point[i][j])^2
        # print point[i][j]
# print dis0
