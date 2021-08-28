seoul_milk = { "liter" : 1, "price" : 2500 }
maeil_milk = { "liter" : 1.8, "price" : 4200 }

def get_price_per_liter(milk):
    return (milk["price"] / milk["liter"])

seoul_price = get_price_per_liter(seoul_milk)
maeil_price = get_price_per_liter(maeil_milk)

print(f"서울우유 : {seoul_price}")
print(f"매일우유 : {maeil_price}")

if (seoul_price < maeil_price):
    print("서울우유가 저렴")
else:
    print("매일우유가 저렴")
