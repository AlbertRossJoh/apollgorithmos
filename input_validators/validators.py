#!/usr/bin/env python3
import re
import sys

s = input()

if not re.match(r'^[a-zA-Z]+$', s):
    sys.exit(43)

if len(s.strip()) > 100:
    sys.exit(43)

if sys.stdin.readline() != "":
    sys.exit(43)

sys.exit(42)
