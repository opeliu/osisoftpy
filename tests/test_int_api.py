# -*- coding: utf-8 -*-

#    Copyright 2017 DST Controls
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
"""
osisoftpy.tests.test_int_api.py
~~~~~~~~~~~~
Some blah blah about what this file is for...
"""
import pytest
import requests

import osisoftpy
from osisoftpy.webapi import PIWebAPI

test = type('Test', (object,), {})()
test.url = 'https://sbb03.eecs.berkeley.edu/piwebapi'
test.authtype = 'basic'
test.username = 'albertxu'
test.password = 'Welcome2pi'


def test_get_webapi_without_url():
    with pytest.raises(TypeError) as e:
        osisoftpy.json()
    e.match('url')


def test_get_webapi_with_invalid_url():
    with pytest.raises(requests.exceptions.MissingSchema) as e:
        osisoftpy.json('foobar')
    e.match('Invalid URL')


def test_get_webapi_with_valid_url_no_credentials():
    r = osisoftpy.json(test.url)
    assert r.status_code == requests.codes.unauthorized


def test_get_webapi_valid_url_basic_missing_credentials():
    r = osisoftpy.json(test.url, authtype=test.authtype)
    assert r.status_code == requests.codes.unauthorized


def test_get_webapi_valid_url_basic_missing_password():
    r = osisoftpy.json(test.url, authtype=test.authtype,
                         username=test.username)
    assert r.status_code == requests.codes.unauthorized


def test_get_webapi_valid_url_basic_missing_username():
    r = osisoftpy.json(test.url, authtype=test.authtype,
                         password=test.password)
    assert r.status_code == requests.codes.unauthorized


def test_get_webapi_valid_url_basic_valid_credentials():
    r = osisoftpy.json(test.url, authtype=test.authtype,
                         username=test.username,
                         password=test.password)
    assert r.status_code == requests.codes.ok
    assert r.json().get('Links').get('Self').startswith(test.url)