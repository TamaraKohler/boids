from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import random
import yaml
import os
from .Boids import Boids
#from pkg_resources import resource_filename, resource_exists, Requirement

# Extract information from the config file 
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'config.yaml')) as config_file:
    config=yaml.load(config_file)
    globals().update(config)
input_position_limits = np.array([minimum_position,maximum_position])
input_velocity_limits = np.array([minimum_velocity,maximum_velocity])


# Input parameters of the simulation
x_axes_limits = [-500,1500]
y_axes_limits = [-500,1500]
number_of_frames = 50
number_of_intervals = 50

#Create an instance of the boids’ class with information from configuration file
boids = Boids(input_position_limits, input_velocity_limits, input_boid_count, input_move_to_middle_strength, input_alert_distance, input_formation_flying_distance, input_formation_flying_strength)


# Animate the boids
figure=plt.figure()
axes=plt.axes(xlim=(x_axes_limits[0],x_axes_limits[1]), ylim=(y_axes_limits[0],y_axes_limits[1]))
scatter=axes.scatter(boids.positions[0],boids.positions[1])

def animate(frame):
    boids.update_boids()
    x_pos = np.array(boids.positions[0])
    y_pos = np.array(boids.positions[1])
    data = np.hstack((x_pos[:,np.newaxis],y_pos[:,np.newaxis]))
    scatter.set_offsets(data)

anim = animation.FuncAnimation(figure, animate, frames=number_of_frames, interval=number_of_intervals)

def process():
    plt.show()

if __name__ == "__main__": 
    process()