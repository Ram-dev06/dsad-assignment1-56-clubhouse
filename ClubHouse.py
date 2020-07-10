# -*- coding: utf-8 -*-
from Applicant import Applicant
from HashTable import HashTable

def insertAppDetails(ApplicationRecords, name, phone, memRef, status):
     """This method Insert the applicant record in hash table """
     p1 = Applicant(name, phone,memRef,status)
     ApplicationRecords.records.put(p1.name,p1)

def updateAppDetails(ApplicationRecords, name, phone, memRef, status):
    """This method will update the value based on key , if key is same and its present in hash table than it will update the record 
    otherwise will insert."""
    p1 = Applicant(name, phone,memRef,status)
    ApplicationRecords.records.put(p1.name,p1)

def memRef(ApplicationRecords, memRefId):
    """This method will serach the applicant based on member reference id. """
    res = []
    for val in ApplicationRecords.records.values():
        if val.memberReferenceId== memRefId :
              res.append(val)

    return res

def appStatus(ApplicationRecords):
    """This method will print the statics of applicant status."""
    applied=0
    verified=0
    approved=0

    for val in ApplicationRecords.records.values():
        if(val.status=="Applied"):
            applied=applied+1
        if(val.status=="Verified"):
            verified=verified+1
        if(val.status=="Approved"):
            approved=approved+1


    return "Applied: "+str(applied)+ "\n\nVerified : "+str(verified)+"\n\nAproved : "+str(approved)

def destroyHash(ApplicationRecords):
    """This method will clean the record from hash table."""
    ApplicationRecords.records.clear()

class ApplicationRecords :

    def initializeHash(self):
        self.records=HashTable()


def main():

    appRecords=ApplicationRecords()
    appRecords.initializeHash()

    with open("inputPS8.txt", "r") as inputFile: #Open input file. 
        with open("outputPS8.txt", "w") as outFile: # Open output file.
            with open("promptsPS8.txt", "r") as promptsFile: # open prompt file.

                __process_insertion__(inputFile ,outFile,appRecords) # Call thie medthod to process file data 

                for line in promptsFile:

                    currentline = line.strip().split(":")

                    if(currentline!= None and len(currentline)>1  and currentline[0].strip()=="Update"):
                        __process_update__(outFile,appRecords,currentline)
                    elif (currentline!= None and len(currentline)>1  and currentline[0].strip()=="memberRef"):
                        __process_member_reference__(outFile,appRecords,currentline)

                    elif(currentline!= None and len(currentline)>1  and currentline[0].strip()=="appStatus"):
                        __process_app_status__(outFile,appRecords)
    
    destroyHash(appRecords) # clean the hash table


def __process_member_reference__(outFile ,appRecords,currentline) :
    """This method retrive the list of applicant based on member reference number.and write into the output. """
    outFile.write("---------- Member reference by "+currentline[1]+" ----------\n\n")
    apps=memRef(appRecords,currentline[1].strip())
    for val in apps:
        outFile.write(val.name+" / "+val.phoneNumber+" / " +val.status+"\n\n")
        outFile.write("-------------------------\n\n")

def __process_app_status__(outFile ,appRecords) :
    """This method get the application status and write into the output."""
    outFile.write("-----------Application Status--------------\n\n")
    outFile.write(appStatus(appRecords)+"\n\n")
    outFile.write("-------------------------\n\n")

def __process_update__(outFile ,appRecords,currentline) :
    applicant=currentline[1].split("/")
    updateAppDetails(appRecords,applicant[0], applicant[1],applicant[2],applicant[3])
    outFile.write("Updated details of "+applicant[0]+". Application Status has been changed.\n\n")

def __process_insertion__(inputFile ,outFile,appRecords) :
    i=0
    for line in inputFile:
        i=i+1
        currentline = line.strip().split("/")
        insertAppDetails(appRecords,currentline[0], currentline[1],currentline[2],currentline[3])
    outFile.write("Successfully inserted "+str(i)+"  applications into the system.\n\n")


if __name__ == "__main__":
    main()

