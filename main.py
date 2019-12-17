#!/usr/bin/env python
# main : Projet arbre
# -*- coding: utf-8 -*-

# This file is part of Projet Arbre with Python3
# See wiki doc for more information
# Copyright (C) CryptoDox <cryptodox@cryptodox.net>
# This program is published under a GPLv2 license

__author__ = "Christophe LEDUC"
__date__ =  "16 decembre 2019"

# import urllib
import urllib.request
import json
import csv
from urllib.request import urlopen, time

# Variables
ListArbres = []
grenobleArbres = []
anneePropre = []
nullDate = []
dataDict = {}
arbres = '_data\\ESP_PUBLIC.IDENTITE_ARBRE.csv'
etoiles = '***************************************************************************************** \n'
# url = 'http://data.metropolegrenoble.fr/ckan/api/action/datastore_search?resource_id=e4dafba3-7fb8-428c-bbac-91e18de333a8&limit=5&q=title:jones'
url = 'http://data.metropolegrenoble.fr/ckan/api/action/datastore_search?resource_id=e4dafba3-7fb8-428c-bbac-91e18de333a8&limit=2'
fileobj = urllib.request.urlopen(url)

# Une petite fonction pour un timer entre les 2 méthodes (locale et distante).
def sleeper(num):
    while True:
        # Try to convert it to a float
        try:
            num = float(num)
        except ValueError:
            continue
 
        # lance la commande time.sleep() et affiche le timestamp de début et de fin.
        print('Programme en pause à: %s' % time.ctime())
        time.sleep(num)
        print('Reprise du programme à: %s\n' % time.ctime())
        return False

# Une petite fonction qui convertit un CSV en liste.
def cvs2List(fichiercsv):
    # Variable
    liste = []

    with open(fichiercsv, newline='', encoding = 'utf-8') as fcsv:
        lecteur = csv.reader(fcsv, delimiter=';')
        for ligne  in lecteur:
            liste.append(ligne)
    fcsv.close()
    return liste

# Une petite fonction qui convertit un CSV en Dict.
def csv2Dict(fichiercsv):

    with open(fichiercsv, newline='', encoding = 'utf-8') as fcsv:
        lecteur = csv.DictReader(fcsv)
        for dico in lecteur:
            print(dico)
    return lecteur

# Une petite fonction qui affiche les cle du Dict.
# et les deux premières lignes
def cle4Dict(fichiercsv):
    
    with open(fichiercsv, newline='', encoding = 'utf-8') as fcsv:
        lecteur = csv.DictReader(fcsv)
        row = lecteur.__next__()
        print (lecteur.fieldnames)
        print (row)
        row = lecteur.__next__()
        print (row)
    return lecteur

# Une petite fonction qui enregistre les années de plantaion dans une liste.
def year2List(fichiercsv):
    # Variable
    liste = []
    
    with open(fichiercsv, newline='', encoding = 'utf-8') as fcsv:
        lecteur = csv.DictReader(fcsv)
        for dico in lecteur:
            liste.append (dico.get('ANNEEDEPLANTATION'))
    return liste

# Fonction qui enlève les valeurs vide de la liste
def cleanList(list2Clean):
    #Variable
    list2Return = []
    n=0

    for i in list2Clean:
        test=''
        test = test+i
        if test !='':
            list2Return.append(i)
        n+=1
    return list2Return

# Convertie une liste de string en liste d'Int
def str_list_to_int_list(str_list):
    # Variable
    n = 0

    while n < len(str_list):
        str_list[n] = int(str_list[n])
        n += 1
    return(str_list)

ListArbres = (fileobj.read())
print (ListArbres)

print(etoiles)

# Une petite pause de 5 seconds...
# On appel la fonction "sleeper" avec 10s en paramètre, équivalent à : "time.sleep(10)"
sleeper(3)

print(etoiles)

greArbres = cvs2List(arbres)

# 2 premières lignes
print('2 premières lignes \n')
print(greArbres[:2])

print(etoiles)

# dataDict = csv2Dict(arbres)

dataDict = cle4Dict(arbres)

print(etoiles)

anneePlant = year2List(arbres)

# print(anneePlant)

print(etoiles)

print("50 premières années: \n", (anneePlant[:50]))

print(etoiles)

# Methode standard pour une plage dans une liste (les 50 derniers)
print ('Methode standard pour une plage dans une liste (les 50 derniers)')
print("50 dernières années: \n", (anneePlant[len(anneePlant)-50:len(anneePlant)]))

print(etoiles)

# Autre methode (les 50 derniers)
print('Autre methode (les 50 derniers) \n')
print("50 dernières années: \n", (anneePlant[-50:]))

print(etoiles)

# Nb arbres sans date de plantation
nullDate = lambda anneePlant: [i for i, elem in enumerate(anneePlant) if elem==""]
print('Nb arbres sans date de plantation: \n')
print (len(nullDate(anneePlant)))

print(etoiles)

# Autre méthode plus simple
print('Autre méthode plus simple: \n')
print(anneePlant.count(''))

print(etoiles)

# Combien d’arbres
print('Combien d’arbres: \n')
nbArbres = ((len(greArbres))-1)
print(nbArbres)

print(etoiles)
# moyenne d’arbres ont été plantés en chaque année
print('moyenne d’arbres ont été plantés en chaque année: \n')

# print(anneePlant)
anneePropre = cleanList(anneePlant)
plage = str_list_to_int_list(anneePropre)
# print(anneePlant)
# plage = list(map (int, greArbres))
plusVieux = ((sorted(plage))[:1])
plusJeune = ((sorted(plage))[-1:])
a = int(max(plage))
b = int(min(plage))
print('Plus jeunne arbre planté: ', plusJeune)
print('Plus vieille arbre planté: ', plusVieux)
# print(type(plusJeune))
periode = a-b
moyenneNbArbesP = nbArbres/periode
print('Moyenne d\'arbre par an, planté sur ', periode, ' années: ', moyenneNbArbesP)
