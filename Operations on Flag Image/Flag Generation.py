import numpy as np
import matplotlib.pyplot as plt

def generate():
    # Set the dimensions of the flag
    height = 600
    width = 600

    # Create a 3D array of zeros
    flag = np.zeros((height, width, 3))

    # Define the colors of the flag
    saffron = np.full((height//3, width, 3), [255/255, 153/255, 51/255])  # RGB for saffron
    white = np.full((height//3, width, 3), [1, 1, 1])       # RGB for white
    green = np.full((height//3, width, 3), [0, 128/255, 0])       # RGB for green

    # Fill the first 1/3 of the flag with saffron
    flag[:height//3, :, :] = saffron

    # Fill the second 1/3 of the flag with white
    flag[height//3:2*height//3, :, :] = white

    # Fill the last 1/3 of the flag with green
    flag[2*height//3:, :, :] = green

    # Draw the Ashoka Chakra
    center = (300, 300)
    radius = 100
    num_spokes = 24
    angle_increment = 360.0 / num_spokes
    linewidth = 2
    

    # Draw the circle
    circle = plt.Circle(center, radius, color=(62/255, 62/255, 255/255), fill=False, linewidth=linewidth)
    

    # Display the flag
    #plt.imshow(flag)
    #plt.axis('off')
    dpi = 80
    height, width, depth = flag.shape
    figsize = width / float(dpi), height / float(dpi)
    fig = plt.figure(figsize=figsize)
    ax = fig.add_axes([0, 0, 1, 1])
    for i in range(num_spokes):
        angle_rad = np.deg2rad(i * angle_increment)
        x = center[0] + radius * np.cos(angle_rad)
        y = center[1] + radius * np.sin(angle_rad)
        plt.plot([center[0], x], [center[1], y], color=(62/255, 62/255, 255/255), linewidth=1)
    plt.gca().add_artist(circle)
    ax.axis('off')
    ax.imshow(flag)
    plt.show()
    #saved the above figure for future reference

generate()

