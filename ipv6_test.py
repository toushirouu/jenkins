from ipv6 import ipv6_expand, ipv6_compress

def test_expand_positive():
    assert ipv6_expand('::BBBB:2') == '0000:0000:0000:0000:0000:0000:BBBB:0002'

def test_expand_negative():
    assert ipv6_expand('::BBBB:2') != '::BBBB:2'

def test_expand_not_empty_string():
    assert ipv6_expand('::BBBB:2') != ''

def test_expand_zeros():
    assert ipv6_expand('::') == '0000:0000:0000:0000:0000:0000:0000:0000'

def test_compress_already_compressed():
    ipv6_address = '::BBBB:2'
    expected_result = '::BBBB:2'
    result = ipv6_compress(ipv6_address)
    assert result == expected_result

def test_compress_negative():
    assert ipv6_compress('::BBBB:2') != '0000:0000:BBBB:2'

def test_compress_not_empty_string():
    assert ipv6_compress('::BBBB:2') != ''

def test_compress_zeros():
    assert ipv6_compress('::') == '::'