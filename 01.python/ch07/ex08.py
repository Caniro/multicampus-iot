# 함수 - 키워드 인수

def calcstep(**args):
    print(type(args))
    print(args)
    
    begin = args.get('begin', 0)
    end = args['end']
    step = args['step']
    total = 0
    for num in range(begin, end + 1, step):
        total += num
    return total

print("3 ~ 5 =", calcstep(begin=3, end=5, step=1), end='\n\n')
print("3 ~ 5 =", calcstep(step=1, end=5, begin=3), end='\n\n')
print(" ~ 5 =", calcstep(step=1, end=5))

''' stdout
<class 'dict'>
{'begin': 3, 'end': 5, 'step': 1}
3 ~ 5 = 12

<class 'dict'>
{'step': 1, 'end': 5, 'begin': 3}
3 ~ 5 = 12

<class 'dict'>
{'step': 1, 'end': 5}
 ~ 5 = 15
'''
