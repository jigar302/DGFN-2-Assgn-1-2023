'''
JIGAR HUNDAL
STUDENT ID: 100891267
TPRG 2131 Fall 2023 Assignment 1
OCTOBER 15, 2023
Phil J <philip.jarvis@durhamcollege>


This file is to be the test_A_V_calc.py file to be used with your A_V_calc.py and pytest.
This must test each of your Area/Volume functions, with a least 3 examples for each of the
5 functions your chose to use.

As this stands it will NOT work with your A_V_calc.py file.
'''

import A_V_calc  # Import your  class

def test_calculate_area_rectangle(): # Test for area of rectangle
    assert A_V_calc.calculate_area_of_rectangle(4,5) == 20.0
    assert A_V_calc.calculate_area_of_rectangle(3,7) == 21.0
    
def test_calculate_area_square(): #Test for area of square
    assert A_V_calc.calculate_area_of_square(3) == 9.0
    assert A_V_calc.calculate_area_of_square(7) == 49.0
    
def test_calculate_area_of_parallelogram(): #Test for value of parallelogram
    assert A_V_calc.calculate_area_of_parallelogram(1,4) == 4.0
    assert A_V_calc.calculate_area_of_parallelogram(3,6) == 18.0
    
def test_volume_of_cube(): #Test for volume of cube
    assert A_V_calc.calculate_volume_of_cube(4) == 64.0
    assert A_V_calc.calculate_volume_of_cube(3) == 27.0
    
def test_volume_of_cuboid(): #Test for volume of cuboid
    assert A_V_calc.calculate_volume_of_cuboid(5,6,7) == 210.0
    assert A_V_calc.calculate_volume_of_cuboid(2,8,3) == 48.0
    
    
