# -*- coding: utf-8 -*-
"""

@author: AASHISH
"""

'''
                                                    Open Close Principle: Open for extenstion and Close for modification
'''

from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class AMAZON_Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


class ProductFilter:
    def filter_by_color(self, LIST_OF_AMAZON_products, color):
        for p in LIST_OF_AMAZON_products:
            if p.color == color: 
                yield p

    def filter_by_size(self, LIST_OF_AMAZON_products, size):
        for p in LIST_OF_AMAZON_products:
            if p.size == size: 
                yield p

    def filter_by_size_and_color(self, LIST_OF_AMAZON_products, size, color):
        for p in LIST_OF_AMAZON_products:
            if p.color == color and p.size == size:
                yield p

				
    # Problem with this implementation:
    # color size weight  colorsize  sizeWeight colorWeight COLORsizeWeight = 7 methods
	
	# Solution is OCP = open for extension, closed for modification

	
class Requirement_Specification:
    def is_satisfied(self, product):
        pass

    # and operator makes life easier
    def __and__(self, other):
        return AndSpecification(self, other)


class Filter:
    def filter(self, LIST_OF_AMAZON_products, Requirement_Specification):
        pass


class ColorSpecification(Requirement_Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, product):
        return product.color == self.color


class SizeSpecification(Requirement_Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, product):
        return product.size == self.size


# class AndSpecification(Requirement_Specification):
#     def __init__(self, spec1, spec2):
#         self.spec2 = spec2
#         self.spec1 = spec1
#
#     def is_satisfied(self, item):
#         return self.spec1.is_satisfied(item) and \
#                self.spec2.is_satisfied(item)

class AndSpecification(Requirement_Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, product):
        return all(map(
            lambda spec: spec.is_satisfied(product), self.args))


class BetterFilter(Filter):                                                   # we could have this implementation in filter class as well, but for future
										                                                                      	
    def filter(self, LIST_OF_AMAZON_products, Requirement_Specification):
        for each_Product in LIST_OF_AMAZON_products:
            if Requirement_Specification.is_satisfied(each_Product):
                yield each_Product

apple = AMAZON_Product('Apple', Color.GREEN, Size.SMALL)
tree = AMAZON_Product('Tree', Color.GREEN, Size.LARGE)
house = AMAZON_Product('House', Color.BLUE, Size.LARGE)

LIST_OF_AMAZON_products = [apple, tree, house]

pf = ProductFilter()
print('Green products (old):')
for p in pf.filter_by_color(LIST_OF_AMAZON_products, Color.GREEN):
    print(f' - {p.name} is green')

# ^ BEFORE

# v AFTER
bf = BetterFilter()

print('Green products (new):')
green = ColorSpecification(Color.GREEN)
for p in bf.filter(LIST_OF_AMAZON_products, green):
    print(f' - {p.name} is green')

print('Large products:')
large = SizeSpecification(Size.LARGE)
for p in bf.filter(LIST_OF_AMAZON_products, large):
    print(f' - {p.name} is large')

print('Large blue items:')
# large_blue = AndSpecification(large, ColorSpecification(Color.BLUE))
large_blue = large & ColorSpecification(Color.BLUE)
for p in bf.filter(LIST_OF_AMAZON_products, large_blue):
    print(f' - {p.name} is large and blue')
