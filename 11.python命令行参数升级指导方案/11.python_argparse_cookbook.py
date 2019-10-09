import argparse

a = [1, 2]

parser = argparse.ArgumentParser(description='python argparse cookbook')

# parser.add_argument('user', help="input username")
# parser.add_argument('pwd', help="input password")
# parser.add_argument('-v', '--version', action='store_true', help="get version")
# parser.add_argument('-t', '--type', choices=['install','uninstall','start','stop'])
parser.add_argument('-p', '--port', type=int)
parser.add_argument('-u','--user',required=True,help="input username")

args = parser.parse_args()
print(args)


