#!/usr/bin/python3.8

import time
import click

click.clear()

try:
    while True:
        for part in ["|", "/", "-", "\\"]:
            print(f"Ctrl-C to end the spinning.  :)\n\n {part}\n")
            click.clear()
            time.sleep(0.1)
except KeyboardInterrupt:
    pass
