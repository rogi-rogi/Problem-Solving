# 04 저축.py
# https://school.programmers.co.kr/learn/courses/19274/lessons/240599

start = int(input())
before = int(input())
after = int(input())

money = start
month = 1
while money < 70:
    money += before
    month += 1
while money < 100:
    money += after
    month += 1
print(month)
