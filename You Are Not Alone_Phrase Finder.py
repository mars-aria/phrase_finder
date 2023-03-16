#!/usr/bin/env python
# coding: utf-8

# # 'You are not alone' Phrase Finder 🔍

# My phrase_finder() function searches for a self-identifying phrase in each of the 4 large classic texts below.

# Standpoint: "So Matilda’s strong young mind continued to grow, nurtured by the voices of all those authors who had sent their books out into the world like ships on the sea. These books gave Matilda a hopeful and comforting message: You are not alone.” ~ from Matilda by Roald Dahl

# In[1036]:

source = open('408-0.txt', encoding= 'utf-8')
souls = source.read()
source.close()
print(souls[0:1000])

# In[1037]:

import re

# In[1301]:

souls_dict = re.findall(r'black woman', souls)

# In[1302]:

souls_dict

# In[1303]:

len(souls_dict)

# In[1304]:

phrase = ''.join(souls)

# In[1305]:

def phrase_finder(phrase):
    if phrase in souls_dict:
        result = 'You are a ' + phrase + '.'
        return result
    elif phrase not in souls_dict:
        return 'Phrase not found, but you are not alone. 🤗'

# In[1306]:

phrase_finder('black woman')

# In[1307]:

phrase_finder('weary soul')

# In[1259]:

source = open('1260-0.txt', encoding= 'utf-8')
jane = source.read()
source.close()
print(jane[0:1000])

# In[1260]:

import re

# In[1378]:

jane_dict = re.findall(r'frantic bird', jane)

# In[1379]:

len(jane_dict)

# In[1370]:

jane_dict

# In[1371]:

phrase = ''.join(jane)

# In[1372]:

def phrase_finder(phrase):
    if phrase in jane_dict:
        result = 'You are a ' + phrase + '.'
        return result
    elif phrase not in jane_dict:
        return 'Phrase not found, but you are not alone. 🤗'

# In[1375]:

phrase_finder('frantic bird')

# In[1380]:

phrase_finder('rare jewel')

# In[1381]:

source = open('43-0.txt', encoding= 'utf-8')
jekyll = source.read()
source.close()
print(jekyll[0:1000])

# In[1382]:

import re

# In[1396]:

jekyll_dict = re.findall(r'beloved daydream', jekyll)

# In[1397]:

len(jekyll_dict)

# In[1398]:

jekyll_dict

# In[1399]:

phrase = ''.join(jekyll)

# In[1400]:

def phrase_finder(phrase):
    if phrase in jekyll_dict:
        result = 'You are a ' + phrase + '.'
        return result
    elif phrase not in frankenstein_dict:
        return 'Phrase not found, but you are not alone. 🤗'

# In[1401]:

phrase_finder('beloved daydream')

# In[1402]:

phrase_finder('weirdo')

# In[1403]:

source = open('84-0.txt', encoding= 'utf-8')
frankenstein = source.read()
source.close()
print(frankenstein[0:1000])

# In[1404]:

import re

# In[1426]:

frankenstein_dict = re.findall(r'fallen angel', frankenstein)

# In[1427]:

len(frankenstein_dict)

# In[1428]:

phrase = ''.join(frankenstein)

# In[1429]:

def phrase_finder(phrase):
    if phrase in frankenstein_dict:
        result = 'You are a ' + phrase + '.'
        return result
    elif phrase not in frankenstein_dict:
        return 'Phrase not found, but you are not alone. 🤗'

# In[1430]:

phrase_finder('fallen angel')

# In[1432]:

phrase_finder('secret wonder')
