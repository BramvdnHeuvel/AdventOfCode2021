import re
from itertools import combinations, filterfalse

from beacon import Beacon

def main():
    scanners = import_file('input.txt')
    beacons  = [get_beacons(s) for s in scanners]

    for b in beacons[0]:
        b.location = b.position
    sync_similar_beacons(beacons)

    while unexplored_scanners(beacons):
        for b in beacons:
            determine_position(b)
        sync_similar_beacons(beacons)

    scanners = []
    for beacon in beacons:
        for b in beacon:
            if b.is_scanner:
                print(b.location)
                scanners.append(b.location)

    distances = [(abs(a[0]-b[0]) + 
                  abs(a[1]-b[1]) + 
                  abs(a[2]-b[2])) for a, b in combinations(scanners, 2)]

    print(max(distances))


def import_file(file_name):
    try:
        with open(file_name, 'r') as open_file:
            scanners = ''.join([line for line in open_file])
    except FileNotFoundError:
        with open('19/ex2/' + file_name, 'r') as open_file:
            scanners = ''.join([line for line in open_file])
    
    scanners = re.split(r'\n*--- scanner \d+ ---\n', scanners)
    scanners = [
        format_scanner(scanner)
        for scanner in scanners
        if len(scanner) > 0
    ]
    scanners = [s for s in scanners if len(s) > 0]

    return scanners

def format_scanner(raw_scanner):
    scanner = []

    for scanner_line in raw_scanner.split('\n'):
        if re.fullmatch(r'-?\d+,-?\d+,-?\d+', scanner_line):
            coords = tuple([
                int(c) for c in scanner_line.split(',')
            ])
            scanner.append(coords)

    return scanner

def get_beacons(scanner):
    beacons = [Beacon(beacon, scanner) for beacon in scanner]
    beacons.append(Beacon((0, 0, 0), scanner, is_scanner=True))
    return beacons

def count_match_beacon_lists(beacons_1, beacons_2, minimum_match=2):
    count = 0

    for _, _ in match_beacon_lists(beacons_1, beacons_2, minimum_match):
        count += 1
    
    return count

def match_beacon_lists(beacons_1, beacons_2, minimum_match=2):
    used  = set()
    count = 0

    for b1 in beacons_1:
        for b2 in filterfalse(lambda v : v in used, beacons_2):
            matches = len([b for b in b1.pattern if b in b2.pattern])
            if matches > minimum_match:
                used.add(b2)
                yield b1, b2

def inspect_scanner(scanner_zero, beacons):
    for scanner, i in zip(beacons, range(len(beacons)+1)):
        m = count_match_beacon_lists(scanner_zero, scanner, 8)
        print(f"Beacon {i} has {m} matching beacons.")

def sync_similar_beacons(beacons):
    for b1, b2 in combinations(beacons, 2):
        for a, b in match_beacon_lists(b1, b2, 2):
            if a.location != None and b.location == None:
                b.location = a.location
            if a.location == None and b.location != None:
                a.location = b.location

def determine_position(beacons):
    if len([b for b in beacons if b.location]) < 3:
        return
    if len([b for b in beacons if b.location == None]) == 0:
        return

    working = []
    
    for x, y, z in [(0, 1, 2), (0, 2, 1), (1, 0, 2), 
                    (1, 2, 0), (2, 0, 1), (2, 1, 0)]:
        for x_dir in [-1, 1]:
            for y_dir in [-1, 1]:
                for z_dir in [-1, 1]:
                    if system_works([b for b in beacons if b.location],
                                    (x, y, z), (x_dir, y_dir, z_dir)):
                        working.append(((x, y, z), (x_dir, y_dir, z_dir)))
    
    if len(working) > 1 or len(working) == 0:
        return

    print(working)
    print("Exploring!")
    apply_system(beacons, working[0][0], working[0][1])
    

def system_works(beacons, cs, ds):
    b = beacons[0]
    offset_x = (b.location[cs[0]] - b.position[0])
    offset_y = (b.location[cs[1]] - b.position[1])
    offset_z = (b.location[cs[2]] - b.position[2])

    for ob in beacons:
        expected_x = b.location[0] + ds[0] * (ob.position[cs[0]] - b.position[cs[0]])
        expected_y = b.location[1] + ds[1] * (ob.position[cs[1]] - b.position[cs[1]])
        expected_z = b.location[2] + ds[2] * (ob.position[cs[2]] - b.position[cs[2]])

        if ob.location != (expected_x, expected_y, expected_z):
            return False
    else:
        return True

def apply_system(beacons, cs, ds):
    b = [b for b in beacons if b.location][0]
    offset_x = (b.location[cs[0]] - b.position[0])
    offset_y = (b.location[cs[1]] - b.position[1])
    offset_z = (b.location[cs[2]] - b.position[2])

    for ob in beacons:
        expected_x = b.location[0] + ds[0] * (ob.position[cs[0]] - b.position[cs[0]])
        expected_y = b.location[1] + ds[1] * (ob.position[cs[1]] - b.position[cs[1]])
        expected_z = b.location[2] + ds[2] * (ob.position[cs[2]] - b.position[cs[2]])
        ob.location = (expected_x, expected_y, expected_z)

def unexplored_scanners(beacons):
    for beacon in beacons:
        for b in beacon:
            if b.is_scanner and not b.location:
                return True
    return False

if __name__ == '__main__':
    main()
