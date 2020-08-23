class py_reverse:
    def reverse_words(self, s):
        return ' '.join(reversed(s.split()))


print(py_reverse().reverse_words('hello .py'))
print(py_reverse().reverse_words('world .py'))
print(py_reverse().reverse_words('cry .html'))
print(py_reverse().reverse_words('water .txt'))
