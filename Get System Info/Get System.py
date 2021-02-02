import os, platform

print("OS name: ", os.name)
print("CPU count: ", os.cpu_count())

print()

print("Platform")
print("System: ", platform.system())
print("Release: ", platform.release())
print("Architecture: ", platform.architecture())
