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
        res = [] 
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
            
                res.append(val)
            
        return "Applied: "+str(applied)+ "\n\nVerified : "+str(verified)+"\n\nAproved : "+str(approved)
    
    def destroyHash(self,ApplicationRecords): 
        self.ApplicationRecords
        
        
def main():
    c=ClubHouse()
    c.initializeHash()
    with open("inputPS8.txt", "r") as inputFile:
        with open("outputPS8.txt", "w") as outFile:
            with open("promptsPS8.txt", "r") as promptsFile:
                i=0
                for line in inputFile:
                    i=i+1
                    currentline = line.strip().split("/")
                    c.insertAppDetails(currentline[0], currentline[1],currentline[2],currentline[3])
                outFile.write("Successfully inserted "+str(i)+"  applications into the system.\n\n")
                for line in promptsFile:
                   
                    currentline = line.strip().split(":")
                   
                    if(currentline[0].strip()=="Update"):
                        applicant=currentline[1].split("/")
                        c.updateAppDetails(applicant[0], applicant[1],applicant[2],applicant[3])
                        outFile.write("Updated details of "+applicant[0]+". Application Status has been changed.\n\n")
                      
                    if(currentline[0].strip()=="memberRef") :   
                        outFile.write("---------- Member reference by "+currentline[1]+" ----------\n\n")
                        apps=c.memRef(currentline[1].strip())
                        for val in apps:
                            outFile.write(val.name+" / "+val.phoneNumber+" / " +val.status+"\n\n")
                        outFile.write("-----------------------------------------\n\n")
                        
                    if(currentline[0].strip()=="appStatus"):  
                        outFile.write("-----------Application Status--------------\n\n")
                        outFile.write(c.appStatus()+"\n\n")
                        outFile.write("-------------------------------------------\n\n")
             
                
                
           
    
if __name__ == "__main__":
    main()   
    
         