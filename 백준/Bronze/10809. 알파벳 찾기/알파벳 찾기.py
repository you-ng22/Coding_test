# #알파벳 찾기
import string
s = input()

for alphabet in string.ascii_lowercase:
    print(s.find(alphabet), end=' ')