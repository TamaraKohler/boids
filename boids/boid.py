
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import random


input_position_limits = np.array([[-450,300.0],[50.0,600.0]])

input_velocity_limits = np.array([[0,-20.0],[10.0,20.0]])


input_boid_count = 50

input_move_to_middle_strength = 0.01
input_alert_distance = 100
input_formation_flying_distance = 10000
input_formation_flying_strength = 0.125


x_axes_limits = [-500,1500]
y_axes_limits = [-500,1500]

number_of_frames = 50
number_of_intervals = 50


class Boids(object):
    def __init__(self, position_limits, velocity_limits, boid_count, move_to_middle_strength, alert_distance, formation_flying_distance, formation_flying_strength):
        self.boid_count = boid_count
        self.positions = self.new_flock(position_limits[0,:],position_limits[1,:])
        self.velocities = self.new_flock(velocity_limits[0,:],velocity_limits[1,:])
        self.move_to_middle_strength = move_to_middle_strength
        self.alert_distance = alert_distance
        self.formation_flying_distance = formation_flying_distance
        self.formation_flying_strength = formation_flying_strength


    def new_flock(self, lower_limits, upper_limits):
        width=upper_limits-lower_limits
        return (lower_limits[:,np.newaxis] + np.random.rand(2, self.boid_count)*width[:,np.newaxis])


    def fly_towards_middle(self):
        middle_of_boids = np.mean(self.positions,1)
        direction_to_middle = self.positions - middle_of_boids[:,np.newaxis]
        self.velocities -= direction_to_middle * self.move_to_middle_strength	

    def square_distances(self):
        boid_separations = self.positions[:,np.newaxis,:] - self.positions[:,:,np.newaxis]
        squared_displacements = boid_separations * boid_separations
        square_distance = np.sum(squared_displacements,0)
        return square_distance


    def avoid_collisions(self):
        close_birds = self.square_distances() < self.alert_distance
        separations_if_close = self.positions[:,np.newaxis,:] - self.positions[:,:,np.newaxis]
        far_away  = np.logical_not(close_birds)
        separations_if_close[0,:,:][far_away] = 0
        separations_if_close[1,:,:][far_away] = 0
        self.velocities += np.sum(separations_if_close,1)


    def match_speed_boids(self):
        velocity_differences = self.velocities[:,np.newaxis,:] - self.velocities[:,:,np.newaxis]
        very_far= self.square_distances() > self.formation_flying_distance
        velocity_differences_if_close = np.copy(velocity_differences)
        velocity_differences_if_close[0,:,:][very_far] =0
        velocity_differences_if_close[1,:,:][very_far] =0
        self.velocities -= np.mean(velocity_differences_if_close, 1) * self.formation_flying_strength


    def update_boids(self): 
        self.fly_towards_middle()	
        self.avoid_collisions()
        self.match_speed_boids()
        self.positions += self.velocities


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

if __name__ == "__main__": 
    plt.show()