from importlib.util import spec_from_file_location, module_from_spec
import os

code_path = os.path.join(os.path.dirname(__file__), "..", "Code", "05_fibonacci.py")
spec = spec_from_file_location("fibonacci", code_path)
module = module_from_spec(spec)
spec.loader.exec_module(module)

assert module.generate_fibonacci(5) == [0, 1, 1, 2, 3]
assert module.generate_fibonacci(1) == [0]
assert module.generate_fibonacci(0) == []

print("All test cases passed.")