import numpy as np
from matplotlib import pyplot as plt
import matplotlib.gridspec as gridspec


# Initialise values
n = 10000 # Number of needles
l = 5/6 # Length of needle
t = 1 # Distance between lines
h = 0 # Number of needles that cross a line
h_record = [] # Record the number of needles that cross a line for each iteration

boundary = { # Boundary of the grid, start at 0,0
    "x": 10,
    "y": 10
}

def lines(t, boundary): # Generate the lines
    return np.arange(t, boundary["x"], t)

lines = lines(t, boundary)

def drop_needle(l, lines, boundary): # Drop the needle
    pos_start = np.random.rand(2) * [boundary["x"], boundary["y"]] # Random position for the start of the needle
    direction = np.random.rand() * 2 * np.pi # Random direction for the needle
    pos_end = pos_start + [np.cos(direction) * l, np.sin(direction) * l] # Calculate the end position of the needle
    if pos_end[0] > boundary["x"]:
        pos_end[0] = boundary["x"] - (pos_end[0] - boundary["x"])
    if pos_end[1] > boundary["y"]:
        pos_end[1] = boundary["y"] - (pos_end[1] - boundary["y"])
    if pos_end[0] < 0:
        pos_end[0] = abs(pos_end[0])
    if pos_end[1] < 0:
        pos_end[1] = abs(pos_end[1])
    
    # Check if the needle crosses a line
    crosses_line = False
    for line in lines:
        if (pos_start[0] < line and pos_end[0] > line) or (pos_start[0] > line and pos_end[0] < line):
            crosses_line = True
            break
    
    return {"start": pos_start, "end": pos_end}, crosses_line

# Drop the needles
needles = []
for _ in range(n):
    needle, crosses_line = drop_needle(l, lines, boundary)
    needles.append(needle)
    if crosses_line:
        h += 1
        h_record.append(h)
    else:
        h_record.append(h)
        
# Estimate pi
pi_estimate = (2 * l * n) / (t * h)

# Calculate the difference between the estimate and the real value of pi over time
differences = []
for i, h_current in enumerate(h_record):
    if h_current == 0:
        differences.append(None)
        continue
    current_estimated_pi = (2 * l * (i+1)) / (t * h_current)
    differences.append(abs(np.pi - current_estimated_pi))

# Create a 3x3 grid
gs = gridspec.GridSpec(3, 3)

# Plot the needles
ax1 = plt.subplot(gs[:2, :2])
ax1.set_xlim(0, boundary["x"])
ax1.set_ylim(0, boundary["y"])
ax1.axis('equal')

for line in lines:
    ax1.axvline(line, color='gray', linestyle='--')

for needle in needles:
    ax1.plot([needle["start"][0], needle["end"][0]], [needle["start"][1], needle["end"][1]])

# Draw a box around the grid
ax1.plot([0, 0, boundary["x"], boundary["x"], 0], [0, boundary["y"], boundary["y"], 0, 0], color='black')


# Write the results
ax2 = plt.subplot(gs[:2, 2])
ax2.axis('off')

ax2.text(0.1, 0.9, f"Needles: {n}")
ax2.text(0.1, 0.8, f"Length: {l}")
ax2.text(0.1, 0.7, f"Distance: {t}")
ax2.text(0.1, 0.6, f"Crosses: {h}")
ax2.text(0.1, 0.5, f"Pi: {pi_estimate}")

# Plot the difference between the estimate and the real value of pi
ax3 = plt.subplot(gs[2, :])  

ax3.plot(differences)
ax3.set_yscale('log')
ax3.set_xlabel('No. Needles')
ax3.set_ylabel('Difference to pi')

plt.tight_layout()
plt.show()