from boids import Boids
import numpy.testing as npt
import os
import yaml

def test_bad_boids_regression():
    regression_data=yaml.load(open(os.path.join(os.path.dirname(__file__),'fixtures/regression_fixture.yml')))
    boids=regression_data["before"]
    boids.update_boids()
    outcome = boids
    expected_outcome = regression_data["after"]
    npt.assert_array_equal(expected_outcome.positions,outcome.positions)
    npt.assert_array_equal(expected_outcome.velocities,outcome.velocities)