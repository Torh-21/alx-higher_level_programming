#!/usr/bin/python3


"""
    This script contains the unittests for the
    Rectangle class
"""


import unittests
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
        This class defines the unittest cases
        for the Rectangle class
    """

    def test_valid_input(self):
        """
            This method tests the case
            when valid inputs are passed
        """
        r = Rectangle(10, 20)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertEqual(r.id, 1)

    def test_invalid_width(self):
        """
            This method tests the case when
            an invalid width is passed
        """
        with self.assertRaises(ValueError):
            r = Rectangle(-10, 20)

    def test_invalid_height(self):
        """
            This method tests the case when
            an invalid height is passed
        """
        with self.assertRaises(ValueError):
            r = Rectangle(10, -20)

    def test_invalid_x(self):
        """
            This method tests the case when
            an invalid x value is passed
        """
        with self.assertRaises(ValueError):
            r = Rectangle(10, 20, -5)

    def test_invalid_y(self):
        """
            This method tests the case when
            an invalid y value is passed
        """
        with self.assertRaises(ValueError):
            r = Rectangle(10, 20, 5, -10)

    def test_area(self):
        """
            This method tests the area method
        """
        r = Rectangle(10, 20)
        self.assertEqual(r.area(), 200)

    def test_display(self):
        """
            This method tests the display method
        """
        r = Rectangle(3, 2)
        expected_output = "###\n###\n"
        with self.assertLogs() as cm:
            r.display()
        self.assertEqual(cm.output, [expected_output])

    def test_update(self):
        """
            This method tests the update method
        """
        r = Rectangle(10, 20)
        r.update(2, 5, 6)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 6)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_str(self):
        """
            This method tests the str method
        """
        r = Rectangle(10, 20, 5, 6, 7)
        expected_output = "[Rectangle] (7) 5/6 - 10/20"
        self.assertEqual(str(r), expected_output)

if __name__ == "__main__":
    unittest.main()
