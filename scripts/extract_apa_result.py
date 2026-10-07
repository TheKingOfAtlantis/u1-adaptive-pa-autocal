import re
import numpy as np
import argparse

p = argparse.ArgumentParser(
    description="Extracts orca adaptive PA and static PA values"
)
p.add_argument(
    "file",
    default=None,
    help="File containing the console output from running the APA_FINISH_CELL command(s)",
)
args = p.parse_args()

console_output = ""
with open(args.file) as file:
    console_output = file.readlines()
    console_output = "\n".join(console_output)

pattern = r"([0-9.]+), ([0-9.]+), ([0-9.]+)"
result = re.findall(pattern, console_output)

result = np.array(result, dtype='f')
static_k = np.median(result[:,0])
print(f"Static K*: {static_k:.3f}")
print(f"Overhang Static K*: {static_k/2:.3f}")

print("\nOrca adaptive PA:")
for i in range(len(result)):
    print(",".join(result[i].astype('str')))
