import requests
import sys

r = requests.get("http://vcm-3591.vm.duke.edu:5000/name")
name = r.json()
sys.stdout.write(str(name) + '\n')

r2 = requests.get("http://vcm-3591.vm.duke.edu:5000/hello/Ethan")
hello = r2.json()
sys.stdout.write(str(hello) + '\n')

r3 = requests.post("http://vcm-3591.vm.duke.edu:5000/distance",
                   json={"a": [1, 2], "b": [3, 4]})
distance = r3.json()
sys.stdout.write(str(distance) + '\n')
