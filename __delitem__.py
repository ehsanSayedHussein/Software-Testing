# -*- coding: utf-8 -*-
"""
Created on Wed May  1 23:33:15 2019

@author: Ehsan Sayed
"""

from testing.keyword import KeywordProcessor
import pytest


keyword_processor = None

#*************************************************************** Initialization *************************************************

def setup_module():
    global keyword_processor
    keyword_processor = KeywordProcessor()

#********************************************************************************************************************************


#*****************************************************************Test P = if (keyword)***************************************************************

@pytest.mark.P1
@pytest.mark.parametrize ("keyword , result",
                              [
                                  ('Word2',True ),
                                  ('Word3',False),
                                  (''     ,False)
                              ]
                          )
def test_delete1(keyword,result):
    keyword_processor.keyword_trie_dict = {'w': {'o': {'r': {'d': {'1': {'_keyword_': 'Word1ID'}, '2': {'_keyword_': 'Word2'}}}}}}
    assert keyword_processor.__delitem__(keyword) == result
    
#********************************************************************************************************************************************************************
    
    
    
#*****************************************************************Test P = if (not self.case_sensitive)***************************************************************

@pytest.mark.P2
@pytest.mark.parametrize ("keyword , case_sensitive , result",
                              [
                                  ('Word1', True , False ),
                                  ('word1', True , True  ),
                                  (''     , True , False ),
                                  ('Word1', False, True  ),
                                  ('word1', False, True  ),
                                  (''     , False, False )
                              ]
                          )
def test_delete2(keyword,case_sensitive,result):
    keyword_processor.keyword_trie_dict = {'w': {'o': {'r': {'d': {'1': {'_keyword_': 'Word1ID'}, '2': {'_keyword_': 'Word2'}}}}}}
    keyword_processor.case_sensitive = case_sensitive
    assert keyword_processor.__delitem__(keyword) == result
  
    
#********************************************************************************************************************************************************************    
    

#*****************************************************************Test P = for (letter in keyword)***************************************************************

@pytest.mark.P3
@pytest.mark.parametrize ("keyword , result",
                              [
                                  ('Word2',True ),
                                  ('Word3',False),
                                  (''     ,False)
                              ]
                          )
def test_delete3(keyword,result):
    keyword_processor.keyword_trie_dict = {'w': {'o': {'r': {'d': {'1': {'_keyword_': 'Word1ID'}, '2': {'_keyword_': 'Word2'}}}}}}
    assert keyword_processor.__delitem__(keyword) == result
    
#********************************************************************************************************************************************************************


#*****************************************************************Test P =  if (letter in current_dict)***************************************************************

@pytest.mark.P4
@pytest.mark.parametrize ("keyword , result",
                              [
                                  ('Word2',True ),
                                  ('Word3',False),
                                  ('Here' ,False)
                              ]
                          )
def test_delete4(keyword,result):
    keyword_processor.keyword_trie_dict = {'w': {'o': {'r': {'d': {'1': {'_keyword_': 'Word1ID'}, '2': {'_keyword_': 'Word2'}}}}}}
    assert keyword_processor.__delitem__(keyword) == result
    
#********************************************************************************************************************************************************************
    
    
    
#*****************************************************************Test P = if (current_dict and self._keyword in current_dict)***************************************************************

@pytest.mark.P5
@pytest.mark.parametrize ("keyword , result",
                              [
                                  ('Word3',False)
                              ]
                          )
def test_delete5(keyword,result):
    keyword_processor.keyword_trie_dict = {'w': {'o': {'r': {'d': {'1': {'_keyword_': 'Word1ID'}, '2': {'_keyword_': 'Word2'}}}}}}
    assert keyword_processor.__delitem__(keyword) == result
    
#********************************************************************************************************************************************************************
    
    
#*****************************************************************Test P = for (key_to_remove, dict_pointer in character_trie_list) ***************************************************************

@pytest.mark.P6
@pytest.mark.parametrize ("keyword , result",
                              [
                                  ('Word1',True)
                              ]
                          )
def test_delete6(keyword,result):
    keyword_processor.keyword_trie_dict = {'w': {'o': {'r': {'d': {'1': {'_keyword_': 'Word1ID'}, '2': {'_keyword_': 'Word2'}}}}}}
    assert keyword_processor.__delitem__(keyword) == result
    
#********************************************************************************************************************************************************************
    
#*****************************************************************Test P = if (len(dict_pointer.keys()) == 1) ***************************************************************

@pytest.mark.P7
@pytest.mark.parametrize ("keyword , result",
                              [
                                  ('Word1',True),
                                  ('Word3',False)
                              ]
                          )
def test_delete7(keyword,result):
    keyword_processor.keyword_trie_dict = {'w': {'o': {'r': {'d': {'1': {'_keyword_': 'Word1ID'}, '2': {'_keyword_': 'Word2'}}}}}}
    assert keyword_processor.__delitem__(keyword) == result
    
#********************************************************************************************************************************************************************
    
        