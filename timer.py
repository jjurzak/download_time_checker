# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 22:52:45 2020

@author: satheek
"""
print("-----------------------------------------------------------------------")

print("Czesc! Mam za zadanie obliczyc czas w ktorym pobierze sie twoj program \n W tym celu bede potrzebowac danych. \n Podaj mi predkosc pobierania i wielkosc pliku!")

print("-----------------------------------------------------------------------")

def inputDownload(message):
    while True:
        try:
            inputDown = float(input(message))
        except ValueError:
            print("To nie jest liczba, wprowadz poprawne dane")
            continue
        else:
            return inputDown
            
    
def inputSize(message):
    while True:
        try:
            inputSiz = int(input(message))
        except ValueError:
            print("To nie jest poprawna wartosc, wprowadz poprawne dane")
            continue
        else:
            return inputSiz
            
        

Down = inputDownload("Podaj predkosc pobierania *w Mb/s* : ")

Size = inputSize("Podaj wielkosc twojego pliku *W Megabajtach* : ")

Result = Size / Down

EndResult = Result 

print("Twoj plik pobierze sie w: ", EndResult, "sekund")

