# Author: Lydia MacBride, 19333944

from generators import *

# Import token
import credentials


# Constants
gh = Github(credentials.token)


# Main
if __name__ == "__main__":

    # TODO: Prompt for username
    gh_username = "Amy-CoolDog"

    # Request data for given username
    print("Starting API Access")
    gh_user = gh.get_user(gh_username)

    # Get general user data and begin world gen settings generation
    gen_pack_meta(gh_username)
    gen_pack_icon(gh_username)
    mod_biomes(gh_username)
    mod_noise(gh_user)
    mod_ores(gh_user)

    # TODO: Extract interesting information from repo list
