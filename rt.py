import math

import numpy as np
from klongpy import KlongInterpreter

klong = KlongInterpreter()

klong('.l("rt.kg")')

pixels = klong["pixels"]

with open("out.ppm", "w") as f:
    print("P3", file=f)
    print(f"{klong['w']} {klong['h']}", file=f)
    print("255", file=f)

    for pixel in pixels:
        for color in pixel:
            print(f"{math.floor(255 * color)} ", file=f, end="")
        print("", file=f)
