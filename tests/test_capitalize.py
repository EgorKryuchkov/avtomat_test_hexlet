from testo.capitalize import capitalize

def test_capitalize_basic():
    assert capitalize('hello') == 'Hello'

def test_capitalize_pogran():
    assert capitalize('') == ''
