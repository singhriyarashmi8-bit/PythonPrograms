import importlib.util

spec = importlib.util.spec_from_file_location("find_duplicates", "Code/19-find-duplicates.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert sorted(module.find_duplicates([1, 2, 3, 2, 4, 5, 1])) == [1, 2]
assert module.find_duplicates([1, 2, 3, 4]) == []
assert module.find_duplicates([5, 5, 5]) == [5]

print("All test cases passed!")