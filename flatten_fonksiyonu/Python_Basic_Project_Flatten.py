# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 11:10:48 2022

@author: Mikail
"""

# 1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı 
# listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:

# input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
# output: [1,'a','cat',2,3,'dog',4,5]


# numbers = [1, 2, 3, 4, 2, 5]]

# inistance fonksiyonun nasılkullanıldığına dair örnekler

# # check if numbers is instance of list
# result = isinstance(numbers, list)
# print(result)

# Output: True

example = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
new_list = []
def flatten(n):
    for i in n:
        if isinstance(i, list):
            flatten(i)
        else:
            new_list.append(i)
flatten(example)
print(new_list)