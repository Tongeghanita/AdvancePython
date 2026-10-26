# Name: Ghanita Tonge
# Roll No: 19

import re

text = """Pune - 411001
Mumbai - 400001
Delhi - 110001
Invalid PIN - 012345
Invalid PIN - 41100"""

pins = re.findall(r'\b[1-9]\d{5}\b', text)

print("Valid PIN Codes:")
for pin in pins:
    print(pin)
