from learning_locker_sdk import client, auth
import argparse
import pprint
import json

"""
Rudimentary test to check ability to retrieve and create company
via the LRS.

MUST pass both a --user and --password via the CLI 
to authenticate with the LRS

"""


def do_tests(user, password):
    zz = auth.LearningLockerAuth(
        "http://localhost:8080", "/api/auth/jwt/password", user, password
    )
    
    token = zz.get_bearer_token

    aa = client.LearningLockerSDK("http://localhost:8080", "/api/v2/", **{"Authorization": token})
    zz = aa.retrieve("organisation")
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(json.loads(zz.content))
    
    new_org = aa.create("organisation", **{"name": "Ring ring 23"})
    pp.pprint(json.loads(new_org.content))


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Learning Locker client options")
    ap.add_argument("--password", dest="password")
    ap.add_argument("--user", dest="user")
    yargs = ap.parse_args()
    do_tests(yargs.user, yargs.password)