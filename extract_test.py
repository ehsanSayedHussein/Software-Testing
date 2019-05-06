# -*- coding: utf-8 -*-

from keyword import KeywordProcessor
import pytest


#*****************************************************************Test if (not sentence )***************************************** 
#GACC
def test1_predicate1():
   keyword_processor = KeywordProcessor()
   sentence ='I love Big Apple and Bay Area'
   keyword_processor.keyword_trie_dict = {'b': {'i': {'g': {' ': {'a': {'p': {'p': {'l': {'e': {'_keyword_': 'New York'}}}}}}}}, 'a': {'y': {' ': {'a': {'r': {'e': {'a': {'_keyword_': 'Bay Area'}}}}}}}}}
   keywords_found = keyword_processor.extract_keywords(sentence)
   assert keywords_found ==  ['New York', 'Bay Area']

def test2_predicate1():
   keyword_processor = KeywordProcessor()
   sentence ='My name is Ehsan'
   keyword_processor.keyword_trie_dict = {'b': {'i': {'g': {' ': {'a': {'p': {'p': {'l': {'e': {'_keyword_': 'New York'}}}}}}}}, 'a': {'y': {' ': {'a': {'r': {'e': {'a': {'_keyword_': 'Bay Area'}}}}}}}}}
   keywords_found = keyword_processor.extract_keywords(sentence)
   assert keywords_found ==  []

def test3_predicate1():
   keyword_processor = KeywordProcessor()
   sentence =''
   keyword_processor.keyword_trie_dict = {'b': {'i': {'g': {' ': {'a': {'p': {'p': {'l': {'e': {'_keyword_': 'New York'}}}}}}}}, 'a': {'y': {' ': {'a': {'r': {'e': {'a': {'_keyword_': 'Bay Area'}}}}}}}}}
   keywords_found = keyword_processor.extract_keywords(sentence)
   assert keywords_found ==  []

#*************************************************************Test if (not self.case_sensitive)***********************************************
#CACC


def test1_predicate2():
   keyword_processor = KeywordProcessor(True)
   sentence ='I love Big Apple and Bay Area'
   keyword_processor.keyword_trie_dict = {'b': {'i': {'g': {' ': {'a': {'p': {'p': {'l': {'e': {'_keyword_': 'New York'}}}}}}}}, 'a': {'y': {' ': {'a': {'r': {'e': {'a': {'_keyword_': 'Bay Area'}}}}}}}}}
   keywords_found = keyword_processor.extract_keywords(sentence)
   assert keywords_found ==  []

def test2_predicate2():
   keyword_processor = KeywordProcessor(True)
   sentence ='I love big apple and bay area'
   keyword_processor.keyword_trie_dict = {'b': {'i': {'g': {' ': {'a': {'p': {'p': {'l': {'e': {'_keyword_': 'New York'}}}}}}}}, 'a': {'y': {' ': {'a': {'r': {'e': {'a': {'_keyword_': 'Bay Area'}}}}}}}}}
   keywords_found = keyword_processor.extract_keywords(sentence)
   assert keywords_found ==  ['New York', 'Bay Area']

def test3_predicate2():
   keyword_processor = KeywordProcessor(False)
   sentence ='I love Big Apple and bay Area'
   keyword_processor.keyword_trie_dict = {'b': {'i': {'g': {' ': {'a': {'p': {'p': {'l': {'e': {'_keyword_': 'New York'}}}}}}}}, 'a': {'y': {' ': {'a': {'r': {'e': {'a': {'_keyword_': 'Bay Area'}}}}}}}}}
   keywords_found = keyword_processor.extract_keywords(sentence)
   assert keywords_found ==  ['New York', 'Bay Area']

def test4_predicate2():
   keyword_processor = KeywordProcessor(False)
   sentence ='I love Big Apple and bay area'
   keyword_processor.keyword_trie_dict = {'b': {'i': {'g': {' ': {'a': {'p': {'p': {'l': {'e': {'_keyword_': 'New York'}}}}}}}}, 'a': {'y': {' ': {'a': {'r': {'e': {'a': {'_keyword_': 'Bay Area'}}}}}}}}}
   keywords_found = keyword_processor.extract_keywords(sentence)
   assert keywords_found ==  ['New York', 'Bay Area']


#*************************************************************Test while (idx < sentence_len)***********************************************
#CACC

def test1_predicate3():
   keyword_processor = KeywordProcessor()
   sentence ='I love Big Apple and Bay Area'
   keyword_processor.keyword_trie_dict = {'b': {'i': {'g': {' ': {'a': {'p': {'p': {'l': {'e': {'_keyword_': 'New York'}}}}}}}}, 'a': {'y': {' ': {'a': {'r': {'e': {'a': {'_keyword_': 'Bay Area'}}}}}}}}}
   keywords_found = keyword_processor.extract_keywords(sentence)
   assert keywords_found ==  ['New York', 'Bay Area']

def test2_predicate3():
   keyword_processor = KeywordProcessor()
   sentence ='My name is Ehsan'
   keyword_processor.keyword_trie_dict = {'b': {'i': {'g': {' ': {'a': {'p': {'p': {'l': {'e': {'_keyword_': 'New York'}}}}}}}}, 'a': {'y': {' ': {'a': {'r': {'e': {'a': {'_keyword_': 'Bay Area'}}}}}}}}}
   keywords_found = keyword_processor.extract_keywords(sentence)
   assert keywords_found ==  []

def test3_predicate3():
   keyword_processor = KeywordProcessor()
   sentence =''
   keyword_processor.keyword_trie_dict = {'b': {'i': {'g': {' ': {'a': {'p': {'p': {'l': {'e': {'_keyword_': 'New York'}}}}}}}}, 'a': {'y': {' ': {'a': {'r': {'e': {'a': {'_keyword_': 'Bay Area'}}}}}}}}}
   keywords_found = keyword_processor.extract_keywords(sentence)
   assert keywords_found ==  []
#*************************************************************Test  if (char not in self.non_word_boundaries)*****************************
#GACC


def test1_predicate4():
   keyword_processor = KeywordProcessor()
   sentence ='I love Big Apple and Bay Area'
   keyword_processor.keyword_trie_dict = {'b': {'i': {'g': {' ': {'a': {'p': {'p': {'l': {'e': {'_keyword_': 'New York'}}}}}}}}, 'a': {'y': {' ': {'a': {'r': {'e': {'a': {'_keyword_': 'Bay Area'}}}}}}}}}
   keywords_found = keyword_processor.extract_keywords(sentence)
   assert keywords_found ==  ['New York', 'Bay Area']

def test2_predicate4():
   keyword_processor = KeywordProcessor()
   sentence ='I love Big Apple'
   keyword_processor.keyword_trie_dict = {'b': {'i': {'g': {' ': {'a': {'p': {'p': {'l': {'e': {'_keyword_': 'New York'}}}}}}}}, 'a': {'y': {' ': {'a': {'r': {'e': {'a': {'_keyword_': 'Bay Area'}}}}}}}}}
   keywords_found = keyword_processor.extract_keywords(sentence)
   assert keywords_found ==  ['New York']

def test3_predicate4():
   keyword_processor = KeywordProcessor()
   sentence ='My Name is Ehsan'
   keyword_processor.keyword_trie_dict = {'b': {'i': {'g': {' ': {'a': {'p': {'p': {'l': {'e': {'_keyword_': 'New York'}}}}}}}}, 'a': {'y': {' ': {'a': {'r': {'e': {'a': {'_keyword_': 'Bay Area'}}}}}}}}}
   keywords_found = keyword_processor.extract_keywords(sentence)
   assert keywords_found ==  []

#*************************************************************Test  if (char in current_dict) *********************************************
#GACC

def test1_predicate5():
   keyword_processor = KeywordProcessor()
   sentence ='I love Big Apple and Bay Area'
   keyword_processor.keyword_trie_dict = {'b': {'i': {'g': {' ': {'a': {'p': {'p': {'l': {'e': {'_keyword_': 'New York'}}}}}}}}, 'a': {'y': {' ': {'a': {'r': {'e': {'a': {'_keyword_': 'Bay Area'}}}}}}}}}
   keywords_found = keyword_processor.extract_keywords(sentence)
   assert keywords_found ==  ['New York', 'Bay Area']

def test2_predicate5():
   keyword_processor = KeywordProcessor()
   sentence ='I love Big'
   keyword_processor.keyword_trie_dict = {'b': {'i': {'g': {' ': {'a': {'p': {'p': {'l': {'e': {'_keyword_': 'New York'}}}}}}}}, 'a': {'y': {' ': {'a': {'r': {'e': {'a': {'_keyword_': 'Bay Area'}}}}}}}}}
   keywords_found = keyword_processor.extract_keywords(sentence)
   assert keywords_found ==  []

def test3_predicate5():
   keyword_processor = KeywordProcessor()
   sentence ='My Name is Ehsan'
   keyword_processor.keyword_trie_dict = {'b': {'i': {'g': {' ': {'a': {'p': {'p': {'l': {'e': {'_keyword_': 'New York'}}}}}}}}, 'a': {'y': {' ': {'a': {'r': {'e': {'a': {'_keyword_': 'Bay Area'}}}}}}}}}
   keywords_found = keyword_processor.extract_keywords(sentence)
   assert keywords_found ==  []


#*************************************************************Test  if (self._keyword in current_dict or char in current_dict) **************
#RICC


def test1_predicate6():
   keyword_processor = KeywordProcessor()
   sentence ='I love Big Apple and Bay Area'
   keyword_processor.keyword_trie_dict = {'b': {'i': {'g': {' ': {'a': {'p': {'p': {'l': {'e': {'_keyword_': 'New York'}}}}}}}}, 'a': {'y': {' ': {'a': {'r': {'e': {'a': {'_keyword_': 'Bay Area'}}}}}}}}}
   keywords_found = keyword_processor.extract_keywords(sentence)
   assert keywords_found ==  ['New York', 'Bay Area']

def test2_predicate6():
   keyword_processor = KeywordProcessor()
   sentence ='I love Big Apple'
   keyword_processor.keyword_trie_dict = {'b': {'i': {'g': {' ': {'a': {'p': {'p': {'l': {'e': {'_keyword_': 'New York'}}}}}}}}, 'a': {'y': {' ': {'a': {'r': {'e': {'a': {'_keyword_': 'Bay Area'}}}}}}}}}
   keywords_found = keyword_processor.extract_keywords(sentence)
   assert keywords_found ==  ['New York']


#*************************************************************Test  if (char in current_dict) *************************************************
#CACC

def test1_predicate7():
   keyword_processor = KeywordProcessor()
   sentence ='I love Big Apple and Bay Area'
   keyword_processor.keyword_trie_dict = {'b': {'i': {'g': {' ': {'a': {'p': {'p': {'l': {'e': {'_keyword_': 'New York'}}}}}}}}, 'a': {'y': {' ': {'a': {'r': {'e': {'a': {'_keyword_': 'Bay Area'}}}}}}}}}
   keywords_found = keyword_processor.extract_keywords(sentence)
   assert keywords_found ==  ['New York', 'Bay Area']

def test2_predicate7():
   keyword_processor = KeywordProcessor()
   sentence ='I love Big A'
   keyword_processor.keyword_trie_dict = {'b': {'i': {'g': {' ': {'a': {'p': {'p': {'l': {'e': {'_keyword_': 'New York'}}}}}}}}, 'a': {'y': {' ': {'a': {'r': {'e': {'a': {'_keyword_': 'Bay Area'}}}}}}}}}
   keywords_found = keyword_processor.extract_keywords(sentence)
   assert keywords_found ==  []

def test3_predicate7():
   keyword_processor = KeywordProcessor()
   sentence ='I love Big'
   keyword_processor.keyword_trie_dict = {'b': {'i': {'g': {' ': {'a': {'p': {'p': {'l': {'e': {'_keyword_': 'New York'}}}}}}}}, 'a': {'y': {' ': {'a': {'r': {'e': {'a': {'_keyword_': 'Bay Area'}}}}}}}}}
   keywords_found = keyword_processor.extract_keywords(sentence)
   assert keywords_found ==  []
#*************************************************************Test  while (idy < sentence_len) ************************************************
#GACC

def test1_predicate8():
   keyword_processor = KeywordProcessor()
   sentence ='I love Big Apple and Bay Area'
   keyword_processor.keyword_trie_dict = {'b': {'i': {'g': {' ': {'a': {'p': {'p': {'l': {'e': {'_keyword_': 'New York'}}}}}}}}, 'a': {'y': {' ': {'a': {'r': {'e': {'a': {'_keyword_': 'Bay Area'}}}}}}}}}
   keywords_found = keyword_processor.extract_keywords(sentence)
   assert keywords_found ==  ['New York', 'Bay Area']

def test2_predicate8():
   keyword_processor = KeywordProcessor()
   sentence ='I love Big A'
   keyword_processor.keyword_trie_dict = {'b': {'i': {'g': {' ': {'a': {'p': {'p': {'l': {'e': {'_keyword_': 'New York'}}}}}}}}, 'a': {'y': {' ': {'a': {'r': {'e': {'a': {'_keyword_': 'Bay Area'}}}}}}}}}
   keywords_found = keyword_processor.extract_keywords(sentence)
   assert keywords_found ==  []

def test3_predicate8():
   keyword_processor = KeywordProcessor()
   sentence ='I love Big'
   keyword_processor.keyword_trie_dict = {'b': {'i': {'g': {' ': {'a': {'p': {'p': {'l': {'e': {'_keyword_': 'New York'}}}}}}}}, 'a': {'y': {' ': {'a': {'r': {'e': {'a': {'_keyword_': 'Bay Area'}}}}}}}}}
   keywords_found = keyword_processor.extract_keywords(sentence)
   assert keywords_found ==  []

#**********************************if (inner_char not in self.non_word_boundaries and self._keyword in current_dict_continued:)**************

def test1_predicate9():
   keyword_processor = KeywordProcessor()
   sentence ='I love Big Apple and Bay Area'
   keyword_processor.keyword_trie_dict = {'b': {'i': {'g': {' ': {'a': {'p': {'p': {'l': {'e': {'_keyword_': 'New York'}}}}}}}}, 'a': {'y': {' ': {'a': {'r': {'e': {'a': {'_keyword_': 'Bay Area'}}}}}}}}}
   keywords_found = keyword_processor.extract_keywords(sentence)
   assert keywords_found ==  ['New York', 'Bay Area']

def test2_predicate9():
   keyword_processor = KeywordProcessor()
   sentence ='I love Big A'
   keyword_processor.keyword_trie_dict = {'b': {'i': {'g': {' ': {'a': {'p': {'p': {'l': {'e': {'_keyword_': 'New York'}}}}}}}}, 'a': {'y': {' ': {'a': {'r': {'e': {'a': {'_keyword_': 'Bay Area'}}}}}}}}}
   keywords_found = keyword_processor.extract_keywords(sentence)
   assert keywords_found ==  []

def test3_predicate9():
   keyword_processor = KeywordProcessor()
   sentence ='I love Big.'
   keyword_processor.keyword_trie_dict = {'b': {'i': {'g': {' ': {'a': {'p': {'p': {'l': {'e': {'_keyword_': 'New York'}}}}}}}}, 'a': {'y': {' ': {'a': {'r': {'e': {'a': {'_keyword_': 'Bay Area'}}}}}}}}}
   keywords_found = keyword_processor.extract_keywords(sentence)
   assert keywords_found ==  []


#********************************** if(inner_char in current_dict_continued) ************************************************************
#GACC
def test1_predicate10():
   keyword_processor = KeywordProcessor()
   sentence ='I love Big Apple and Bay Area'
   keyword_processor.keyword_trie_dict = {'b': {'i': {'g': {' ': {'a': {'p': {'p': {'l': {'e': {'_keyword_': 'New York'}}}}}}}}, 'a': {'y': {' ': {'a': {'r': {'e': {'a': {'_keyword_': 'Bay Area'}}}}}}}}}
   keywords_found = keyword_processor.extract_keywords(sentence)
   assert keywords_found ==  ['New York', 'Bay Area']

def test2_predicate10():
   keyword_processor = KeywordProcessor()
   sentence ='I love Big .'
   keyword_processor.keyword_trie_dict = {'b': {'i': {'g': {' ': {'a': {'p': {'p': {'l': {'e': {'_keyword_': 'New York'}}}}}}}}, 'a': {'y': {' ': {'a': {'r': {'e': {'a': {'_keyword_': 'Bay Area'}}}}}}}}}
   keywords_found = keyword_processor.extract_keywords(sentence)
   assert keywords_found ==  []

#********************************** if(is_longer_seq_found) **************************************************************************
#GACC

def test1_predicate11():
   keyword_processor = KeywordProcessor()
   sentence ='I love Big Apple'
   keyword_processor.keyword_trie_dict = {'b': {'i': {'g': {' ': {'a': {'p': {'p': {'l': {'e': {'_keyword_': 'New York'}}}}}}}}, 'a': {'y': {' ': {'a': {'r': {'e': {'a': {'_keyword_': 'Bay Area'}}}}}}}}}
   keywords_found = keyword_processor.extract_keywords(sentence)
   assert keywords_found ==  ['New York']

def test2_predicate11():
   keyword_processor = KeywordProcessor()
   sentence ='Big A'
   keyword_processor.keyword_trie_dict = {'b': {'i': {'g': {' ': {'a': {'p': {'p': {'l': {'e': {'_keyword_': 'New York'}}}}}}}}, 'a': {'y': {' ': {'a': {'r': {'e': {'a': {'_keyword_': 'Bay Area'}}}}}}}}}
   keywords_found = keyword_processor.extract_keywords(sentence)
   assert keywords_found ==  []
#****************************************************  if(self._keyword in current_dict_continued) **********************************
#GICC

def test1_predicate12():
   keyword_processor = KeywordProcessor()
   sentence ='I love Big Apple'
   keyword_processor.keyword_trie_dict = {'b': {'i': {'g': {' ': {'a': {'p': {'p': {'l': {'e': {'_keyword_': 'New York'}}}}}}}}, 'a': {'y': {' ': {'a': {'r': {'e': {'a': {'_keyword_': 'Bay Area'}}}}}}}}}
   keywords_found = keyword_processor.extract_keywords(sentence)
   assert keywords_found ==  ['New York']

def test2_predicate12():
   keyword_processor = KeywordProcessor()
   sentence ='I love Big Apple.'
   keyword_processor.keyword_trie_dict = {'b': {'i': {'g': {' ': {'a': {'p': {'p': {'l': {'e': {'_keyword_': 'New York'}}}}}}}}, 'a': {'y': {' ': {'a': {'r': {'e': {'a': {'_keyword_': 'Bay Area'}}}}}}}}}
   keywords_found = keyword_processor.extract_keywords(sentence)
   assert keywords_found ==  ['New York']
#****************************************************   if(longest_sequence_found) ****************************************************
#GACC

def test1_predicate13():
   keyword_processor = KeywordProcessor()
   sentence ='I love Big Apple'
   keyword_processor.keyword_trie_dict = {'b': {'i': {'g': {' ': {'a': {'p': {'p': {'l': {'e': {'_keyword_': 'New York'}}}}}}}}, 'a': {'y': {' ': {'a': {'r': {'e': {'a': {'_keyword_': 'Bay Area'}}}}}}}}}
   keywords_found = keyword_processor.extract_keywords(sentence)
   assert keywords_found ==  ['New York']

def test2_predicate13():
   keyword_processor = KeywordProcessor()
   sentence ='I love Big'
   keyword_processor.keyword_trie_dict = {'b': {'i': {'g': {' ': {'a': {'p': {'p': {'l': {'e': {'_keyword_': 'New York'}}}}}}}}, 'a': {'y': {' ': {'a': {'r': {'e': {'a': {'_keyword_': 'Bay Area'}}}}}}}}}
   keywords_found = keyword_processor.extract_keywords(sentence)
   assert keywords_found ==  []
#****************************************************  while (idy < sentence_len)*************************************************
#CACC


def test1_predicate14():
   keyword_processor = KeywordProcessor()
   sentence ='I love Big Apple'
   keyword_processor.keyword_trie_dict = {'b': {'i': {'g': {' ': {'a': {'p': {'p': {'l': {'e': {'_keyword_': 'New York'}}}}}}}}, 'a': {'y': {' ': {'a': {'r': {'e': {'a': {'_keyword_': 'Bay Area'}}}}}}}}}
   keywords_found = keyword_processor.extract_keywords(sentence)
   assert keywords_found ==  ['New York']

def test2_predicate14():
   keyword_processor = KeywordProcessor()
   sentence ='I love Big'
   keyword_processor.keyword_trie_dict = {'b': {'i': {'g': {' ': {'a': {'p': {'p': {'l': {'e': {'_keyword_': 'New York'}}}}}}}}, 'a': {'y': {' ': {'a': {'r': {'e': {'a': {'_keyword_': 'Bay Area'}}}}}}}}}
   keywords_found = keyword_processor.extract_keywords(sentence)
   assert keywords_found ==  []

def test3_predicate14():
   keyword_processor = KeywordProcessor()
   sentence ='I love Big A'
   keyword_processor.keyword_trie_dict = {'b': {'i': {'g': {' ': {'a': {'p': {'p': {'l': {'e': {'_keyword_': 'New York'}}}}}}}}, 'a': {'y': {' ': {'a': {'r': {'e': {'a': {'_keyword_': 'Bay Area'}}}}}}}}}
   keywords_found = keyword_processor.extract_keywords(sentence)
   assert keywords_found ==  []

#****************************************************  if ( char not in self.non_word_boundaries ) ***************************************
#GACC


def test1_predicate15():
   keyword_processor = KeywordProcessor()
   sentence ='I love Big Apple'
   keyword_processor.keyword_trie_dict = {'b': {'i': {'g': {' ': {'a': {'p': {'p': {'l': {'e': {'_keyword_': 'New York'}}}}}}}}, 'a': {'y': {' ': {'a': {'r': {'e': {'a': {'_keyword_': 'Bay Area'}}}}}}}}}
   keywords_found = keyword_processor.extract_keywords(sentence)
   assert keywords_found ==  ['New York']

def test2_predicate15():
   keyword_processor = KeywordProcessor()
   sentence ='I love Big'
   keyword_processor.keyword_trie_dict = {'b': {'i': {'g': {' ': {'a': {'p': {'p': {'l': {'e': {'_keyword_': 'New York'}}}}}}}}, 'a': {'y': {' ': {'a': {'r': {'e': {'a': {'_keyword_': 'Bay Area'}}}}}}}}}
   keywords_found = keyword_processor.extract_keywords(sentence)
   assert keywords_found ==  []

def test3_predicate15():
   keyword_processor = KeywordProcessor()
   sentence ='I love Big A'
   keyword_processor.keyword_trie_dict = {'b': {'i': {'g': {' ': {'a': {'p': {'p': {'l': {'e': {'_keyword_': 'New York'}}}}}}}}, 'a': {'y': {' ': {'a': {'r': {'e': {'a': {'_keyword_': 'Bay Area'}}}}}}}}}
   keywords_found = keyword_processor.extract_keywords(sentence)
   assert keywords_found ==  []


#**************************************************** if (idx + 1 >= sentence_len) *******************************************************
#CACC


def test1_predicate16():
   keyword_processor = KeywordProcessor()
   sentence ='B'
   keyword_processor.keyword_trie_dict = {'b': {'i': {'g': {' ': {'a': {'p': {'p': {'l': {'e': {'_keyword_': 'New York'}}}}}}}}, 'a': {'y': {' ': {'a': {'r': {'e': {'a': {'_keyword_': 'Bay Area'}}}}}}}}}
   keywords_found = keyword_processor.extract_keywords(sentence)
   assert keywords_found ==  []

def test2_predicate16():
   keyword_processor = KeywordProcessor()
   sentence ='Big'
   keyword_processor.keyword_trie_dict = {'b': {'i': {'g': {' ': {'a': {'p': {'p': {'l': {'e': {'_keyword_': 'New York'}}}}}}}}, 'a': {'y': {' ': {'a': {'r': {'e': {'a': {'_keyword_': 'Bay Area'}}}}}}}}}
   keywords_found = keyword_processor.extract_keywords(sentence)
   assert keywords_found ==  []


#**************************************************** if (reset_current_dict) ************************************************************
#GACC


def test1_predicate17():
   keyword_processor = KeywordProcessor()
   sentence ='Big Apple'
   keyword_processor.keyword_trie_dict = {'b': {'i': {'g': {' ': {'a': {'p': {'p': {'l': {'e': {'_keyword_': 'New York'}}}}}}}}, 'a': {'y': {' ': {'a': {'r': {'e': {'a': {'_keyword_': 'Bay Area'}}}}}}}}}
   keywords_found = keyword_processor.extract_keywords(sentence)
   assert keywords_found ==  ['New York']

def test2_predicate17():
   keyword_processor = KeywordProcessor()
   sentence ='Big'
   keyword_processor.keyword_trie_dict = {'b': {'i': {'g': {' ': {'a': {'p': {'p': {'l': {'e': {'_keyword_': 'New York'}}}}}}}}, 'a': {'y': {' ': {'a': {'r': {'e': {'a': {'_keyword_': 'Bay Area'}}}}}}}}}
   keywords_found = keyword_processor.extract_keywords(sentence)
   assert keywords_found ==  []


#****************************************************  if (span_info) ***************************************************************
#CACC



def test1_predicate18():
   keyword_processor = KeywordProcessor()
   sentence ='I love Big Apple and Bay Area.'
   keyword_processor.keyword_trie_dict = {'b': {'i': {'g': {' ': {'a': {'p': {'p': {'l': {'e': {'_keyword_': 'New York'}}}}}}}}, 'a': {'y': {' ': {'a': {'r': {'e': {'a': {'_keyword_': 'Bay Area'}}}}}}}}}
   keywords_found = keyword_processor.extract_keywords(sentence , True)
   assert keywords_found ==  ['New York','Bay Area']



def test1_predicate18():
   keyword_processor = KeywordProcessor()
   sentence ='I love Big Apple and Bay Area.'
   keyword_processor.keyword_trie_dict = {'b': {'i': {'g': {' ': {'a': {'p': {'p': {'l': {'e': {'_keyword_': 'New York'}}}}}}}}, 'a': {'y': {' ': {'a': {'r': {'e': {'a': {'_keyword_': 'Bay Area'}}}}}}}}}
   keywords_found = keyword_processor.extract_keywords(sentence)
   assert keywords_found ==  ['New York','Bay Area']

