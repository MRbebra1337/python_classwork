import requests
import inspect
import sys

for module_name, module_path in sys.modules.items():
    print(module_name, module_path)

for _ in dir(__builtins__):
    print(_)
print(sys.argv)
print(sys.platform)
print(sys.executable)
print(sys.version)

print(inspect.ismodule(requests))
print(inspect.isclass(requests))
print(inspect.isfunction(requests))
