
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np

import random

lower_position_limits = np.array([-450,300.0])
upper_position_limits = np.array([50.0,600.0])

lower_velocity_limits = np.array([0,-20.0])
upper_velocity_limits = np.array([10.0,20.0])

x_axes_limits = [-500,1500]
y_axes_limits = [-500,1500]

boid_count = 50
number_of_frames = 50
number_of_intervals = 50

move_to_middle_strength = 0.01
alert_distance = 100
formation_flying_distance = 10000
formation_flying_strength = 0.125

def new_flock(count, lower_limits, upper_limits):
    width=upper_limits-lower_limits
    return (lower_limits[:,np.newaxis] + 
         np.random.rand(2, count)*width[:,np.newaxis])

boids_positions = new_flock(boid_count,lower_position_limits,upper_position_limits)
boids_velocities = new_flock(boid_count,lower_velocity_limits,upper_velocity_limits)


boids=(boids_positions,boids_velocities)

def update_boids(boids): 
    positions,velocities=boids
    # Fly towards the middle 
    middle_of_boids = np.mean(positions,1)
    direction_to_middle = positions - middle_of_boids[:,np.newaxis]
    velocities -= direction_to_middle * move_to_middle_strength	

    # Fly away from nearby boids
    boid_separations = positions[:,np.newaxis,:] - positions[:,:,np.newaxis]
    squared_displacements = boid_separations * boid_separations
    square_distance = np.sum(squared_displacements,0)
    close_birds = square_distance < alert_distance
    separations_if_close = np.copy(boid_separations)
    far_away  = np.logical_not(close_birds)
    separations_if_close[0,:,:][far_away] = 0
    separations_if_close[1,:,:][far_away] = 0
    velocities += np.sum(separations_if_close,1)

    # Try to match speed with nearby boids
    velocity_differences = velocities[:,np.newaxis,:] - velocities[:,:,np.newaxis]
    very_far=square_distance > formation_flying_distance
    velocity_differences_if_close = np.copy(velocity_differences)
    velocity_differences_if_close[0,:,:][very_far] =0
    velocity_differences_if_close[1,:,:][very_far] =0
    velocities -= np.mean(velocity_differences_if_close, 1) * formation_flying_strength

    # Move according to velocities
    positions += velocities

figure=plt.figure()
axes=plt.axes(xlim=(x_axes_limits[0],x_axes_limits[1]), ylim=(y_axes_limits[0],y_axes_limits[1]))
scatter=axes.scatter(boids[0],boids[1])

def animate(frame):
    update_boids(boids) 
    x_pos = np.array(boids[0])
    y_pos = np.array(boids[1])
    data = np.hstack((x_pos[:,np.newaxis],y_pos[:,np.newaxis]))
    scatter.set_offsets(data)

anim = animation.FuncAnimation(figure, animate, frames=number_of_frames, interval=number_of_intervals)

if __name__ == "__main__": 
    plt.show()