def flunk(s):
    return s < 60

def myfilter(fn, data):
    new_data = []
    for e in data:
        if (fn(e)):
            new_data.append(e)
    return new_data    

score = [ 45, 89, 72, 53, 94 ]

for s in myfilter(flunk, score):
    print(s)
