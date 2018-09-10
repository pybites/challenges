#!python3
#test_converter.py

import pytest

from list_to_string import convert_text

def test_convert_text():
    assert convert_text("""julian
                        bob
                        homies""") == 'julian bob homies'
    
