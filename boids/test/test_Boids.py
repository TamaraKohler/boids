from boids import Boids
import os
import numpy.testing as npt
import numpy as np
from nose.tools import assert_equals, assert_true
import yaml

def test_new_flock():
    boids = Boids()
    array = boids.new_flock(np.array([0,50]),np.array([50,100]))
    x_array = array[0,:]
    y_array = array[1,:]
    assert_equals(array.shape, (2,50))
    assert_true((x_array > 0).all() and (x_array < 50).all())
    assert_true((y_array >50).all() and (y_array < 100).all())

def test_fly_towards_middle():
    fly_middle_data=yaml.load(open(os.path.join(os.path.dirname(__file__),'fixtures/fly_towards_middle_fixture.yml')))
    boids = fly_middle_data["before"]
    boids.fly_towards_middle()
    expected_outcome = fly_middle_data["after"]
    npt.assert_array_equal(expected_outcome.positions, boids.positions)
    npt.assert_array_equal(expected_outcome.velocities,boids.velocities)
    #assert_equals(fly_middle_data["after"],boids)
    
def test_square_distances():
    square_distances_data=yaml.load(open(os.path.join(os.path.dirname(__file__),'fixtures/square_distances_fixture.yml')))
    boids = square_distances_data["before"]
    expected_answer = square_distances_data["distances"]
    answer = boids.square_distances()
    npt.assert_array_equal(expected_answer,answer)
    
def test_avoid_collisions():
    avoid_collisions_data=yaml.load(open(os.path.join(os.path.dirname(__file__),'fixtures/avoid_collisions_fixture.yml')))
    boids = avoid_collisions_data["before"]
    boids.avoid_collisions()
    expected_outcome = avoid_collisions_data["after"]
    npt.assert_array_equal(expected_outcome.positions, boids.positions)
    npt.assert_array_equal(expected_outcome.velocities,boids.velocities)
    #assert_equals(avoid_collisions_data["after"],boids)
    
def test_match_speed_boids():
    match_speed_data=yaml.load(open(os.path.join(os.path.dirname(__file__),'fixtures/match_speed_fixture.yml')))
    boids = match_speed_data["before"]
    boids.match_speed_boids()
    expected_outcome = match_speed_data["after"]
    npt.assert_array_equal(expected_outcome.positions, boids.positions)
    npt.assert_array_equal(expected_outcome.velocities,boids.velocities)
    #assert_equals(match_speed_data["after"],boids)
    
def test_update_boids():
    update_data=yaml.load(open(os.path.join(os.path.dirname(__file__),'fixtures/update_boids_fixture.yml')))
    boids=update_data["before"]
    boids.update_boids()
    expected_outcome = update_data["after"]
    npt.assert_array_equal(expected_outcome.positions,boids.positions)
    npt.assert_array_equal(expected_outcome.velocities,boids.velocities)
    #assert_equals(update_data["after"],boids)