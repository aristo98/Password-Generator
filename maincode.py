# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 13:48:00 2022

@author: arist
"""
from string import ascii_lowercase, ascii_uppercase
from random import choice

class Password_Generator:
    def __init__(self, para, length):
        special_char="´&<>"+"’"+"'*@\{}[]^¢«»©†°"+"÷$.–=€!`≤≥\"×≠#()%π|"+"+±?®§/~™_"
        self.password_set=[list(ascii_lowercase), list(ascii_uppercase), list(i for i in range(10)),list(i for i in special_char)]
        self.para=para
        self.length=length

    def generate_pass(self):
        ps,password_subset="",[]
        for i in self.para:
            password_subset+=self.password_set[int(i)]
        for j in range(self.length):
            ps+=str(choice(password_subset))
        return ps
    

    