
def pyramid(height):
    for i in range(int(height)):
        print " "*(int(height)-i-1),"*"*(2*(i+1)-1)," "*(int(height)-i-1)

print pyramid(3)
