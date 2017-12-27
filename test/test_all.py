# Copyright (c) 2014, Ken Bannister
# All rights reserved. 
#  
# Released under the Mozilla Public License 2.0, as published at the link below.
# http://opensource.org/licenses/MPL-2.0
'''
All tests
'''
import logging
import pytest

logging.basicConfig(filename='test.log', level=logging.DEBUG, 
                    format='%(asctime)s %(module)s %(message)s')
log = logging.getLogger(__name__)

def test_home(selenium):
    '''Test home page and contents'''
    selenium.get('http://localhost:5000')
    assert 'Ratnet' in selenium.title

    greeting = selenium.find_element_by_id('greeting')
    assert greeting.text == 'you dirty rat'
