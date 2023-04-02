## I am so anxious for ap exams I am doing this instead of studying for them. Intelligent human being here folks.

import time

def apExams():
    done = False
    apList = []
    while done == False:
        ap= input("What AP exams are you taking? Type stop to stop.")
        
        if (ap == "stop"):
            done = True
        else:
            apList.append(ap)
    
    return apList

print(apExams())