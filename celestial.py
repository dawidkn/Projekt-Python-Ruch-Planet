import numpy as np
import matplotlib.pyplot as plt

class CelestialBody:
    
    def __init__(self, name, mass, position, velocity):
        self.name = name
        self.mass = mass
        self.position = np.array(position, dtype='float64')
        self.velocity = np.array(velocity, dtype='float64')

class Star(CelestialBody):

    def __init__(self, name, mass, position):
        super().__init__(name, mass, position, [0, 0])

class Planet(CelestialBody):

    def __init__(self, name, mass, position, velocity):
        super().__init__(name, mass, position, velocity)

def gravitational_force(star, planet):

    G = 6.67430e-11 

    direction = star.position - planet.position
    distance_squared = np.sum(direction ** 2)
    distance = np.sqrt(distance_squared)
    force_magnitude = G * (planet.mass * star.mass) / distance_squared
    force_direction = direction / distance
    force = force_direction * force_magnitude

    return force

def simulate(planets, star, iterations, dt):

    positions = {planet.name: [] for planet in planets}
    velocities = {planet.name: [] for planet in planets}


    for _ in range(iterations):
        for planet in planets:
            force = gravitational_force(star, planet)
            acceleration = force / planet.mass
            planet.velocity += acceleration * dt
            planet.position += planet.velocity * dt 
            positions[planet.name].append(planet.position.copy())
            velocities[planet.name].append(planet.velocity.copy())  

    return positions, velocities