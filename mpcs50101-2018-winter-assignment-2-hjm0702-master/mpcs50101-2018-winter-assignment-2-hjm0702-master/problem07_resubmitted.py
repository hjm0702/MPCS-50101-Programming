def pyramid(height):

    for i in range(height):
        print " "*(height-i-1), "*"*(1+i*2)," "*(height-i-1)

print pyramid(8)
