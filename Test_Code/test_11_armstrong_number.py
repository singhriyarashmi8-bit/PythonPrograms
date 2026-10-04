from importlib.util import spec_from_file_location, module_from_spec
import os

code_path = os.path.join(os.path.dirname(__file__), "..", "Code", "11_armstrong_number.py")
spec = spec_from_file_location("armstrong_number", code_path)
module = module_from_spec(spec)
spec.loader.exec_module(module)

assert module.is_armstrong(153) == True
assert module.is_armstrong(370) == True
assert module.is_armstrong(123) == False
assert module.is_armstrong(-153) == False

print("All test cases passed.")