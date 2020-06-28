# This file collects a few examples on how the modules of
# the package can be tested. This file can also be used by
# the github continuous integration (CI) to the test the code
# everytime there is a push.
#
# The <test coverage> can then be assessed using pytest-cov.
# This basically tests how many percents of the modules are
# being tested.
#
# Documentation:
# https://docs.pytest.org/en/stable/contents.html

import pytest
import numpy as np
from pathlib import Path
from numpy.testing import assert_almost_equal


# -- Addition ---------------------------------------------------------
@pytest.mark.parametrize("inputs, expected", [("1+2", 3), ("3*4", 12)])
def test_computation(inputs, expected):
    """Test a function that takes 2 arguments and compute the results
    according to a given operations.

    Parameters
    ----------
        inputs: operations
            Operation to be computed
        expected: int
            Expected results
    """
    assert eval(inputs) == expected


# -- Mean -------------------------------------------------------------
# Compare function that computes the mean of an array with numpy.mean
DIM_X = 10
DIM_Y = 20
DIM_Z = 40


def _mean(arr):
    """Compute mean in the standard way."""
    result = np.zeros((DIM_Y, DIM_Z))
    for fl in range(DIM_Y):
        for x in range(DIM_Z):
            repl = 0
            for rep in range(DIM_X):
                repl += arr[rep][fl][x]
            result[fl][x] = repl
    return result / DIM_X


def test_mean():
    """ Compare standard mean and the numpy implementation"""
    arr = np.random.uniform(0, 1, size=[DIM_X, DIM_Y, DIM_Z])
    st_mean = _mean(arr)
    np_mean = np.mean(arr, axis=0)
    assert_almost_equal(np_mean, st_mean, decimal=10)


# -- Test a class -----------------------------------------------------

class CheckDir:
    curr_path = Path().absolute()

    def return_dir(self):
        return self.curr_path


def checkatttribute(cl, attr):
    """This function checks if an attribute `attr` is present in
    the class `cl`.

    Parameters
    ----------
        cl: class
            A given class
        attr:
            Name of the attribute
    """
    __tracebackhide__ = True
    if not hasattr(cl, attr):
        pytest.fail("{cl} has no attribute {attr}")


def test_checkatttribute():
    """This is the test function that is going to be called by
    pytest in order to test the `checkatttribute` method.
    """
    checkatttribute(CheckDir, "return_dir")
