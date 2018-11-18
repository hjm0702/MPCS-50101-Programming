def divide_by(number):
    number = raw_input("Enter a number: ")
    total = 0
    if number.isdigit():
        for i in range(len(number)):
            if i % 2 == 0:
                total = total + int(number[i])
            else:
                total = total - int(number[i])
        if total % 11 == 0:
            return "This is divisible by 11."
        return "This is not divisible by 11."
        # else:
        #     for i in range(len(number)-1):
        #         if i % 2 == 0:
        #             total = total + int(number[1:][i])
        #         else:
        #             total = total - int(number[1:][i])
    elif number[0] == "-" and number[1:].isdigit():
        for i in range(len(number)-1):
            if i % 2 == 0:
                total = total + int(number[1:][i])
            else:
                total = total - int(number[1:][i])
        if total % 11 == 0:
            return "This is divisible by 11."
        return "This is not divisible by 11."
    else:
        return "Input must be a number."

print divide_by(123)
