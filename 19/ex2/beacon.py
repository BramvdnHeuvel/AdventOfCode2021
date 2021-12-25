from typing import Tuple, List

class Beacon:
    def __init__(self, my_coord :      Tuple[int, int, int], 
                       coords   : List[Tuple[int, int, int]],
                       is_scanner = False):
        self.position   = my_coord
        self.coords     = coords
        self.is_scanner = is_scanner
    
        self.pattern    = self.calculate_pattern()
        self.location   = None
    
    def __repr__(self):
        return ('<Beacon ' + 
            (str(self.location) if self.location else 'somewhere')
        + '>')
    
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
