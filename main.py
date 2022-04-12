import queue
import threading
from cube import Cube
from collections import deque

BUF_SIZE = 5
q = queue.Queue(BUF_SIZE)


def producer():
    '''Create a producer to read from console and pass to consumer'''

    number_of_tests = int(input())

    # Run for number of cases
    for _ in range(number_of_tests):
        n_cubes = input()
        cubes_sides = input().split()
        cubes = deque()

        # Create Cube objects and store them in deque
        for cube_side in cubes_sides:
            cubes.append(Cube(int(cube_side)))

        if not q.full():
            q.put(cubes)


def consumer(pt):
    '''Keep waiting on producer to suply queue until producer is finished'''

    keep_up = True
    while keep_up:
        if not q.empty():
            cubes = q.get()

            vol = volume_sum(cubes)
            
            if stackable(cubes):
                print(f'Yes {vol}')
            else:
                print(f'No {vol}')

            if not pt.is_alive():
                keep_up = False


def stackable(cubes):
    '''Check if all cubes are stackable'''
    stackable = True
    cur_cube = None

    # Get current cube, bigger of leftmost and rightmost cubes
    if cubes[0].side_length() >= cubes[-1].side_length():
        cur_cube = cubes.popleft()
    else:
        cur_cube = cubes.pop()

    # Check leftmost and rightmost cubes against current cube and themselves to find next cube
    while cubes and stackable:
        lcube_s = cubes[0].side_length()  # O(1)
        rcube_s = cubes[-1].side_length()  # O(1)
        ccube_s = cur_cube.side_length()  # O(1)

        if (lcube_s <= ccube_s) and (lcube_s >= rcube_s):
            cur_cube = cubes.popleft()  # O(1)
        elif (rcube_s <= ccube_s) and (rcube_s >= lcube_s):
            cur_cube = cubes.pop()  # O(1)
        else:
            stackable = False

    return stackable


def volume_sum(cubes):
    '''Sum volume of all cubes'''
    vol = 0
    for cube in cubes:
        vol += cube.volume()
    return vol


if __name__ == '__main__':

    pt = threading.Thread(name='producer', target=producer)
    ct = threading.Thread(name='consumer', target=consumer, args=(pt,))

    pt.start()
    ct.start()
