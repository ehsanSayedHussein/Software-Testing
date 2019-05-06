# -*- coding: utf-8 -*-

from keyword import KeywordProcessor
import pytest


#*****************************************************************Test for (clean_name, keywords in keyword_dict.items)
#GACC
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
   keyword_dict = {"java": ["java_2e", "java programing"],"product management": ["PM", "product manager"]}
   keyword_processor.remove_keywords_from_dict(keyword_dict)
   assert keyword_processor.keyword_trie_dict ==  {}

def test2_predicate2():
   keyword_processor = KeywordProcessor()
   keyword_dict = {}
   keyword_processor.remove_keywords_from_dict(keyword_dict)
   assert keyword_processor.keyword_trie_dict ==  {}


#******************************************** Test  if (not isinstance(keywords, list)) ******************* 
#GACC

def test1_predicate3():
   keyword_processor = KeywordProcessor()
   keyword_dict = {"java": ["java_2e", "java programing"],"product management": ["PM", "product manager"]}
   keyword_processor.remove_keywords_from_dict(keyword_dict)
   assert keyword_processor.keyword_trie_dict ==  {}
'''
def test2_predicate2():
   keyword_processor = KeywordProcessor()
   keyword_dict =  {"java": "java_2e","product management": ["PM", "product manager"]}
   keyword_processor.remove_keywords_from_dict(keyword_dict)
   assert keyword_processor.keyword_trie_dict ==  {}
'''
#******************************************** Test for (keyword in keywords) ******************* 
#GACC

def test1_predicate4():
   keyword_processor = KeywordProcessor()
   keyword_dict = {"java": ["java_2e", "java programing"],"product management": ["PM", "product manager"]}
   keyword_processor.remove_keywords_from_dict(keyword_dict)
   assert keyword_processor.keyword_trie_dict ==  {}

def test2_predicate4():
   keyword_processor = KeywordProcessor()
   keyword_dict = {}
   keyword_processor.remove_keywords_from_dict(keyword_dict)
   assert keyword_processor.keyword_trie_dict ==  {}


