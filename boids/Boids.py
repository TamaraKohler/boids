import numpy as np

class Boids(object):
    def __init__(self, position_limits = np.array([[-450,300.0],[50.0,600.0]]), velocity_limits = np.array([[0,-20.0],[10.0,20.0]]), boid_count = 50, move_to_middle_strength = 0.01, alert_distance = 100, formation_flying_distance = 1000, formation_flying_strength = 0.125):
        self.boid_count = boid_count
        self.positions = self.new_flock(position_limits[0,:],position_limits[1,:])
        self.velocities = self.new_flock(velocity_limits[0,:],velocity_limits[1,:])
        self.move_to_middle_strength = move_to_middle_strength
        self.alert_distance = alert_distance
        self.formation_flying_distance = formation_flying_distance
        self.formation_flying_strength = formation_flying_strength

    # Method to create a new flock
    def new_flock(self, lower_limits, upper_limits):
        width=upper_limits-lower_limits
        return (lower_limits[:,np.newaxis] + np.random.rand(2, self.boid_count)*width[:,np.newaxis])

    # Method to encode the behaviour that boids fly to the middle of the flock
    def fly_towards_middle(self):
        middle_of_boids = np.mean(self.positions,1)
        direction_to_middle = self.positions - middle_of_boids[:,np.newaxis]
        self.velocities -= direction_to_middle * self.move_to_middle_strength	

    # Method to find the square of the distances between boids
    def square_distances(self):
        boid_separations = self.positions[:,np.newaxis,:] - self.positions[:,:,np.newaxis]
        squared_displacements = boid_separations * boid_separations
        square_distance = np.sum(squared_displacements,0)
        return square_distance

    # Method to ensure boids don’t collide with each other
    def avoid_collisions(self):
        close_birds = self.square_distances() < self.alert_distance
        separations_if_close = self.positions[:,np.newaxis,:] - self.positions[:,:,np.newaxis]
        far_away  = np.logical_not(close_birds)
        separations_if_close[0,:,:][far_away] = 0
        separations_if_close[1,:,:][far_away] = 0
        self.velocities += np.sum(separations_if_close,1)

    # Method to keep boids moving at similar speeds
    def match_speed_boids(self):
        velocity_differences = self.velocities[:,np.newaxis,:] - self.velocities[:,:,np.newaxis]
        very_far= self.square_distances() > self.formation_flying_distance
        velocity_differences_if_close = np.copy(velocity_differences)
        velocity_differences_if_close[0,:,:][very_far] =0
        velocity_differences_if_close[1,:,:][very_far] =0
        self.velocities -= np.mean(velocity_differences_if_close, 1) * self.formation_flying_strength

    # Method to update the boids’ speed 
    def update_boids(self): 
        self.fly_towards_middle()	
        self.avoid_collisions()
        self.match_speed_boids()
        self.positions += self.velocities