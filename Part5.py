"""
program to obtain the data from a list, tuple or dictionary and not from user input. A histogram related to the data will be output 
"""
rowcount=0
progress=0
progressMT=0
notprogress=0
exclude=0

grades=[[120,0,0],[100,20,0],[100,0,20],[80,20,20],[60,40,20],[40,40,40],[20,40,60],[20,20,80],[20,0,100],[0,0,120]] #list of all the data

def histogram(count):   #function to calculate the number of stars needed for the given count input 
    starcount=[]
    for _ in range(count):
        starcount.append('*')
    finalstarcount=''.join(starcount)
    return finalstarcount

while rowcount<=9:
    if grades[rowcount][0]==120:  #checks if the student has progressed
        progress+=1 #counter used for the histogram
        print("Progress")
    elif grades[rowcount][0]==100:
        progressMT+=1   #counter used for the histogram
        print("Progress (Module Trailer)")
    elif grades[rowcount][2]>=80:    #since 80 and higher is the fail margin any fail credit above or equal to 80 is an automatic exclude
        exclude+=1  #counter used for the histogram
        print("Exclude")
    else:
        notprogress+=1  #counter used for the histogram
        print("Do not Progress - Module Retriever") 
    rowcount+=1


print("\n---------------------------------------------------------------\nHorizontal Histogram")#horizontal histogram
print(f"Progress {progress} : {histogram(progress)}")
print(f"Trailer {progressMT} : {histogram(progressMT)}")
print(f"Retriever {notprogress} : {histogram(notprogress)}")
print(f"Excluded {exclude} : {histogram(exclude)}")

total=progress+progressMT+notprogress+exclude
print(f"\n{total} outcomes in total.")
print("---------------------------------------------------------------")