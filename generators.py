# File generators
# Author: Lydia MacBride

from PIL import Image
from colour_utils import *
from json_utils import *
from time_utils import *


# Generate pack.png based on user's pfp
def gen_pack_icon(username):
    print("Generating pack.png")

    # Get and resize users pfp
    i = Image.fromarray(np.array(imageio.imread("https://github.com/" + username + ".png")))
    i = i.resize((64, 64))

    # Save image
    i.save(OUT_ICON)


# Generate pack.mcmeta
def gen_pack_meta(username):
    print("Generating pack.mcmeta")

    save_json(OUT_PACK, {"pack": {"pack_format": 8, "description": "Worldgen based on " + username}})


# TODO: Noise setting modification
def mod_noise(user):
    print("Modifying noise parameters")

    for f in os.listdir(IN_NOISE):
        print("Modifying " + IN_NOISE + str(f))

        # Load file (json to dict)
        d = load_json(IN_NOISE + str(f))

        # Set noise:sampling:height
        d.get("noise").get("sampling")["y_scale"] = acc_exist_prop(user)

        # Store modified file (dict to json)
        save_json(OUT_NOISE + str(f), d)


# Update biomes
def mod_biomes(username):
    print("Modifying biome parameters")

    for f in os.listdir(IN_BIOME):
        print("Modifying " + IN_BIOME + str(f))

        # Load file (json to dict)
        d = load_json(IN_BIOME + str(f))

        # Modify world colours
        d.get("effects")["grass_color_modifier"] = "none"
        d.get("effects")["sky_color"] = get_pfp_colour(username).dec()
        d.get("effects")["fog_color"] = get_pfp_colour(username).dec()
        d.get("effects")["water_color"] = get_pfp_colour(username).dec()
        d.get("effects")["water_fog_color"] = get_pfp_colour(username).dec()
        d.get("effects")["grass_color"] = get_pfp_colour(username).compliment().dec()
        d.get("effects")["foliage_color"] = get_pfp_colour(username).compliment().dec()  # TODO: Only changes oak trees

        # Store modified file (dict to json)
        save_json(OUT_BIOME + str(f), d)


# TODO: Modify ore generation
def mod_ores(user):
    print("Modifying ore parameters")

    # TODO: Log scale for each of the following

    # TODO: Diamonds based on PRs
    pull_count = sum(map(lambda x: x.get_pulls().totalCount, user.get_repos()))
    print("Pulls: " + str(pull_count))

    # TODO: Redstone based on commits
    commit_count = sum(map(lambda x: x.get_commits().totalCount, user.get_repos()))
    print("Commits: " + str(commit_count))

    # TODO: Gold based on followers
    follower_count = user.get_followers().totalCount
    print("Followers: " + str(follower_count))

    # TODO: Iron based on repo count
    repo_count = user.get_repos().totalCount
    print("Repos: " + str(repo_count))

    # TODO: Lapis based on stars
    star_count = sum(map(lambda x: x.get_stargazers().totalCount, user.get_repos()))
    print("Stars: " + str(star_count))


# This is for testing purposes only
if __name__ == "__main__":
    print("Testing purposes only!!!")

    mod_ores(gh.get_user("LydiaUwU"))
