

import re
import numpy as np

# Fill with console output
input = """

"""

startMarker = "=== APA TEST POINT START ==="

tests = input.split(startMarker)

for test in tests[1:]:
    # Extract k/area lines
    k_areas = []
    k_pattern = r"k([0-9.]+): area=([-\d.]+)"
    k_matches = re.findall(k_pattern, test)
    k_areas.extend([(float(k), float(area)) for k, area in k_matches])
    k_areas = np.array(k_areas)

    max_abs = np.max(np.abs(k_areas[:, 1]))
    k0_k1_boundry = np.sum(k_areas[:, 1] > 0)

    A0 = k_areas[k0_k1_boundry - 1, 1]
    k0 = k_areas[k0_k1_boundry - 1, 0]

    K1 = k_areas[k0_k1_boundry, 0]
    A1 = k_areas[k0_k1_boundry, 1]

    apa_finish_pattern = r"APA_FINISH_CELL K0= A0= K1= A1= FLOW=([0-9.]+) ACCEL=([0-9.]+) NAME=(\w+) MAX_ABS="
    apa_finish_matches = re.findall(apa_finish_pattern, test)[0]

    flow, accel, name = apa_finish_matches

    print(f"APA_FINISH_CELL K0={k0} A0={A0} K1={K1} A1={A1} FLOW={flow} ACCEL={accel} NAME={name} MAX_ABS={max_abs}")
