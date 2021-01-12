#!/usr/bin/python3

import subprocess
import re

from dataclasses import dataclass
from operator import attrgetter

@dataclass
class Device:
  parent_id: int
  id: int
  name: str

process = subprocess.Popen('aconnect -i -l'.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

device_list_o = output.decode('utf-8')

device_blacklist = ['Timer', 'Through', 'Announce', 'Network']

regex = r" +(\d)\s'([^']+)'|client (\d+)"

matches = re.findall(regex,device_list_o) 

devices = []
current_parent = 0
for match in matches:

  # A line with client showed up
  if match[2] != '':
    current_parent = int(match[2])
    continue

  # Only process files not in blacklist
  if any(term for term in device_blacklist if (term in match[1])):
    continue
  devices.append(Device(current_parent, match[0], match[1]))


device_types = list(set([x.name for x in devices]))
print(f"Device types: {device_types}")
unique_devices = []

for device_type in device_types:
  latest_device = max([x for x in devices if x.name == device_type], key=attrgetter('id'))
  unique_devices.append(latest_device)

for d_i in unique_devices:
  for d_j in unique_devices:
    if d_i == d_j:
      continue
    print(f"Connecting {d_i.parent_id}:{d_i.id} to {d_j.parent_id}:{d_j.id}")
    process = subprocess.Popen(f'aconnect {d_i.parent_id}:{d_i.id} {d_j.parent_id}:{d_j.id}'.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
