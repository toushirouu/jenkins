from ipv6 import ipv6_expand

def test_expand_positive():
    assert ipv6_expand('::BBBB:2') == '0000:0000:0000:0000:0000:0000:BBBB:0002'

def test_expand_negative():
    assert ipv6_expand('::BBBB:2') == '::BBBB:2'

def test_expand_not_empty_string():
    assert ipv6_expand('::BBBB:2') != ''

def test_expand_zeros():
    assert ipv6_expand('::') == '0000:0000:0000:0000:0000:0000:0000:0000'

