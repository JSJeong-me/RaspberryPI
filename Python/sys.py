import platform
import os

print(platform.system())
print(platform.architecture())
print(os.name)

bus, xxx = platform.architecture()
print(bus)
print(xxx)