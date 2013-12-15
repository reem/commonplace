"""
Jonathan Reem
Unit Tests for commonplace.Base
"""

import nose.tools as nt
import commonplace.Base as Base


class BaseObj_Test(object):
    "BaseObj_Test: Tests BaseObj defined in commonplace/Base.py"
    def setup(self):
        "BaseObj_Test: Sets up the test object."
        self.name = 'name'
        self.description = 'description:\n\tthis is an object'
        self.test_obj = Base.BaseObj(self.name, self.description)

    def test_init(self):
        "BaseObj_Test: Tests that values were initialized correctly"
        nt.assert_equal(self.test_obj.name, self.name)
        nt.assert_equal(self.test_obj.description, self.description)

    def test_str(self):
        "BaseObj_Test: Tests the str method."
        str_prediction = "{0.name}\n{0.description}".format(self)
        nt.assert_equal(str(self.test_obj), str_prediction)

    def teardown(self):
        "BaseObj_Test: Tears down the test object."
        self.name = ''
        self.description = ''
        self.test_obj = None
