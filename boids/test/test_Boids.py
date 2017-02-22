from boids import Boids
import os
import numpy.testing as npt
import numpy as np
from nose.tools import assert_equals

input_position_limits = np.array([[-450,300.0],[50.0,600.0]])
input_velocity_limits = np.array([[0,-20.0],[10.0,20.0]])
input_boid_count = 50
input_move_to_middle_strength = 0.01
input_alert_distance = 100
input_formation_flying_distance = 1000
input_formation_flying_strength = 0.125

initial_positions = np.load(os.path.join(os.path.dirname(__file__),'fixtures/initial_positions.npy'))
initial_velocities = np.load(os.path.join(os.path.dirname(__file__),'fixtures/initial_velocities.npy'))

#def test_new_flock() how to test random output??

def test_fly_towards_middle():
    boids = Boids(input_position_limits, input_velocity_limits, input_boid_count, input_move_to_middle_strength, input_alert_distance, input_formation_flying_distance, input_formation_flying_strength)
    boids.positions = initial_positions
    boids.velocities = initial_velocities
    expected_final_positions = np.load(os.path.join(os.path.dirname(__file__),'fixtures/fly_towards_middle_positions.npy'))
    expected_final_velocities = np.load(os.path.join(os.path.dirname(__file__),'fixtures/fly_towards_middle_velocities.npy'))
    boids.fly_towards_middle()
    final_positions = boids.positions
    final_velocities = boids.velocities
    npt.assert_array_equal(final_positions,expected_final_positions)
    npt.assert_array_equal(final_velocities,expected_final_velocities)
    

    
    