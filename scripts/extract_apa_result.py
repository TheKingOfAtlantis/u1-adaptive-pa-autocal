import re

# Fill with console output after running all APA_FINISH_CELL macros
input = """
"""

pattern = r"([0-9.]+), ([0-9.]+), ([0-9.]+)"
result = re.findall(pattern, input)

print("# Orca adaptive PA:")
for line in result:
    print(",".join(line))
