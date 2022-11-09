#팰린드롬수
#어떤 단어를 뒤에서부터 읽어도 똑같다면 그 단어를 팰린드롬이라고 한다. 'radar', 'sees'는 팰린드롬이다.

def palindrome(strings):
    if strings == strings[::-1]:
        answer = 'yes'
    else:
        answer = 'no'
    return answer

if __name__ == '__main__':
    while True:
        strings = input()
        if strings == '0':
            break
        print(palindrome(strings))