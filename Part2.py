"""
The program should prompt for the number of credits at pass, defer and fail 
and then display the appropriate progression outcome for an individual student 
(i.e., progress, trailing, module retriever or exclude).
"""
valid=False
passvalid=False
defervalid=False
failvalid=False

def typerangevalidity(credit):   #function tests if the input is an integer and then if input is in the range
    typeflag=True
    try:
        int(credit)
    except ValueError:
        print("Integer Required")
        typeflag=False
    if typeflag:
        credit=int(credit)
        rangevalid=True
        creditrange=[0,20,40,60,80,100,120]
        if credit not in creditrange:
            print("Out of range")
            rangevalid=False
        return rangevalid

def totalvalidity(credit1,credit2,credit3):  #function tests if the sum of the inputs is 120
    totalvalid=True
    total=credit1+credit2+credit3
    if total!=120:
        print("Total incorrect")
        totalvalid=False
    return totalvalid
        

while not valid:
    while not passvalid:    #this loop will end once a valid pass value has been entered
        creditpass=input("Please enter your pass credits: ")
        if typerangevalidity(creditpass):
            creditpass=int(creditpass)
            passvalid=True

    while not defervalid:   #this loop will end once a valid defer value has been entered
        creditdefer=input("Please enter your defer credits: ")
        if typerangevalidity(creditdefer):
            creditdefer=int(creditdefer)
            defervalid=True

    while not failvalid:    #this loop will end once a valid fail value has been entered
        creditfail=input("Please enter your fail credits: ")
        if typerangevalidity(creditfail):
            creditfail=int(creditfail)
            failvalid=True

    if totalvalidity(creditpass,creditdefer,creditfail):    #if the total is incorrect the whole input process is repeted till the sum of the inputs is 120
        valid=True
    else:
        passvalid=False
        defervalid=False
        failvalid=False


if creditpass==120:  #checks if the student has progressed 
    print("Progress")
elif creditpass==100:
    print("Progress (Module Trailer)")
elif creditfail>=80:    #since 80 and higher is the fail margin any fail credit above or equal to 80 is an automatic exclude
    print("Exclude")
else:
    print("Do not Progress - Module Retriever") 