from pysastra.Tokenizer import Tokenizer
import unittest

def test_space_tokenize():
    text = "Ibu membeli bola"
    st = Tokenizer() 
    result = st.tokenize(text)
    assert len(result) == 3

 
def test_space_2_tokenize():
    text = "Ibu membeli bola 2.5 kg"
    st = Tokenizer() 
    result = st.tokenize(text)
    assert len(result) == 5
