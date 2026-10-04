from importlib.util import spec_from_file_location, module_from_spec
import os

code_path = os.path.join(os.path.dirname(__file__), "..", "Code", "07_primes_in_range.py")
spec = spec_from_file_location("primes_in_range", code_path)
module = module_from_spec(spec)
spec.loader.exec_module(module)

assert module.get_primes_in_range(10, 20) == [11, 13, 17, 19]
assert module.get_primes_in_range(1, 5) == [2, 3, 5]
assert module.get_primes_in_range(20, 25) == [23]

print("All test cases passed.")