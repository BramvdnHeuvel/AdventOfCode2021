import re
from itertools import combinations, filterfalse

from beacon import Beacon

def main():
    scanners = import_file('input.txt')
    beacons  = [get_beacons(s) for s in scanners]

    # Take a look at how beacons overlap
    # inspect_scanner(beacons[0], beacons)

    bs = []
    for beacon in beacons:
        for b in beacon:
            bs.append(b)
    print(bs)

    for b1, b2 in combinations(beacons, 2):
        for _, b in match_beacon_lists(b1, b2, 2):
            if b in bs:
                bs.remove(b)
    
    print(len(bs))


def import_file(file_name):
    try:
        with open(file_name, 'r') as open_file:
            scanners = ''.join([line for line in open_file])
    except FileNotFoundError:
        with open('19/ex1/' + file_name, 'r') as open_file:
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
    return [Beacon(beacon, scanner) for beacon in scanner]

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

if __name__ == '__main__':
    main()
