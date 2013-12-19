"""
Jonathan Reem
Tests for the Places module.
"""

# pylint disable=W0201,F0401
import nose.tools as nt
import commonplace.Places as Places


class Rooms_Test(object):
    "Rooms_Test: Tests the BaseRoom object of "
    def setup(self):
        "Rooms_Test: Sets up the boilerplate info."
        self.name = "Test Room"
        self.description = "Test Description:\n\tThis room is a test room."

    def teardown(self):
        "Rooms_Test: Tears down the test_room between tests."
        self.test_room = None

    def test_init(self):
        "Rooms_Test: Tests the basic __init__ function and inheritance."
        valid_doors = {'right': Places.BaseRoom("Test",
                                                "Test Description",
                                                {})}
        self.test_room = Places.BaseRoom(self.name, self.description,
                                         valid_doors)
        nt.assert_equal(self.test_room.name, self.name)
        nt.assert_equal(self.test_room.description, self.description)
        nt.assert_equal(self.test_room.doors['right'],
                        valid_doors['right'])

    def test_door_typecheck(self):
        "Rooms_Test: Tests the typechecking of the doors attribute."
        invalid_doors = [Places.BaseRoom("Test", "Test Description", {}),
                         Places.BaseRoom("Test", "Test Description", {})]
        try:
            self.test_room = Places.BaseRoom(self.name, self.description,
                                             invalid_doors)
        except TypeError:
            pass
        else:
            raise Exception("door typechecking did not work.")
