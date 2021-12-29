# GH2MC
# Create a Minecraft 1.18.X worldgen datapack based on information pulled from the GitHub API
# Created for CSU33012
#
# Author: Lydia MacBride, 19333944
#
# 😺

import sys
from libraries.generators import *


# Main
if __name__ == "__main__":
    # Load or ask for token
    token = ""

    if not os.path.exists("credentials.json"):
        token = input("Input your GitHub token: ")
        save_json("credentials.json", {"token": token})
    else:
        d = load_json("credentials.json")
        token = d.get("token")

    gh = Github(token)

    # Check for properly formed command call
    if len(sys.argv) != 2:
        print("Incorrect command usage, should be: ./gh2mc \"username\"")
        quit()

    # Receive username from command line argument
    gh_username = str(sys.argv[1])

    # Request data for given username
    print("Starting API Access")
    gh_user = gh.get_user(gh_username)

    # Get general user data and begin world gen settings generation
    gen_pack_meta(gh_username)
    gen_pack_icon(gh_username)
    mod_biomes(gh_username)
    mod_noise(gh_user)
    mod_ores(gh_user)

    print("All done! See README.md for datapack installation instructions")
