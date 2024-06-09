import matplotlib.pyplot as plt
import numpy as np

def plot_orbits(positions, velocities, scale_factor=1e9):
    plt.figure(figsize=(15, 6))
    
    # pozycja
    plt.subplot(1, 2, 1)
    for planet_name, position_list in positions.items():
        x = [pos[0] / scale_factor for pos in position_list]
        y = [pos[1] / scale_factor for pos in position_list]
        plt.plot(x, y, label=planet_name)
    plt.scatter([0], [0], color='yellow', label='Sun', s=100)
    plt.legend()
    plt.xlabel('X Position (10^9 m)')
    plt.ylabel('Y Position (10^9 m)')
    plt.title('Planetary Orbits')
    plt.grid(True)
    plt.axis('equal')

    # predkosc
    plt.subplot(1, 2, 2)
    for planet_name, velocity_list in velocities.items():
        v = [np.linalg.norm(vel) for vel in velocity_list]
        t = np.arange(len(v))
        plt.plot(t, v, label=planet_name)
    plt.legend()
    plt.xlabel('Time Step')
    plt.ylabel('Magnitude of Velocity (m/s)')
    plt.title('Magnitude of Velocity over Time')
    plt.grid(True)

    plt.tight_layout()
    plt.show()
