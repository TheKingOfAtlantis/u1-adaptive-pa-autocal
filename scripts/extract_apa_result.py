import re
import numpy as np

# Fill with console output after running all APA_FINISH_CELL macros
console_output = """
"""

pattern = r"([0-9.]+), ([0-9.]+), ([0-9.]+)"
result = re.findall(pattern, console_output)

print("# Orca adaptive PA:")
for line in result:
    print(",".join(line))

result = np.array(result, dtype='f')
static_k = np.median(result[:,0])
print(f"Static K*: {static_k:.3f}")
print(f"Overhang Static K*: {static_k/2:.3f}")
