
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np

import random

x_position_limits = [-450,50.0]
y_position_limits = [300.0,600.0]

x_velocity_limits = [0,10.0]
y_velocity_limits = [-20.0,20.0]

x_axes_limits = [-500,1500]
y_axes_limits = [-500,1500]

boid_count = 50
number_of_frames = 50
number_of_intervals = 50

move_to_middle_strength = 0.01
alert_distance = 100
formation_flying_distance = 10000
formation_flying_strength = 0.125

boids_x=[random.uniform(x_position_limits[0],x_position_limits[1]) for x in range(boid_count)] 
boids_y=[random.uniform(y_position_limits[0],y_position_limits[1]) for x in range(boid_count)] 
boid_x_velocities=[random.uniform(x_velocity_limits[0],x_velocity_limits[1]) for x in range(boid_count)] 
boid_y_velocities=[random.uniform(y_velocity_limits[0],y_velocity_limits[1]) for x in range(boid_count)] 
boids=(boids_x,boids_y,boid_x_velocities,boid_y_velocities)

def update_boids(boids): 
    xs,ys,xvs,yvs=boids
    # Fly towards the middle 
    for i in range(boid_count):
        for j in range(boid_count): 
            xvs[i]=xvs[i]+(xs[j]-xs[i])*move_to_middle_strength/len(xs)
    for i in range(boid_count):
        for j in range(boid_count): 
            yvs[i]=yvs[i]+(ys[j]-ys[i])*move_to_middle_strength/len(xs)
    # Fly away from nearby boids
    for i in range(boid_count):
        for j in range(boid_count):
            if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < alert_distance: 
                xvs[i]=xvs[i]+(xs[i]-xs[j]) 
                yvs[i]=yvs[i]+(ys[i]-ys[j])
    # Try to match speed with nearby boids
    for i in range(boid_count):
        for j in range(boid_count):
            if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < formation_flying_distance: 
                xvs[i]=xvs[i]+(xvs[j]-xvs[i])*formation_flying_strength/len(xs) 
                yvs[i]=yvs[i]+(yvs[j]-yvs[i])*formation_flying_strength/len(xs)
    # Move according to velocities
    for i in range(boid_count): 
        xs[i]=xs[i]+xvs[i] 
        ys[i]=ys[i]+yvs[i]

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