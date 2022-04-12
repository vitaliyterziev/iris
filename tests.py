import unittest
from cube import Cube
from main import stackable, volume_sum, producer, consumer
from collections import deque
import threading


class CubeTests(unittest.TestCase):
    '''Test Cube objects and their respective volume and side_length methods'''

    def setUp(self):
        self.cube = Cube(3)

    def test_volume(self):
        self.assertEqual(self.cube.volume(), 27)

    def test_side_length(self):
        self.assertEqual(self.cube.side_length(), 3)


class VolumeStackableTests(unittest.TestCase):
    '''Test helper functions, stackable and volume_sum'''

    def setUp(self):
        cubes = deque()
        for side in [4, 3, 2, 1, 3, 4]:
            cubes.append(Cube(side))
        self.cubes = cubes

    def test_volume_sum(self):
        self.assertEqual(volume_sum(self.cubes), 191)

    def test_stackable(self):
        self.assertEqual(stackable(self.cubes), True)


class ProducerConsumerTests(unittest.TestCase):
    '''Test Producer/Consumer pattern, number of threads, hit enter after finished'''

    def setUp(self):
        self.pt = threading.Thread(name='producer', target=producer)
        self.ct = threading.Thread(name='consumer', target=consumer)
        self.pt.start()
        self.ct.start()

    def test_number_threads(self):
        self.assertEqual(threading.activeCount(), 3)
