# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 12:50:35 2022

@author: Mikail
"""

# 2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. 
#Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:

# input: [[1, 2], [3, 4], [5, 6, 7]]

# output: [[[7, 6, 5], [4, 3], [2, 1]]

normal = [[1, 2], [3, 4], [5, 6, 7]]

def reverse(lst): 
    new_lst = lst[::-1] 
    for i in range(len(new_lst)):
        new_lst[i]=new_lst[i][::-1]
    return new_lst 

print(reverse(normal))

      