# Authors: Alexandre Gramfort <alexandre.gramfort@telecom-paristech.fr>
#
# License: BSD (3-clause)

from numpy.testing import (assert_array_equal, assert_almost_equal,
                           assert_allclose)
import numpy as np
from scipy import stats

from mne.stats.permutations import permutation_t_test, _ci, _bootstrap_ci
from mne.utils import run_tests_if_main


def test_permutation_t_test():
    """Test T-test based on permutations."""
    # 1 sample t-test
    np.random.seed(10)
    n_samples, n_tests = 30, 5
    X = np.random.randn(n_samples, n_tests)
    X[:, :2] += 1

    T_obs, p_values, H0 = permutation_t_test(X, n_permutations=999, tail=0)
    is_significant = p_values < 0.05
    assert_array_equal(is_significant, [True, True, False, False, False])

    T_obs, p_values, H0 = permutation_t_test(X, n_permutations=999, tail=1)
    is_significant = p_values < 0.05
    assert_array_equal(is_significant, [True, True, False, False, False])

    T_obs, p_values, H0 = permutation_t_test(X, n_permutations=999, tail=-1)
    is_significant = p_values < 0.05
    assert_array_equal(is_significant, [False, False, False, False, False])

    X = np.random.randn(18, 1)
    T_obs, p_values, H0 = permutation_t_test(X[:, [0]], n_permutations='all')
    T_obs_scipy, p_values_scipy = stats.ttest_1samp(X[:, 0], 0)
    assert_almost_equal(T_obs[0], T_obs_scipy, 8)
    assert_almost_equal(p_values[0], p_values_scipy, 2)


def test_ci():
    # isolated test of CI functions
    arr = np.linspace(0, 1, 1000)[..., np.newaxis]
    assert_allclose(_ci(arr, method="parametric"),
                    _ci(arr, method="bootstrap"), rtol=.005)
    assert_allclose(_bootstrap_ci(arr, statfun="median", random_state=0),
                    _bootstrap_ci(arr, statfun="mean", random_state=0),
                    rtol=.1)

run_tests_if_main()
