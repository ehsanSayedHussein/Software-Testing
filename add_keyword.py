from SourceCode.keyword import KeywordProcessor
import pytest


#*************************************************************** Initialization *************************************************
def setup_module():
    global keyword_processor
    keyword_processor = KeywordProcessor()
#********************************************************************************************************************************


#*****************************************************************add keyword node coverage***************************************** 

@pytest.mark.Test1Case1
@pytest.mark.parametrize ("keyword , result",
                              [
                                  ('Menna',{'m': {'e': {'n': {'n': {'a': {'_keyword_': 'Menna'}}}}}})
                              ]
                          )
def test1_Case1(keyword,result):
   keyword_processor.add_keyword(keyword)
   assert keyword_processor.keyword_trie_dict == result
   
#******************************************************************************************************************************** 


#*****************************************************************add keyword branch coverage***************************************** 

@pytest.mark.Test2Case1
def test2_Case1():
   keyword_processor = KeywordProcessor(True)
   keyword_processor.add_keyword('Menna')
   keyword_processor.add_keyword('Menna', 'Morsi')
   assert keyword_processor.keyword_trie_dict ==  {'M': {'e': {'n': {'n': {'a': {'_keyword_': 'Morsi'}}}}}}
   
@pytest.mark.Test2Case2
def test2_Case2():
   keyword_processor.add_keyword('Menna')
   assert keyword_processor.keyword_trie_dict == {'m': {'e': {'n': {'n': {'a': {'_keyword_': 'Menna'}}}}}}
   
@pytest.mark.Test2Case3
def test2_Case3():
    keyword_processor = KeywordProcessor()
    keyword_processor.add_keyword('')
    assert keyword_processor.keyword_trie_dict == {}
   
#******************************************************************************************************************************** 

