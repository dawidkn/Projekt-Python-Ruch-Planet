#zalozenia programu
#program nie zaklada wzajemnego oddzialywanie grawitacyjnego miedzy planetami


import celestial
from visualization import plot_orbits
import animate



sun = celestial.Star('Sun', 1.989e30, [0, 0])
earth = celestial.Planet('Earth', 5.972e24, [1.496e11, 0], [0, 29783])
jupietr_Sun = celestial.Planet('Jupiter as Sun', 1.989e30, [7.78e11, 45], [0, 2400])
mars = celestial.Planet('Mars', 6.417e23, [2.279e11, 0], [0, 24007])
    
planets = [earth, mars, jupietr_Sun]
iterations = 90000 #jak dla ziemii to najlepiej 365
dt = 50000  # jak dla ziemii to najlepiej dzien w sekundach

positions, velocity = celestial.simulate(planets, sun, iterations, dt)

plot_orbits(positions, velocity)
#animate.animate_points(positions, velocity, iterations) #nie dziala