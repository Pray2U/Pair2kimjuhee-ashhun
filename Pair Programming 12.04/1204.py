# -*- coding: utf-8 -*-
"""1204.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11rhtqimarAgSVfdt-nLIJPHtdzInUI6x
"""

from itertools import permutations
a = "aya", "ye", "woo", "ma"
b = []
for item in permutations(a, 2):
  b.append(item)
print(b)

def solution(babbling):
  b = []
  count = 0
  for i in range(1,5):
    for item in permutations(a, i):
      b.append(''.join(item))
  print(b)
  for i in babbling:
    if i in b:
      count += 1
  return count

solution(["aya", "yee", "u", "maa", "wyeoo"])

solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"])

num = 4
total = 14
result = []
a = int(total/num)
b = a + 1
result.append(a)
result.append(b)
if a * num != total:
  for i in range(int((num-1)/2)):
    result.append(b+1)
    result.append(a-1)
print(result)

def solution(num, total):
  result = []
  a = int(total/num)
  if a * num != total: 
    b = a + 1 
    result.append(a)
    result.append(b)
    for i in range(int((num-1)/2)):
      result.append(b+1)
      result.append(a-1)
      a -= 1
      b += 1
  else:
    result.append(a)
    c = a
    for i in range(int((num-1)/2)):
      result.append(c-1)
      result.append(a+1)
      c -= 1
      a += 1
  result.sort()
  return result

solution(3, 12)

solution(5, 5)

solution(4, 14)