# -*- coding: utf-8 -*-
from Applicant import Applicant
from HashTable import HashTable

class ClubHouse :
   
        
    def initializeHash(self): 
        self.ApplicationRecords=HashTable()
    
    def insertAppDetails(self, name, phone, memRef, status):
             p1 = Applicant(name, phone,memRef,status)
             self.ApplicationRecords.put(p1.name,p1)
             
    def updateAppDetails(self, name, phone, memRef, status):
             p1 = Applicant(name, phone,memRef,status)
             self.ApplicationRecords.put(p1.name,p1)
                     
    def memRef(self, memRefId): 
        
        res = [] 
        for val in self.ApplicationRecords.values(): 
            if val.memberReferenceId== memRefId : 
                res.append(val)
        
        return res
        
    def appStatus(self):
        
        applied=0
        verified=0
        approved=0
        
        for val in self.ApplicationRecords.values():
            if(val.status=="Applied"):
                applied=applied+1
                
            if(val.status=="Verified"):
                verified=verified+1
            if(val.status=="Approved"):
                approved=approved+1
            
            
        return "Applied: "+str(applied)+ "\n\nVerified : "+str(verified)+"\n\nAproved : "+str(approved)
    
    def destroyHash(self): 
        self.ApplicationRecords.clear()
        
        
def main():
    clubHouse=ClubHouse()
    clubHouse.initializeHash()
    with open("inputPS8.txt", "r") as inputFile:
        with open("outputPS8.txt", "w") as outFile:
            with open("promptsPS8.txt", "r") as promptsFile:
    
                __process_insertion__(inputFile ,outFile,clubHouse)
                
                for line in promptsFile:
                   
                    currentline = line.strip().split(":")
                   
                    if(currentline[0].strip()=="Update"):
                        __process_update__(outFile,clubHouse,currentline)
                       
                      
                    if(currentline[0].strip()=="memberRef") :   
                        __process_member_reference__(outFile,clubHouse,currentline)
                        
                    if(currentline[0].strip()=="appStatus"):  
                        __process_app_status__(outFile,clubHouse)
    clubHouse.destroyHash()   
       
           
def __process_member_reference__(outFile ,clubHouse,currentline) :
    outFile.write("---------- Member reference by "+currentline[1]+" ----------\n\n")
    apps=clubHouse.memRef(currentline[1].strip())
    for val in apps:
        outFile.write(val.name+" / "+val.phoneNumber+" / " +val.status+"\n\n")
        outFile.write("-------------------------\n\n")
    
def __process_app_status__(outFile ,clubHouse) :
    outFile.write("-----------Application Status--------------\n\n")
    outFile.write(clubHouse.appStatus()+"\n\n")
    outFile.write("-------------------------\n\n")
    
def __process_update__(outFile ,clubHouse,currentline) :
    applicant=currentline[1].split("/")
    clubHouse.updateAppDetails(applicant[0], applicant[1],applicant[2],applicant[3])
    outFile.write("Updated details of "+applicant[0]+". Application Status has been changed.\n\n")
    
def __process_insertion__(inputFile ,outFile,clubHouse) :
    i=0
    for line in inputFile:
        i=i+1
        currentline = line.strip().split("/")
        clubHouse.insertAppDetails(currentline[0], currentline[1],currentline[2],currentline[3])
    outFile.write("Successfully inserted "+str(i)+"  applications into the system.\n\n") 
    
         
if __name__ == "__main__":
    main()   
    
         