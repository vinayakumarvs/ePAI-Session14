import math

class Polygon:
    def __init__(self, edges, circumradius):
        if type(edges) is not int:
            raise TypeError('Polygon edges should be integer in number')

        if type(circumradius) not in [int, float]:
            raise TypeError('Polygon circum radius should be in integer or float')

        if edges < 3:
            raise ValueError('Polygon edges should be more than 3')

        if circumradius < 0:
            raise ValueError('Polygon circum radius should be positive')

        self._edges = edges
        self._circumradius = circumradius
        self._vertices = None
        self._interior_angle = None
        self._edge_length = None
        self._apothem = None
        self._area = None
        self._perimeter = None

    def __repr__(self):
        return f'Polygon with (edges = {self._edges}, circum radius: {self._circumradius})'

    def __iter__(self):
        return self

    def __next__(self):
        return self

    @property
    def edges(self):
        return self._edges

    @property
    def circumradius(self):
        return self._circumradius

    @property
    def vertices(self):
        if self._vertices is None:
            print('Setting vertices...')
            self._vertices = self._edges
        return self._vertices

    @property
    def interior_angle(self):
        if self._interior_angle is None:
            print('Calculating the interior angle...')
            self._interior_angle = (self._edges - 2) * (180 / self._edges)
        return self._interior_angle

    @property
    def edge_length(self):
        if self._edge_length is None:
            print('Calculating the edge length...')
            self._edge_length = 2 * self._circumradius * math.sin(math.pi/self._edges)
        return self._edge_length

    @property
    def apothem(self):
        if self._apothem is None:
            print('Calculating apothem...')
            self._apothem = self._circumradius * math.cos(math.pi/self._edges)
        return self._apothem

    @property
    def area(self):
        if self._area is None:
            print('Calculating the area of Polygon...')
            self._area = 0.5 * self._edges * self.edge_length * self.apothem
        return self._area

    @property
    def perimeter(self):
        if self._perimeter is None:
            print('Calculating perimeter...')
            self._perimeter = self._edges * self.edge_length
        return self._perimeter

    def __eq__(self, other):
        if isinstance(other,self.__class__):
            return (self.edges == other.edges) and (self.circumradius == other.circumradius)
        else:
            raise TypeError("Polygon class instance is expected")

    def __gt__(self, other):
        if isinstance(other,self.__class__):
            return self.vertices > other.vertices
        else:
            raise TypeError("Polygon class instance is expected")
