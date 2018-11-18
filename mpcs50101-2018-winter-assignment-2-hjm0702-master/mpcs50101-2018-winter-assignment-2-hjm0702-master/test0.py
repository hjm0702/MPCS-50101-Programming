while True:
    response = raw_input(" Are you ready? ")
    if response.lower() == "yes":
        print ("Then lets get started!")
        break
    elif response.lower()=="no":
        print ("Please try again later....")
        break
    else:
        print ("Please enter a 'yes' or 'no' response!")
