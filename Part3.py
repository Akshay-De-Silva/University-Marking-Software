"""
The program should prompt for the number of credits at pass, defer and fail 
and then display the appropriate progression outcome for an individual student 
(i.e., progress, trailing, module retriever or exclude).
but also allows a staff member to predict progression outcomes for multiple students
"""
studentuser=True
usertype=True
mainuserflag=False

valid=False
passvalid=False
defervalid=False
failvalid=False

endloop=False

progress=0
progressMT=0
notprogress=0
exclude=0

credittype=True
repeatvalid=False

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

def histogram(count):   #function to calculate the number of stars needed for the given count input 
    starcount=[]
    for _ in range(count):
        starcount.append('*')
    finalstarcount=''.join(starcount)
    return finalstarcount


while not mainuserflag: #function to determine if a user is a student or staff member
    user=input("If you are a Student please enter 1, If you are a Staff Member please press 2: ")
    usertype=True
    try:
        int(user)
    except ValueError:
        print("Invalid input detected")
        usertype=False
    if usertype:
        user=int(user)
        if user==1:
            mainuserflag=True
            print("\nHello Student")
        elif user==2:
            studentuser=False
            mainuserflag=True
            print("\nHello Staff Member")
        else:
            print("Number entered was not 1 or 2 please try again")


while not endloop:  #this loop will end once the student gets their predicted progression outcome or when the staff member has gotten all the predicted progression outcomes they require
    while not valid:    #this loop will end once all 3 inputs are valid
        while not passvalid:    #this loop will end once a valid pass value has been entered
            creditpass=input("\nPlease enter your pass credits: ")
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
        progress+=1 #counter used for the histogram
        print("Progress")
    elif creditpass==100:
        progressMT+=1   #counter used for the histogram
        print("Progress (Module Trailer)")
    elif creditfail>=80:    #since 80 and higher is the fail margin any fail credit above or equal to 80 is an automatic exclude
        exclude+=1  #counter used for the histogram
        print("Exclude")
    else:
        notprogress+=1  #counter used for the histogram
        print("Do not Progress - Module Retriever") 

    
    if studentuser: #if user is a student they only need to predict their own progression outcome
        endloop=True
    else:   #if user is a staff member they are given the choice to repeat the input process as they need to predict multiple students outcomes
        repeatvalid=False
        while repeatvalid==False:
            repeatcredits=input("\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ")
            try:
                str(repeatcredits)
            except ValueError:
                print("Invalid input detected")
                credittype=False
            if credittype:
                if repeatcredits=='q':
                    endloop=True
                    repeatvalid=True
                elif repeatcredits=='y':
                    valid=False
                    passvalid=False
                    defervalid=False
                    failvalid=False
                    repeatvalid=True
                else:
                    print("\nValue entered was not y or q please try again")


if not studentuser: #if user is a staff member then they are provided with a histogram of all the outputs they recieved from the loop
    print("\n---------------------------------------------------------------\nHorizontal Histogram")
    print(f"Progress {progress} : {histogram(progress)}")
    print(f"Trailer {progressMT} : {histogram(progressMT)}")
    print(f"Retriever {notprogress} : {histogram(notprogress)}")
    print(f"Excluded {exclude} : {histogram(exclude)}")

    total=progress+progressMT+notprogress+exclude
    print(f"\n{total} outcomes in total.")
    print("---------------------------------------------------------------")