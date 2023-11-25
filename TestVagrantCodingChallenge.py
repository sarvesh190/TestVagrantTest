def discount(unit_price,quantity):
    amount = quantity * unit_price
    if unit_price >= 500 :
        discount = 0.05 * amount
        f_amount = amount- discount
        return f_amount
    else:
        return amount
def gst(amount,gst):
    gst = amount * float(gst/100)

    return gst

product_list = [["Leather wallet",1100,18,1],["Umbrella",900,12,4],["cigarette",200,28,3],["Honey",100,0,2]]
length = len(product_list)
final_price = []
max_gst = []
final_amount = []
for i in range(length):
    #for j in range(i+1):
    result1 = discount(product_list[i][1],product_list[i][3])
    result2 = gst(result1,product_list[i][2])
    final_price1 = result1 + result2
    final_amount.append(final_price1)
    max_gst.append(result2)
print("final amount to be payed to the shopkeeper",sum(final_amount))
print("maximum gst is ",max(max_gst),"for the product",product_list[1][0])