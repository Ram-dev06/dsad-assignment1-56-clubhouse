#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 10:25:59 2020

@author: bhakumar0
"""

class Applicant :
   def __init__(self, name, phoneNumber,memberReferenceId,status):
    self.name = name.strip()
    self.phoneNumber = phoneNumber.strip()
    self.memberReferenceId=memberReferenceId.strip()
    self.status=status.strip()
    
