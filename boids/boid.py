
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
    for i in range(boid_count):
        for j in range(boid_count): 
            velocities[0,i]=velocities[0,i]+(positions[0,j]-positions[0,i])*move_to_middle_strength/len(positions[0,:])
    for i in range(boid_count):
        for j in range(boid_count): 
            velocities[1,i]=velocities[1,i]+(positions[1,j]-positions[1,i])*move_to_middle_strength/len(positions[0,:])
    # Fly away from nearby boids
    for i in range(boid_count):
        for j in range(boid_count):
            if (positions[0,j]-positions[0,i])**2 + (positions[1,j]-positions[1,i])**2 < alert_distance: 
                velocities[0,i]=velocities[0,i]+(positions[0,i]-positions[0,j]) 
                velocities[1,i]=velocities[1,i]+(positions[1,i]-positions[1,j])
    # Try to match speed with nearby boids
    for i in range(boid_count):
        for j in range(boid_count):
            if (positions[0,j]-positions[0,i])**2 + (positions[1,j]-positions[1,i])**2 < formation_flying_distance: 
                velocities[0,i]=velocities[0,i]+(velocities[0,j]-velocities[0,i])*formation_flying_strength/len(positions[0,:]) 
                velocities[1,i]=velocities[1,i]+(velocities[1,j]-velocities[1,i])*formation_flying_strength/len(positions[0,:]) 
    # Move according to velocities
    for i in range(boid_count): 
        positions[0,i]=positions[0,i]+velocities[0,i] 
        positions[1,i]=positions[1,i]+velocities[1,i]

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