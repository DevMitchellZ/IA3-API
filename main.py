# main.py | M.Z-2022

import sys

sys.path.insert(0, r"C:\Users\mitch\Documents\Git Repositories\IA3-API\API")
sys.path.insert(0, r"C:\Users\mitch\Documents\Git Repositories\IA3-API\UI")


from poll import poll
pollapi=poll.apipoll()

def __init__():
    try:
        pollapi()
    except:
        return