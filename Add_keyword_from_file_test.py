# -*- coding: utf-8 -*-

from keyword import KeywordProcessor
import pytest


#*****************************************************************Test  if not os.path.isfile(keyword_file) *******************************
#CACC
def test1_predicate1():
   keyword_processor = KeywordProcessor()
   file_name ='keywords.txt'
   keyword_processor.add_keyword_from_file(file_name)
   assert keyword_processor.keyword_trie_dict ==  {u'c': {u'+': {u'+': {'_keyword_': u'c++'}}},u'j': {u'a': {u'v': {u'a': {'_keyword_': u'java'}}}},u'p': {u'y': {u't': {u'h': {u'o': {u'n': {'_keyword_': u'python'}}}}}}}

def test2_predicate1():
   keyword_processor = KeywordProcessor()
   file_name ='keywords1.txt'
   keyword_processor.add_keyword_from_file(file_name)
   print(keyword_processor.keyword_trie_dict)
   assert keyword_processor.keyword_trie_dict == {u'p': {u'r': {u'o': {u'd': {u'u': {u'c': {u't': {u' ': {u'm': {u'a': {u'n': {u'a': {u'g': {u'e': {u'm': {u'e': {u'n': {u't': {u' ': {u't': {u'e': {u'c': {u'h': {u'n': {u'i': {u'q': {u'u': {u'e': {u's': {'_keyword_': u'product management'}}}}}}}}}}}, '_keyword_': u'product management'}}}}}}}}}}}}}}}}}}, u'j': {u'a': {u'v': {u'a': {u' ': {u'p': {u'r': {u'o': {u'g': {u'r': {u'a': {u'm': {u'i': {u'n': {u'g': {'_keyword_': u'java'}}}}}}}}}}}, u'_': {u'2': {u'a': {'_keyword_': u'java'}}}}}}}}
'''
def test3_predicate1():
   keyword_processor = KeywordProcessor()
   file_name ='keywords5.txt'
   #keyword_processor.keyword_trie_dict = {'B': {'i': {'g': {' ': {'a': {'p': {'p': {'l': {'e': {'_keyword_': 'New York'}}}}}}}}}
   keyword_processor.add_keyword_from_file(file_name)
   assert keyword_processor.keyword_trie_dict ==  "Invalid file path {}"
'''
#******************************************** Test if ('=>' in line) ************************************************************
#CACC

def test1_predicate2():
   keyword_processor = KeywordProcessor()
   file_name ='keywords.txt'
   keyword_processor.add_keyword_from_file(file_name)
   assert keyword_processor.keyword_trie_dict ==  {u'c': {u'+': {u'+': {'_keyword_': u'c++'}}},u'j': {u'a': {u'v': {u'a': {'_keyword_': u'java'}}}},u'p': {u'y': {u't': {u'h': {u'o': {u'n': {'_keyword_': u'python'}}}}}}}

def test2_predicate2():
   keyword_processor = KeywordProcessor()
   file_name ='keywords1.txt'
   keyword_processor.add_keyword_from_file(file_name)
   print(keyword_processor.keyword_trie_dict)
   assert keyword_processor.keyword_trie_dict == {u'p': {u'r': {u'o': {u'd': {u'u': {u'c': {u't': {u' ': {u'm': {u'a': {u'n': {u'a': {u'g': {u'e': {u'm': {u'e': {u'n': {u't': {u' ': {u't': {u'e': {u'c': {u'h': {u'n': {u'i': {u'q': {u'u': {u'e': {u's': {'_keyword_': u'product management'}}}}}}}}}}}, '_keyword_': u'product management'}}}}}}}}}}}}}}}}}}, u'j': {u'a': {u'v': {u'a': {u' ': {u'p': {u'r': {u'o': {u'g': {u'r': {u'a': {u'm': {u'i': {u'n': {u'g': {'_keyword_': u'java'}}}}}}}}}}}, u'_': {u'2': {u'a': {'_keyword_': u'java'}}}}}}}}

