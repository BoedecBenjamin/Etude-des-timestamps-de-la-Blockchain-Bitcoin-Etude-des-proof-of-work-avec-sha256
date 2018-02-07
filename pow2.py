# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 12:25:15 2018

@author: benja
"""

import hashlib
import time
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
timeelapsed= []


max_nonce = 4294967296 # 4 billion

header = "La phrase que l'on veut"
difficulty_bits = 24

def proof_of_work(header, difficulty_bits):
   
   target = 2 ** (256-difficulty_bits)
   
   
   for nonce in range(1,max_nonce):
       
       
       headernonce = str(header)+str(nonce)
       hash_result = hashlib.sha256(headernonce.encode("UTF-8"))
       
      # hash_result =hash_result.update(headernonce.encode("UTF-8"))
       hash_result =hash_result.hexdigest()
       if int(hash_result,16) < target:
           print("Success with nonce %d" % nonce)
           print("Hash is %s" % hash_result)	
           return (hash_result, nonce)
   print("Failed after %d (max_nonce) tries" % nonce)
   return nonce

if __name__ == '__main__':
    nonce = 0
    hash_result = ''
    
    for i in range(0,30): #On fait tourner 30 fois l'algo pour avoir un meilleur échantillon d'étude.
    #Bien que 30 n'est pas un nombre suffisant d'itération, on s'en contentera puisque cela prend déja 20-30 minutes
        for difficulty_bits in range(25):
            difficulty = 2 ** difficulty_bits
            print("")
            print("Difficulty: %ld (%d bits)" % (difficulty, difficulty_bits))
            print("Starting search...")
            start_time = time.time()
            new_block = 'test block with transactions' + hash_result
            (hash_result, nonce) = proof_of_work(new_block, difficulty_bits)
            end_time = time.time()
            elapsed_time = end_time - start_time
            timeelapsed.append(elapsed_time)
            print("Elapsed time: %.4f seconds" % elapsed_time)
            print("i : %d" %i)
            #print(timeelapsed)
            if elapsed_time > 0:
                hash_power = float(int(nonce)/elapsed_time)
                print("Hashing power: %ld hashes per second" % hash_power)
                

#On fait tourner l'algorithme de proof of work puis on recupere les différents temps 
#écoulés pour chaque difficulté             
def getDifficultyTime(difficulty):
    ListTime=[]
    j=0
    for j in range(difficulty-1,len(timeelapsed),25):
        ListTime.append(timeelapsed[j])  
    mean= np.mean(ListTime)
    return mean

#On sort la liste des moyennes de temps  écoulés pour chaque difficulté  
ListMean=[]
for i in range(1,26):
    ListMean.append(getDifficultyTime(i))

#Graph du temps écoulé en fonction de la difficulté
plt.plot(ListMean)
plt.xlabel("Difficulty")
plt.ylabel("Time to solve")





            
        
        