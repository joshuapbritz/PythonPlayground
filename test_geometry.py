import unittest
import geometry


class TestGeometry(unittest.TestCase):
    # Helper Methods
    def create_line_instance(self):
        C1 = (1, 8)
        C2 = (8, 10)
        LINE = geometry.Line(C1, C2)
        return LINE

    def create_cylinder_instance(self):
        return geometry.Cylinder(2, 3)

    def create_cirlce_instance(self):
        return geometry.Circle(100)

    def create_square_instance(self):
        return geometry.Square(200, 300)

    # Tests - Line
    def test_line_create(self):
        LINE = self.create_line_instance()
        self.assertIsInstance(LINE, geometry.Line)

    def test_line_slope(self):
        LINE = self.create_line_instance()
        self.assertEqual(LINE.slope(), 0.29)

    def test_line_distance(self):
        LINE = self.create_line_instance()
        self.assertEqual(LINE.distance(), 7.28)

    # Tests - Cylinder
    def test_cylinder_create(self):
        CY = self.create_cylinder_instance()
        self.assertIsInstance(CY, geometry.Cylinder)

    def test_cylinder_volume(self):
        CY = self.create_cylinder_instance()
        self.assertEqual(CY.volume(), 56.55)

    def test_cylinder_surface_area(self):
        CY = self.create_cylinder_instance()
        self.assertEqual(CY.surface_area(), 94.25)

    # Test - Circle
    def test_circle_instance(self):
        CIRC = self.create_cirlce_instance()
        self.assertIsInstance(CIRC, geometry.Circle)

    def test_circle_circumference(self):
        CIRC = self.create_cirlce_instance()
        self.assertEqual(CIRC.get_circumference(), 628.32)

    def test_circle_area(self):
        CIRC = self.create_cirlce_instance()
        self.assertEqual(CIRC.get_area(), 31415.93)

    def test_circle_diameter(self):
        CIRC = self.create_cirlce_instance()
        self.assertEqual(CIRC.get_diameter(), 200)

    # Test - Square
    def test_square_instance(self):
        SQ = self.create_square_instance()
        self.assertIsInstance(SQ, geometry.Square)

    def test_square_area(self):
        SQ = self.create_square_instance()
        self.assertEqual(SQ.get_area(), 60000)

    def test_square_perimeter(self):
        SQ = self.create_square_instance()
        self.assertEqual(SQ.get_perimeter(), 1000)


if __name__ == '__main__':
    unittest.main()