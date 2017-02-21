
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import random
import yaml
import os
from .Boids import Boids
#from pkg_resources import resource_filename, resource_exists, Requirement


# config_file = resource_filename(Requirement.parse("Boids"),"boids/config.yaml")
# config=yaml.load(config_file)
# globals().update(config)

#input_position_limits = np.array([minimum_position,maximum_position])
#input_velocity_limits = np.array([minimum_velocity,maximum_velocity])

input_position_limits = np.array([[-450,300.0],[50.0,600.0]])
input_velocity_limits = np.array([[0,-20.0],[10.0,20.0]])
input_boid_count = 50
input_move_to_middle_strength = 0.01
input_alert_distance = 100
input_formation_flying_distance = 1000
input_formation_flying_strength = 0.125


x_axes_limits = [-500,1500]
y_axes_limits = [-500,1500]

number_of_frames = 50
number_of_intervals = 50

boids = Boids(input_position_limits, input_velocity_limits, input_boid_count, input_move_to_middle_strength, input_alert_distance, input_formation_flying_distance, input_formation_flying_strength)


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