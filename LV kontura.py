
from shapely.geometry import Polygon
import matplotlib.pyplot as plt

# Latvia coordinates (20 points)
latvia_coordinates = [
    (21.6, 55.3),  # Kurzeme
    (21.6, 56.5),
    (21.8, 56.7),
    (22.1, 57.2),
    (22.5, 57.5),
    (22.8, 57.6),  # Kolka
    (23.3, 57.2),
    (23.6, 56.8),
    (24.0, 56.9),  # Gulf of Riga
    (24.3, 57.8),
    (25.0, 57.9),
    (25.7, 57.4),
    (26.1, 57.5),
    (26.2, 57.4),
    (26.5, 56.8),
    (26.7, 56.2),
    (26.0, 55.4),
    (25.6, 55.7),
    (24.6, 56.0),
    (23.0, 55.8),
    (22.0, 55.8),
]

# Create polygon
latvia = Polygon(latvia_coordinates)

# Plot the map
fig, ax = plt.subplots(figsize=(8, 8))

x, y = latvia.exterior.xy

ax.fill(x, y, color="lightgreen", alpha=0.7)
ax.plot(x, y, color="darkgreen", linewidth=2)

# Add title and labels
ax.set_title("Latvijas kontūras karte", fontsize=16)
ax.set_xlabel("Garuma grādi")
ax.set_ylabel("Platuma grādi")

ax.set_aspect("equal")
ax.grid(True, linestyle="--", alpha=0.4)

plt.show()


