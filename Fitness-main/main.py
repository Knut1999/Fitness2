import argparse
from Controller import Controller

parser = argparse.ArgumentParser()

parser.add_argument("--profiles", required=True)
parser.add_argument("--sessions", required=True)
parser.add_argument("--output", required=True)

args = parser.parse_args()

controller = Controller(args.profiles,args.sessions,args.output)