import numpy as np

from hits import utilities
from hits.serialize import array_1d, array_2d

def test_array_1d_round_trip(tmp_path):
    fn = tmp_path / 'array_1d.txt'
    array = np.array([0, 3, 5])
    array_1d.write_file(array, fn)
    assert np.array_equal(array_1d.read_file(fn), array)

def test_array_2d_round_trip(tmp_path):
    fn = tmp_path / 'array_2d.txt'
    array = np.array([[0, 1], [2, 3]])
    array_2d.write_file(array, fn)
    assert np.array_equal(array_2d.read_file(fn), array)

def test_counts_to_array_2d():
    array = utilities.counts_to_array({(0, 1): 4, (2, 0): 7}, dim=2)
    expected = np.zeros((3, 3), int)
    expected[0, 1] = 4
    expected[2, 0] = 7
    assert np.array_equal(array, expected)
