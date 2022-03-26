"""
The program should prompt for the number of credits at pass, defer and fail 
and then display the appropriate progression outcome for an individual student 
(i.e., progress, trailing, module retriever or exclude).
"""

creditpass=int(input("Please enter your pass credits: "))   #get student input for their pass, defer and fail credits
creditdefer=int(input("Please enter your defer credits: "))
creditfail=int(input("Please enter your fail credits: "))

if creditpass==120:  #checks if the student has progressed 
    print("Progress")
elif creditpass==100:
    print("Progress (Module Trailer)")
elif creditfail>=80:    #since 80 and higher is the fail margin any fail credit above or equal to 80 is an automatic exclude
    print("Exclude")
else:
    print("Do not Progress - Module Retriever") 