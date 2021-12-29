# Various utilities related to handling json files
# Author: Lydia MacBride, 19333944

import json
import os


# File paths
# Input files
IN_BASE = "./vanilla_worldgen/"
IN_CONTENT = IN_BASE + "data/minecraft/worldgen/"
IN_BIOME = IN_CONTENT + "biome/"
IN_NOISE = IN_CONTENT + "noise_settings/"
IN_FEATURES = IN_CONTENT + "configured_feature/"

# Output files
OUT_BASE = "./github_worldgen/"
OUT_ICON = OUT_BASE + "pack.png"
OUT_PACK = OUT_BASE + "pack.mcmeta"
OUT_CONTENT = OUT_BASE + "data/minecraft/worldgen/"
OUT_BIOME = OUT_CONTENT + "biome/"
OUT_NOISE = OUT_CONTENT + "noise_settings/"
OUT_FEATURES = OUT_CONTENT + "configured_feature/"


# Loads vanilla_worldgen/worldgen/biome/plains.json
def load_json(filename):
    print("Loading json: " + filename)

    with open(filename) as f:
        data = json.load(f)

    return data


# Save dictionary as json file
def save_json(filename, data):
    print("Saving json: " + filename)

    # Check if path exists, if not, create it
    path = '/'.join(filename.split("/")[:-1])
    if not os.path.exists(path) and path != "":
        os.makedirs(path)

    with open(filename, 'w') as json_file:
        json.dump(data, json_file)


# This is for testing purposes only
if __name__ == "__main__":
    print("Testing purposes only!!!")
