#!/usr/bin/python3 
import sys
import json
import random
mockThis = sys.argv[1]

output_text = ""
for char in mockThis:
  if char.isalpha():
    if random.random() > 0.5:
      output_text += char.upper()
    else:
        output_text += char.lower()
  else:
      output_text += char
  
result = { "items": [ {
    "title": output_text,
    "valid": 'TRUE',
    "arg": output_text
}]}

print (json.dumps(result))