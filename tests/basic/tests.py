from django.test import TestCase

from models import Number
from django.db.models import F

class SimpleTest(TestCase):
    def setUp(self):
        Number.objects.create(x=2,y=3)
    
    def test_basic_addition(self):
        number = Number.objects.calculate(z=F('x')+F('y'))[0]
        self.assertEqual(number.z, 5)
        self.assertEqual(number.x, 2)
        self.assertEqual(number.y, 3)
        
    
    def test_basic_sub(self):
        number = Number.objects.calculate(z=F('x')-F('y'))[0]
        self.assertEqual(number.z, -1)
        self.assertEqual(number.x, 2)
        self.assertEqual(number.y, 3)
        
    
    def test_basic_mult(self):
        number = Number.objects.calculate(z=F('x')*F('y'))[0]
        self.assertEqual(number.z, 6)
        self.assertEqual(number.x, 2)
        self.assertEqual(number.y, 3)
        
    
    def test_basic_div(self):
        number = Number.objects.calculate(z=F('x')/F('y'))[0]
        self.assertEqual(number.z, 2.0/3)
        self.assertEqual(number.x, 2)
        self.assertEqual(number.y, 3)
        
    
class Chaining(TestCase):
    def setUp(self):
        Number.objects.create(x=2,y=3)
    
    def test_square_addition(self):
        number = Number.objects.calculate(z=F('x')+F('y'))
        number = number.calculate(z_squared=F('z')*F('z'))[0]
        self.assertEqual(number.z_squared, 25)
        self.assertEqual(number.z, 5)
        self.assertEqual(number.x, 2)
        self.assertEqual(number.y, 3)
    
    def test_square_mult(self):
        number = Number.objects.calculate(z=F('x')*F('y'))
        number = number.calculate(z_squared=F('z')*F('z'))[0]
        self.assertEqual(number.z_squared, 36)
        self.assertEqual(number.z, 6)
        self.assertEqual(number.x, 2)
        self.assertEqual(number.y, 3)
    
