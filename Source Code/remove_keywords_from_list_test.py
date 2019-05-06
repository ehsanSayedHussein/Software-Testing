# -*- coding: utf-8 -*-

from keyword import KeywordProcessor
import pytest


#*****************************************************************Test  if not isinstance(keyword_list, list) ****************************
#CACC
def test1_predicate1():
   keyword_processor = KeywordProcessor()
   keyword_dict = ["java", "python"]
   keyword_processor.remove_keywords_from_list(keyword_dict)
   assert keyword_processor.keyword_trie_dict ==  {}
'''
def test2_predicate1():
   keyword_processor = KeywordProcessor()
   keyword_dict = "java"
   keyword_processor.remove_keywords_from_dict(keyword_dict)
   assert keyword_processor.keyword_trie_dict ==  {}
'''

#******************************************** Test  (for keyword in keyword_list) ******************* 
#GACC

def test1_predicate2():
   keyword_processor = KeywordProcessor()
   keyword_dict = ["java", "python"]
   keyword_processor.remove_keywords_from_list(keyword_dict)
   assert keyword_processor.keyword_trie_dict ==  {}

def test2_predicate2():
   keyword_processor = KeywordProcessor()
   keyword_dict = []
   keyword_processor.remove_keywords_from_list(keyword_dict)
   assert keyword_processor.keyword_trie_dict ==  {}

