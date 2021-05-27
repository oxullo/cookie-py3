#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (C) {% now 'local', '%Y' %} Archimedes Exhibitions GmbH,
# Saarbrücker Str. 24, Berlin, Germany
#
# This file contains proprietary source code and confidential
# information. Its contents may not be disclosed or distributed to
# third parties unless prior specific permission by Archimedes
# Exhibitions GmbH, Berlin, Germany is obtained in writing. This applies
# to copies made in any form and using any medium. It applies to
# partial as well as complete copies.

"""Tests for {{ cookiecutter.package_name }} package."""

{% if cookiecutter.use_pytest == 'y' -%}
import pytest
{% else %}
import unittest
{%- endif %}

from {{ cookiecutter.package_name }} import {{ cookiecutter.package_name }}


{%- if cookiecutter.use_pytest == 'y' %}

@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """

def test_foobar(response):
    """Sample pytest test function with the pytest fixture as an argument."""

{%- else %}

class Test{{ cookiecutter.package_name|title }}(unittest.TestCase):
    """Tests for `{{ cookiecutter.package_name }}` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_foobar(self):
        """Test something."""
{%- endif %}
