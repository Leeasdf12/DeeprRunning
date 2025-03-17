# -*- coding: utf-8 -*-
"""(03-17) 이민성 오전 과제.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1yMO6EhPuqEgdPHYYBLTbgE41tsZZQQYL

# 변수

값을 저장하는 공간

# *숫자형*
*  '='는 변수에 대입
"""

#정수형
a = 123

#실수형
a = 1.2

#8진수
a = 0o177

#16진수
a = 0x8ff

""" * 정수, 실수, 8진수와 16진수로 나뉨


"""

a = 3
b = 4
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** b)
print(a % b)
print(a // b)

"""*  사칙 연산(+, -, *, /)
* 제곱 (**), 나눗셈(%), 나눗셈 후 몫 리턴 (//) 등이 있음
* 복합연산자(+=, -=, *=, /=, //=, %=, **=)도 있음

# *문자열*
"""

"Hello World"
'Python is fun'
"""Life is too short, You need python"""
'''Life is too short, You need python'''

"""*   ("", '', ''',''') 로 문자열 생성"""

multiline = "Life is too short\nYou need python"
print(multiline)

"""
*   이스케이프 코드 (\n, \t, \\, \', \") 사용하여 보기 좋게 출력 가능"""

head = "Python"
tail = " is fun!"
print(head + tail)

"""*   변수에 저장한 문자열 (+)로 더하기 가능"""

a = "python"
a * 2
print(a)

"""*   변수에 저장한 문자열 (*)로 곱하기 가능"""

a = "Life is too short"
len(a)

"""* 문자열 길이(len) 추출"""

a = "Life is too short, You need Python"
print(a[0])
print(a[12])
print(a[-1])

"""*   문자열 인덱싱같은 경우 공백을 포함한 배열로 생각하면 된다 파이썬의 경우 (-)로 역순 가능"""

a = "Life is too short, You need Python"
print(a[0:4])
print(a[:17])

"""*   슬라이싱
  1.   0부터 표현하고 싶은 문자 위치+1로 가능 (a[0:5])
  2.   공백을 줄 경우 처음 or 마지막 까지 ([:5])

# *포매팅*
"""

#숫자 바로 대입
print("I eat %d apples." % 3)

#문자열 바로 대입
print("I eat %s apples." % "five")

#숫자 변수로 대입
number = 3
print("I eat %d apples." % number)

"""*  문자열(%s), 문자(%c), 정수(%d), 부동소수(%f), 8진수(%o), 16진수(%x)
   문자 % 자체출력(%%)
*  실사용에선 %s로 만능 사용 가능
"""

"%0.4f" % 3.42134234

"""*  소수점 자릿수 표현방식 (0.4)는 소숫점 네번째 자리까지라는 의미"""

"I eat {0} apples".format(3)

"""*  format 함수로도 포매팅 가능"""

#왼쪽 정렬
print("{0:<10}".format("hi"))
#오른쪽 정렬
print("{0:>10}".format("hi"))
#가운 정렬
print("{0:^10}".format("hi"))

"""* 출력시 줄맞출때 용이한 정렬"""

#!로 공백 채우기
print("{0:!<20}".format('안녕'))

"""*  특정 문자로 공백 채우기 가능"""

name = '홍길동'
age = 30
print(f"나의 이름은 {name}입니다. 나이는 {age}입니다.")

"""*   f 문자열 포매팅
  1.   문자열 앞에 f를 붙혀 생성할 수 있다.
  2.   위와 같이 변숫값을 바로 참조 할 수 있다.

# *문자열 관련 함수*
"""

a = "hobby"
a.count('b')

"""* 특정 문자의 개수를 셀 수 있다."""

a = "Python is the best choice"
print(a.find('b'))
print(a.find('k'))

"""* 특정 문자의 위치를 알수 있고 존재하지 않으면 -1 반환. (index 방식은 오류를 발생시킴)"""

",".join('abcd')

"""* 문자 사이에 특정 문자를 넣을 수 있다."""

#소문자를 대문자로
a = "hi"
print(a)
print(a.upper())
print("\n")

#대문자를 소문자로
a = "HI"
print(a)
print(a.lower())
print("\n")

#왼쪽 공백 지우기
a = " hi "
print(a)
print(a.lstrip())
print("\n")

#오른쪽 공백 지우기
a = " hi "
print(a)
print(a.rstrip())
print("\n")

#양쪽 공백 지우기
a = " hi "
print(a)
print(a.strip())
print("\n")

"""* 상황에 맞게 유용하게 사용할 수 있는 함수들"""

#문자열 바꾸기
a = "Life is too short"
print(a)
print(a.replace("Life", "Your leg"))

"""* 특정 문자열을 바꿀 때 사용할 수 있다."""

a = "Life is too short"
a.split()

"""* 아무것도 넣지 않으면 공백을 기준으로 문자열을 나누어 준다"""

b = "a:b:c:d"
b.split(':')

"""* (:)를 기준으로 문자열을 나누어 주었다."""

a = input()

print("입력한 내용 : %s" % a)

"""* input() 함수로 사용자에게 입력 받을 수 있다
* input() 안에 문자열을 넣는 것으로 안내 문구를 적을 수 있다.
"""