# -*- coding: utf-8 -*-
"""
Created on Wed May  8 15:11:45 2019

@author: Ehsan Sayed
"""


from SourceCode.keyword import KeywordProcessor
import pytest


#*************************************************************** Initialization *************************************************
def setup_module():
    global keyword_processor
    keyword_processor = KeywordProcessor()
#********************************************************************************************************************************


#*****************************************************************Get all keyword node coverage & Branch coverage***************************************** 

@pytest.mark.Test3Case1
def test3_Case1():
   keyword_processor.keyword_trie_dict = {'m': {'_keyword_': 'N'}}
   assert keyword_processor.get_all_keywords() ==  {'m': 'N'}
   
#******************************************************************************************************************************** 



#*****************************************************************Get keyword***************************************** *********

@pytest.mark.Test4Case1
def test4_Case1():
   keyword_processor.keyword_trie_dict = {'m': {'_keyword_': 'N'}}
   assert keyword_processor.get_keyword('M') ==  'N'
   
   
@pytest.mark.Test4Case2
def test4_Case2():
   keyword_processor = KeywordProcessor(True)
   assert keyword_processor.get_keyword('M') ==  None
   
#******************************************************************************************************************************** 

