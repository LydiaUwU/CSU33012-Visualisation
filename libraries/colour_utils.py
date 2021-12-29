# Various utilities related colours
# Author: Lydia MacBride, 19333944

import imageio
import numpy as np
from matplotlib import colors


# Classes
# Colour class
class Colour:
    def __init__(self, colour):
        self.colour = colour
        self.r = colour[0]
        self.g = colour[1]
        self.b = colour[2]

    # Find compliment
    def compliment(self):
        return Colour(np.array(list(map(lambda x: 255 - x, self.colour))))

    # Return colour as hex
    def hex(self):
        return colors.to_hex(np.true_divide(self.colour, 255))

    # Return colour as decimal
    def dec(self):
        return int(str(self.hex()[1:]), 16)

    pass


# Get average colour (in hex) of user pfp
# This sets the sky colour
def get_pfp_colour(username):
    # Get user profile picture and store in a numpy array
    pfp = np.array(imageio.imread("https://github.com/" + username + ".png"))[:, :, :3]

    # Find average colour of pfp
    avg_c_row = np.average(pfp, axis=0)
    avg_c = np.average(avg_c_row, axis=0)

    # Convert RGB to hex and return
    return Colour(avg_c)


# This is for testing purposes only
if __name__ == "__main__":
    print("Testing purposes only!!!")

    username_test = "LydiaUwU"  # "Amy-CoolDog"

    colour_test = get_pfp_colour(username_test)
    print(colour_test.colour)
    print(colour_test.hex())
    print(colour_test.compliment().hex())

    print(colour_test.dec())
