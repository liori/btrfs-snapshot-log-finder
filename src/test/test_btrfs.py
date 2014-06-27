import pytest

from ..btrfs import parse_list_output


def test_parse_list_output_exists():
    assert parse_list_output


def test_parse_list_output_single_line():
    text = 'ID 2093 gen 3312 top level 5 path temp2/s11'
    
    expected = [(2093, 3312, 'temp2/s11')]
    
    assert list(parse_list_output(text)) == expected


def test_parse_list_output():
    text = '''
ID 2090 gen 3307 top level 5 path temp2/s9
ID 2091 gen 3308 top level 5 path temp2/s10
ID 2093 gen 3312 top level 5 path temp2/s11
ID 2094 gen 3315 top level 5 path temp2/s12
ID 2098 gen 3323 top level 5 path snapshot-tatoeba1-2013-12-01T16:09:00+01:00
ID 2102 gen 3337 top level 5 path snapshot-tatoeba1-2013-12-01T09:44:06+01:00
ID 2112 gen 3363 top level 5 path snapshot-tatoeba1-2013-12-01T02:03:49+01:00
ID 2117 gen 3379 top level 5 path snapshot-tatoeba1-2013-11-30T19:47:43+01:00
    '''.strip()
    
    expected_output = [
        (2090, 3307, 'temp2/s9'),
        (2091, 3308, 'temp2/s10'),
        (2093, 3312, 'temp2/s11'),
        (2094, 3315, 'temp2/s12'),
        (2098, 3323, 'snapshot-tatoeba1-2013-12-01T16:09:00+01:00'),
        (2102, 3337, 'snapshot-tatoeba1-2013-12-01T09:44:06+01:00'),
        (2112, 3363, 'snapshot-tatoeba1-2013-12-01T02:03:49+01:00'),
        (2117, 3379, 'snapshot-tatoeba1-2013-11-30T19:47:43+01:00')
    ]
    
    assert list(parse_list_output(text)) == expected_output
