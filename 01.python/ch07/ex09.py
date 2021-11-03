# 사전의 언팩

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
    
dic = {
    'begin' : 1,
    'end' : 100,
    'step' : 2
}

# dict의 펼침 : **사전명
print(calcstep(**dic))
print(*dic) # 키들만 언팩되어 인자로 전달됨
# print(**dic)

''' stdout
<class 'dict'>
{'begin': 1, 'end': 100, 'step': 2}
2500
begin end step
'''
