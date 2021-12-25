import re

with open('input.txt', 'r') as open_file:
    instructions = [
        list(re.fullmatch(
            r'(off|on) x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)',
            line.strip()
        ).groups())
        for line in open_file
    ]

    for task in instructions:
        for i in range(1, 7):
            task[i] = int(task[i])

class Cuboid:
    def __init__(self, x_from, x_to, y_from, y_to, z_from, z_to):
        self.x = (x_from, x_to)
        self.y = (y_from, y_to)
        self.z = (z_from, z_to)

        self.within_bounds = (
            (-50 <= x_from <= x_to <= 50) and 
            (-50 <= y_from <= y_to <= 50) and 
            (-50 <= z_from <= z_to <= 50)
        )
    
    def __repr__(self):
        return (
            f"<Cuboid ({self.x[0]}, {self.y[0]}, {self.z[0]})" +
            f" -> ({self.x[1]}, {self.y[1]}, {self.z[1]})>"
        )

    
    def __len__(self):
        """
            Determine how many tiles are within this cuboid.
        """
        return (
            (abs(self.x[1] - self.x[0]) + 1) *
            (abs(self.y[1] - self.y[0]) + 1) *
            (abs(self.z[1] - self.z[0]) + 1)
        )
    
    def erase(self, other):
        """
            Remove tiles from this cube.

            Returns a list of cuboid objects that can replace
            both cuboid objects altogether.
        """
        if not self.overlap(other):
            yield self
        else:
            if self.x[0] < other.x[0]:
                yield Cuboid(self.x[0], other.x[0]-1, 
                             self.y[0], self.y[1], 
                             self.z[0], self.z[1])
            if self.x[1] > other.x[1]:
                yield Cuboid(other.x[1]+1, self.x[1],
                             self.y[0], self.y[1],
                             self.z[0], self.z[1])
            if self.y[0] < other.y[0]:
                yield Cuboid(max(self.x[0], other.x[0]), min(self.x[1], other.x[1]),
                             self.y[0], other.y[0]-1,
                             self.z[0], self.z[1])
            if self.y[1] > other.y[1]:
                yield Cuboid(max(self.x[0], other.x[0]), min(self.x[1], other.x[1]),
                             other.y[1]+1, self.y[1],
                             self.z[0], self.z[1])
            if self.z[0] < other.z[0]:
                yield Cuboid(max(self.x[0], other.x[0]), min(self.x[1], other.x[1]),
                             max(self.y[0], other.y[0]), min(self.y[1], other.y[1]),
                             self.z[0], other.z[0]-1)
            if self.z[1] > other.z[1]:
                yield Cuboid(max(self.x[0], other.x[0]), min(self.x[1], other.x[1]),
                             max(self.y[0], other.y[0]), min(self.y[1], other.y[1]),
                             other.z[1]+1, self.z[1])

    def add(self, other):
        """
            Add tiles to this cube.

            Returns a list of cuboid objects that can replace
            both cuboid objects altogether.
        """
        if not self.overlap(other):
            yield from [self, other]
        else:
            yield self
            yield from other.erase(self)

    def overlap(self, other):
        """
            Return whether two cuboids overlap.
        """
        return not (
            self.x[1] < other.x[0] or
            other.x[1] < self.x[0] or

            self.y[1] < other.y[0] or
            other.y[1] < self.y[0] or

            self.z[1] < other.z[0] or
            other.z[1] < self.z[0]
        )

cuboids = [(task[0], Cuboid(*task[1:])) for task in instructions]
# cuboids = [c for c in cuboids if c[1].within_bounds]

current_cuboids = []

for task, cuboid in cuboids:
    if task == 'off':
        new_current = []

        for current in current_cuboids:
            new_current.extend(
                list(current.erase(cuboid))
            )
    
        current_cuboids = list(set(new_current))
    
    elif task == 'on':
        new_cuboids = [cuboid]

        for current in current_cuboids:
            new_new_cuboids = []
            for cube in new_cuboids:
                new_new_cuboids.extend(
                    list(cube.erase(current))
                )
            
            new_cuboids = new_new_cuboids
        
        current_cuboids.extend(new_cuboids)

print(sum([len(cuboid) for cuboid in current_cuboids]))
