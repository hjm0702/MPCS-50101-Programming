
numbers = [1,4,5,6,100]
average = 0

# Approach 1
def centered_average_with_iteration(numbers):
    total = 0
    if len(numbers) >= 3:
        for i in range(len(numbers)):
            total = total + numbers[i]
        average = (total - min(numbers) - max(numbers))/(len(numbers)-2)
        return average
    else :
        print "The length of the input is shorter than 3."

# Approach 2
def centered_average(numbers):
    total = 0
    if len(numbers) >= 3:
        average = (sum(numbers) - min(numbers) - max(numbers))/(len(numbers)-2)
        return average
    else :
        print "The length of the input is shorter than 3."

print centered_average_with_iteration(numbers)
print centered_average(numbers)
