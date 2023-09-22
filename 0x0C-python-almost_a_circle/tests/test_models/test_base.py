#!/usr/bin/python3


"""
    This script defines the unittests for base.py
"""


import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """
        Test cases for the Base class.
    """

    def setUp(self):
        """
            This method resets the number
            of objects before each test
        """
        Base._Base__nb_objects = 0

    def test_id(self):
        """
            This method tests the id for new instances
        """
        b0 = Base()
        self.assertEqual(b0.id, 1)
        b1 = Base()
        self.assertEqual(b1.id, 2)
        b2 = Base(12)
        self.assertEqual(b2.id, 12)
        b3 = Base(0)
        self.assertEqual(b3.id, 0)
        b4 = Base(927)
        self.assertEqual(b4.id, 927)
        b5 = Base(-5)
        self.assertEqual(b5.id, -5)
        b6 = Base(9)
        self.assertEqual(b6.id, 9)

    def test_type(self):
        """
            This method tests for the type of an instance
        """
        b6 = Base()
        self.assertEqual(type(b6), Base)
        self.assertTrue(isinstance(b6, Base))

    def test_json_string(self):
        """
            This method tests if to_json_string
            produces the correct output.
        """
        r1 = Rectangle(10, 10, 10, 10)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(json_dictionary, '[{"x": 10, "width": 10, "id": 1, "height": 10, "y": 10}]')

    def test_save_to_file(self):
        """
            This method tests if save_to_file
            writes the correct output to a file.
        """
        r1 = Rectangle(10, 10, 10, 10)
        r2 = Rectangle(20, 20, 20, 20)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            contents = file.read()
        expected_output = '[{"x": 10, "width": 10, "id": 1, "height": 10, "y": 10}, {"x": 20, "width": 20, "id": 2, "height": 20, "y": 20}]'
        self.assertEqual(contents, expected_output)

    def test_from_json_string(self):
        """
            This method tests if from_json_string
            produces the correct output.
        """
        json_string = '[{"x": 10, "width": 10, "id": 1, "height": 10, "y": 10}, {"x": 20, "width": 20, "id": 2, "height": 20, "y": 20}]'
        output = Base.from_json_string(json_string)
        expected_output = [{"x": 10, "width": 10, "id": 1, "height": 10, "y": 10}, {"x": 20, "width": 20, "id": 2, "height": 20, "y": 20}]
        self.assertEqual(output, expected_output)

    def test_create(self):
        """
            This method tests that create
            produces the correct output.
        """
        dictionary = {"x": 10, "y": 20, "id": 1, "width": 30, "height": 40}
        r1 = Rectangle.create(**dictionary)
        expected_output = "[Rectangle] (1) 10/20 - 30/40"
        self.assertEqual(str(r1), expected_output)

    def test_load_from_file(self):
        """
            This method tests that load_from_file
            produces the correct output.
        """

        r1 = Rectangle(10, 10, 10, 10)
        r2 = Rectangle(20, 20, 20, 20)
        Rectangle.save_to_file([r1, r2])


if __name__ == "__main__":
    unittest.main()
