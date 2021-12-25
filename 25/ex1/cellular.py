import math
from os import curdir

from typing import Any, Callable, Dict, Generator, List, Tuple
from collections import Counter

class CellularAutomaton:
    """
        Class that simulates cellular automatons like Game of Life.
        Since applications may vary, there are several parameters
        that can be changed to function in a better way.
    """
    def __init__(self, 
        next_state     : Callable,
        default_value  : Any,
        neighbour_size : int = 1,
        dimensions     : List[Tuple[int, int]] = [
            (-float("inf"), float("inf")),
            (-float("inf"), float("inf"))
        ]
    ):
        self.dimensions     : List[Tuple[int, int]] = dimensions
        self.default_value  : Any                   = default_value
        self.neighbour_size : int                   = neighbour_size
        self.next_state     : Callable              = next_state

        self.boundaries     : List[Tuple[int, int]] = [(0,0) for _ in dimensions]
        self.values         : Dict[int, Any]        = {}


    def run(self, iterations : int = 1):
        """
            Run the automaton for multiple rounds.
        """
        print("Initial state:")
        self.show()

        previous, current = None, self.values

        for i in range(iterations):
            self.__iterate()

            print(f"After {i+1} steps: ")
            # self.show()

            previous, current = current, self.values
            if previous == current:
                break
        
        return self.values

    def count(self) -> Counter:
        """
            Count how often each value appears in the automaton.
        """
        default_size = (
            self.__dim_size(self.dimensions) - self.__dim_size(self.boundaries)
        )

        c = Counter({self.default_value: default_size})

        for coords in self.__iterate_dimensions():
            c[self.lookup(*coords)] += 1
        
        return c


    def set_point(self, value, *coords) -> None:
        """
            Override a specific point at a location with a given value.
        """
        self.__correct_dimensions(*coords)
        
        self.values[coords] = value

        # We don't want it if it's a default value
        if value == self.default_value:
            del self.values[coords]

        # If it's something else, update the boundaries
        else:
            self.__update_boundaries(*coords)


    def lookup(self, *coords, default_lookup = None) -> Any:
        """
            Look up a value in the cellular automaton.

            If the position isn't found, it returns the attribute
            `default_value`. This can be overwritten by giving a
            custom `default_lookup` value.

            If the position is out of bounds, it will return the output
            of the method `out_of_bounds_lookup`.
        """
        self.__correct_dimensions(*coords)
        
        # Check if the value is within bounds
        for c, ds in zip(coords, self.dimensions):
            if not ds[0] <= c <= ds[1]:
                return self.out_of_bounds_lookup(*coords)
        

        if coords in self.values:
            return self.values[coords]
        elif default_lookup is None:
            return self.default_value
        else:
            return default_lookup


    def out_of_bounds_lookup(self, *coords) -> Any:
        """
            This function can be manually overwritten if needed.

            By default, it returns `default_value`.
        """
        new_coords = ()
        for x, d in zip(coords, self.dimensions):
            if x < d[0]:
                new_coords += (x + abs(d[1]-d[0])+1,)
            elif d[0] <= x <= d[1]:
                new_coords += (x,)
            else:
                new_coords += (x - abs(d[1]-d[0])-1,)
        
        return self.lookup(*new_coords)
    
    def show(self):
        d = self.dimensions
        for y in range(d[1][0], d[1][1]+1):
            for x in range(d[0][0], d[0][1]+1):
                print(self.lookup(x, y), end='')
            print('')
        print('')
            
    

    def __iterate(self):
        """
            Run one step for the cellular automaton.
        """
        def calculate_position(*coords):
            def lookup_func(*rel_coords):
                c = tuple(
                    c + rc for c, rc in zip(coords, rel_coords)
                )
                return self.lookup(*c)
            return self.next_state(lookup_func)

        # We alter the automaton by building a new copy
        # before inheriting its attributes.
        c = CellularAutomaton(
            next_state     = self.next_state,
            default_value  = self.next_state(
                                # Calculate the next default state
                                lambda *c : self.default_value
                             ),
            neighbour_size = self.neighbour_size,
            dimensions     = self.dimensions
        )

        for coord in self.__iterate_dimensions():
            if coord == (6, 4):
                j = 0
            new_value = calculate_position(*coord)
            c.set_point(new_value, *coord)
        
        self.default_value = c.default_value
        self.boundaries    = c.boundaries
        self.values        = c.values

    def __correct_dimensions(self, *coords) -> None:
        """
            Check if the right amount of dimensions is given.
        """
        if len(coords) != len(self.dimensions):
            raise ValueError(
                "Received incorrect amount of dimensions " + 
                f"(expected {len(self.dimensions)}, got {len(coords)})"
            )
    
    def __update_boundaries(self, *coords) -> None:
        """
            Notify the automaton that a given coordinate has been changed
            to a non-default value, telling it that the automaton should
            now also look near this location.
        """
        nbs = self.neighbour_size

        for c, ds, bs, i in zip(coords, self.dimensions, 
                                self.boundaries, range(len(coords))):
            minimum = min(c-nbs, bs[0])
            minimum = max(ds[0], minimum) # Don't let it cross borders

            maximum = max(c+nbs, bs[1])
            maximum = min(ds[1], maximum) # Don't let it cross borders

            if (minimum, maximum) != bs:
                self.boundaries[i] = (minimum, maximum)
    
    def __dim_size(self, dimensions : List[Tuple[int, int]]) -> int:
        """
            Calculate the size of a multidimensional plane.
        """
        return math.prod(
            [1 + abs(d[1] - d[0]) for d in dimensions]
        )

    def __iterate_dimensions(self, slice : int = 0):
        """
            Iterate over all the dimensions using DFS.
        """
        if slice == len(self.boundaries):
            yield ()
        else:
            minimum, maximum = self.boundaries[slice]

            for i in range(minimum, maximum + 1):
                for t in self.__iterate_dimensions(slice + 1):
                    yield (i,) + t
