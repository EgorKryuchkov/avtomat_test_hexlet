'''funny test'''
from testo.capitalize import capitalize

def test_capitalize_basic():
    '''funny test1'''
    assert capitalize('hello') == 'Hello'

def test_capitalize_pogran():
    '''funny test2'''
    assert capitalize('') == ''
