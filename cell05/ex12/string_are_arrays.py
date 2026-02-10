#!/usr/bin/env python3
import sys

if len(sys.argv) < 2:
    print("none")
else:
    text = sys.argv[1]
    result = ""

    for i in text:
        if i == 'z':
            result += 'z'
    
    if result == "":
        print("none")
    else:
        print(result)
