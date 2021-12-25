from typing import Tuple, List

class Beacon:
    def __init__(self, my_coord :      Tuple[int, int, int], 
                       coords   : List[Tuple[int, int, int]]):
        self.position = my_coord
        self.coords   = coords
    
        self.pattern  = self.calculate_pattern()
    
    def __repr__(self):
        return '<Beacon ' + str(self.pattern[:4]) + '>'
    
    def calculate_pattern(self):
        """
            Since it will be too difficult to look at all
            beacons in all Euclidian transformations, we
            acquire a "signature" by noting which beacons
            are closest to this beacon.
            We can use this to match beacons to each other
            on different scanners.
        """
        positions = [self.distance(c) for c in self.coords]
        positions.sort()

        return positions

    def distance(self, other_coords):
        d = 0

        for s, o in zip(self.position, other_coords):
            d += abs(s - o) ** 2
        
        return d
