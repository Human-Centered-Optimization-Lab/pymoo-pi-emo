import pytest

from pymoo.util import value_functions as vf
import numpy as np

test_dummy_val_fnc_inputs = [
    (np.array([[1,2], [2,3]]), [1,2], np.array([1,2]), 3),
    (np.array([[2,3], [3,2]]), [2,1], np.array([3,2]), 5)
]

# This is a general test for function I/O. 
# It should take in a set of PO points, and then return a function. 
# That function should take in a given PO point and return the 
# value of that point according to the decision maker

@pytest.mark.parametrize('F, rankings, test_f, expected_value', test_dummy_val_fnc_inputs)
def test_dummy_vf(F, rankings, test_f, expected_value):

    val_fnc = vf.create_linear_vf(F, rankings)

    assert val_fnc(test_f) == expected_value


test_test_prob_const_in_out = [
    (np.array([[1,2], [2,3], [4,5]]), [1,3,2], np.array([[1,2], [4,5], [2,3]])),
    (np.array([[2,3], [3,2], [7,8]]), [5,2,1], np.array([[7,8], [3,2], [2,3]]))
]



@pytest.mark.parametrize('F, rankings, output', test_test_prob_const_in_out)
def test_prob_const(F, rankings, output):

    pymoo_prob = vf.OptimizeVF(F, rankings)

    ## Test whether the solutions are ranked by ranking 
    ranks_from_prob = pymoo_prob.P[:, -1]
    F_from_prob = pymoo_prob.P[:, 0:-1]

    rankings.sort()

    # Check the solutions 
    assert np.all(output == F_from_prob)

    # Check the ranks
    assert ranks_from_prob.tolist() == rankings
   

    

    


