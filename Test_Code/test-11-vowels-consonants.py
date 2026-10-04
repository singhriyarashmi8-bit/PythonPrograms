import importlib.util

spec = importlib.util.spec_from_file_location("vowels-consonants", "Code/11-vowels-consonants.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.count_vowels_consonants("Hello") == (2, 3)
assert module.count_vowels_consonants("Python") == (1, 5)
assert module.count_vowels_consonants("AEIOU") == (5, 0)
assert module.count_vowels_consonants("abc") == (1, 2)
assert module.count_vowels_consonants("123") == (0, 0)

print("All test cases passed.")

