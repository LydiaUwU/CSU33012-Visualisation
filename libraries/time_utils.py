
# Various utilities related to time and date
# Author: Lydia MacBride, 19333944

import datetime

# Constants
GITHUB_LAUNCH = datetime.date(2008, 4, 10)


# Get time since github launch
def time_since_launch():
    return datetime.timedelta.total_seconds(datetime.date.today() - GITHUB_LAUNCH)


# Get time github account was created
def time_account_age(user):
    return datetime.timedelta.total_seconds(datetime.date.today() - user.created_at.date())


# Get percentage of Github's uptime account has existed for
def acc_exist_prop(user):
    return time_account_age(user) / time_since_launch()


# This is for testing purposes only
if __name__ == "__main__":
    print("Testing purposes only!!!")

    user_test = gh.get_user("LydiaUwU")
    print(user_test.created_at)

    print(time_since_launch())
    print(time_account_age(user_test))
    print(acc_exist_prop(user_test))
