#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 22:55:39 2019

@author: maxence
"""
from PIL import Image
import numpy as np



import os
weirdFichier = ['.directory', '.DS_Store']
doss= ['/test_set/','/training_set/']
dos=doss[1]

for i in range (0,20):
    listeFichiers = []
    fichiers = os.listdir('dtd/images')
    fichier = fichiers[np.random.randint(0,len(fichiers))] 
    
    if(fichier in weirdFichier):
        break;
    else:
        
        images = os.listdir('dtd/images/'+ fichier)
        image = images[np.random.randint(0,len(images))] 
        
    if(image in weirdFichier):
        break;
    else:
    

        cartes = os.listdir('predata/')
        carte = cartes[np.random.randint(0,len(cartes))] 

        if(carte in weirdFichier):
            break;
        else:
            
            im1 = Image.open('dtd/images/' + fichier +'/' + image )
            im2 = Image.open("predata/" + carte)
           
            #(np.random.rand(0,im1.size[0]),np.random.rand(0,im1.size[1]))
            x= np.random.randint(im1.size[0]/6,im1.size[0]-im1.size[0]/6)
            y = np.random.randint(im1.size[1]/6,im1.size[1]-im1.size[1]/6)
            xt= np.random.randint(im1.size[1]/6,im1.size[0]/2)
            #rot = np.random.randint(0,45)
            #im2 = im2.rotate(rot, fillcolor='white')
            im2 = im2.resize((xt,xt),Image.ANTIALIAS)
            im1.paste(im2, (x,y))
            nombre = ['1','2','3','4','5','6','7','8','9']
            
            print()
            
            if(str(carte[1])!="_"):
                if(str(carte[1])=="0"):
                    if(str(carte[:2])=="20"):
                        cheminDossierCarte = str(carte[:2])+'_A' 
                    else:
                        cheminDossierCarte = str(carte[:2]) 
                elif(carte[1] in nombre):
                  cheminDossierCarte = str(carte[:2]) +'_A' 
                else:
                   cheminDossierCarte = str(carte[0])
                     
            else:
                 cheminDossierCarte = str(carte[0])+'_A'
            
            
            
            setData = os.listdir("dataset"+dos+cheminDossierCarte)
            im1.save("dataset"+dos+cheminDossierCarte+"/"+ cheminDossierCarte+'_'+str(len(setData)+1)+".png")
                
            print("save in: " +"dataset"+dos+str(carte[0])+"/"+ str(carte[0])+'_'+str(len(setData)+1)+".png")
            
