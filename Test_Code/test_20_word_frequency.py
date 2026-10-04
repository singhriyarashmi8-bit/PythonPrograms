import importlib.util

spec = importlib.util.spec_from_file_location("word_frequency", "Code/20-word-frequency.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.word_frequency("hello world hello") == {"hello": 2, "world": 1}
assert module.word_frequency("Python is great and Python is easy") == {
    "python": 2,
    "is": 2,
    "great": 1,
    "and": 1,
    "easy": 1
}
assert module.word_frequency("") == {}

print("All test cases passed!")