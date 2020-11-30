from module1 import Polygon


class Polygons:
    def __init__(self, edges, circumradius):
        self._edges = edges
        self._circumradius = circumradius
    def __iter__(self):
        return self.PolygonIter(self)
        
    def __len__(self):
        return self._edges - 2

    def __repr__(self):
        return f'Polygons(Edges = {self._edges}, Circumradius = {self._circumradius})'

    @property
    def max_efficiency_polygon(self):
        sorted_polygons = sorted(self, key=lambda p:p.area/p.perimeter, reverse= True)
        return sorted_polygons[0]

    class PolygonIter:
        def __init__(self, poly_obj):
            self._index = 3
            self._poly_obj = poly_obj

        def __iter__(self):
            return self

        def __next__(self):
            if self._index > self._poly_obj._edges:
                raise StopIteration
            else:
                item = Polygon(self._index, self._poly_obj._circumradius)
                self._index += 1
                return item
