from importlib.util import spec_from_file_location, module_from_spec
import os

code_path = os.path.join(os.path.dirname(__file__), "..", "Code", "02_largest_of_three.py")
spec = spec_from_file_location("largest_of_three", code_path)
module = module_from_spec(spec)
spec.loader.exec_module(module)

assert module.find_largest(10, 20, 15) == 20
assert module.find_largest(5, 5, 2) == 5
assert module.find_largest(-1, -5, -3) == -1

print("All test cases passed.")