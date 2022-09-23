import json
from credentials import appid
#creating weather app
import sys

if len(sys.argv)<2:
    grad=input("Choose town: ")
else:
    grad=sys.argv[1]

print(sys.executable)