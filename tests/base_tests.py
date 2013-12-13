"""
Jonathan Reem
Unit Tests for commonplace.Base
"""

import nose.tools
import commonplace.Base as Base


class BaseObjTest(object):
    "Tests BaseObj defined in commonplace/Base.py"
    __slots__ = ['name', 'description', 'test_obj']

    def setup(self):
        "Sets up the test object."
        self.name = 'name'
        self.description = 'description:\n\tthis is an object'
        self.test_obj = Base.BaseObj(self.name, self.description)

    def test_init(self):
        "Tests that values were initialized correctly"
        nose.assert_is_equal(self.test_obj.name, self.name)
        nose.assert_is_equal(self.test_obj.description, self.description)

    def test_repr_str(self):
        "Tests the str and repr methods."
        repr_prediction = "'{.name}'\n'{.description}'".format(self)
        str_prediction = "{.name}\n{.description}".format(self)
        nose.assert_is_equal(repr(self.test_obj), repr_prediction)
        nose.assert_is_equal(str(self.test_obj), str_prediction)

    def teardown(self):
        "Tears down the test object."
        self.name = ''
        self.description = ''
        self.test_obj = None
