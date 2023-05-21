import pytest

from ipv6 import ipv6_expand, ipv6_compress


def test_expand_positive():
    ipv6_address = '2DFA::F'
    expected_result = '2DFA:0000:0000:0000:0000:0000:0000:000F'
    result = ipv6_expand(ipv6_address)
    assert result == expected_result


def test_expand_with_ipv4_address():
    with pytest.raises(Exception):
        ipv6_address = '192.168.0.1'
        ipv6_expand(ipv6_address)


def test_expand_with_prohibited_char():
    with pytest.raises(Exception):
        ipv6_address = '2GFA::F'
        ipv6_expand(ipv6_address)


def test_expand_negative():
    ipv6_address = '::BBBB:2'
    expected_result = '::BBBB:2'
    result = ipv6_expand(ipv6_address)
    assert result != expected_result


def test_expand_not_empty_string():
    ipv6_address = '::BBBB:2'
    expected_result = ''
    result = ipv6_expand(ipv6_address)
    assert result != expected_result


def test_expand_zeros():
    ipv6_address = '::'
    expected_result = '0000:0000:0000:0000:0000:0000:0000:0000'
    result = ipv6_expand(ipv6_address)
    assert result == expected_result


def test_compress_already_compressed():
    ipv6_address = '::BBBB:2'
    expected_result = '::BBBB:2'
    result = ipv6_compress(ipv6_address)
    assert result == expected_result


def test_compress_already_compressed_long():
    ipv6_address = '25CF:3A:6DA:219A:84A:AA1:BBBB:2'
    expected_result = '25CF:3A:6DA:219A:84A:AA1:BBBB:2'
    result = ipv6_compress(ipv6_address)
    assert result == expected_result


def test_compress_negative():
    ipv6_address = '::BBBB:2'
    expected_result = '0000:0000:BBBB:2'
    result = ipv6_compress(ipv6_address)
    assert result != expected_result


def test_compress_not_empty_string():
    ipv6_address = '::BBBB:2'
    expected_result = ''
    result = ipv6_compress(ipv6_address)
    assert result != expected_result


def test_compress_zeros():
    ipv6_address = '::BBBB:2'
    expected_result = ''
    result = ipv6_compress(ipv6_address)
    assert result != expected_result


def test_compress_with_ipv4_address():
    with pytest.raises(Exception):
        ipv6_address = '192.168.0.1'
        ipv6_compress(ipv6_address)


def test_compress_with_prohibited_char():
    with pytest.raises(Exception):
        ipv6_address = '2001:0db8:0001:z2C0:0000:0ab9:C0A8:0103'
        ipv6_compress(ipv6_address)
