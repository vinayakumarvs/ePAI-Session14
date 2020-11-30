# Session 14 - Iterables and Iterators

# EPAi Session14 Assignment

### Objective of Assignment:

The starting point for this project is the Polygon class and the Polygons sequence type we created in the Session13 project.

## Objective - 1

Refactor the Polygon class so that all the calculated properties are lazy properties, i.e. they should still be calculated properties, but they should not have to get recalculated more than once (since we made our Polygon class "immutable").


## Objective - 2

Refactor the Polygons (sequence) type, into an iterable. Make sure also that the elements in the iterator are computed lazily - i.e. you can no longer use a list as an underlying storage mechanism for your polygons.

Need to implement both an iterable, and an iterator.
