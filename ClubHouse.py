# -*- coding: utf-8 -*-
from Applicant import Applicant
from HashTables import HashTable
from Status import Status

p1 = Applicant("Bhavesh", "9619655828","ref1",Status.Applied)
p2 = Applicant("Kumar bhavesh", "9619655828","ref1",Status.Applied)
p3 = Applicant("Bhavesh1", "9619655828","ref1",Status.Applied)
p4 = Applicant("Kumar1 bhavesh", "9619655828","ref1",Status.Applied)

h1=HashTable()

h1.put(p1.name,p1)

h1.put(p2.name,p2)
h1.put(p3.name,p3)

h1.put(p4.name,p4)

print("Get Value >>>>>>")

print("Key Doesnt exist ", h1.get("abc"))
print(h1.get("Bhavesh").phoneNumber)

print(h1.keys())
print(h1.values())
print("Exit *** ")

def initializeHash(self): 
    self.ApplicationRecords=HashTable()

def insertAppDetails(self,ApplicationRecords, name, phone, memRef, status):
         p1 = Applicant(name, phone,memRef,status)
         self.ApplicationRecords.put(p1.name,p1)
         
def updateAppDetails(self,ApplicationRecords, name, phone, memRef, status):
         p1 = Applicant(name, phone,memRef,status)
         self.ApplicationRecords.put(p1.name,p1)
                 
def memRef(self,ApplicationRecords, memID): 
    return
def appStatus(self,ApplicationRecords):
    return

def destroyHash(self,ApplicationRecords): 
    self.ApplicationRecords
    
         