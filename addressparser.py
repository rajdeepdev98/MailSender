#this function gets the mail addresses and names of the recipients from the txt file
import os
import sys


def get_contacts(filename):
    names=[]
    emails=[]
    with open(os.path.join(sys.path[0], filename), mode='r', encoding='utf-8') as contacts_file:
        
        for contact in contacts_file:
            person=contact.split()
            names.append(person[0])
            emails.append(person[1])

    return names,emails

        

