class Reverse:
    def reverse_by_words(self, s):
        return ' '.join(reversed(s.split()))


print(Reverse().reverse_by_words('My name is Abhinav Tyagi'))