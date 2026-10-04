from importlib.util import spec_from_file_location, module_from_spec
import os

code_path = os.path.join(os.path.dirname(__file__), "..", "Code", "08_reverse_number.py")
spec = spec_from_file_location("reverse_number", code_path)
module = module_from_spec(spec)
spec.loader.exec_module(module)

assert module.reverse_number(1234) == 4321
assert module.reverse_number(-567) == -765
assert module.reverse_number(100) == 1

print("All test cases passed.")