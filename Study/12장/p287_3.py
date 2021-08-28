# 밑면이 8이고 높이가 5인 직각삼각형의 빗변 길이를 구하라.

from math import sqrt, pow

def get_hypotenuse(len1, len2):
    return sqrt(pow(len1, 2) + pow(len2, 2))

base = 8
height = 5
print(get_hypotenuse(base, height))
