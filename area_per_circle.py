#!/usr/bin/env python3
# Created by: Hunter Connolly
# February 23
# This program calculates area and circumference of a circle
# with a radius of 15mm
import math


def main():
    print("For a circle that has the radius")
    print("of 15mm")
    print("")
    print("Area = {} mm^2" .format(math.pi*15**2))
    print("Circumference = {} mm" .format(2*math.pi*15))


if __name__ == "__main__":
    main()
