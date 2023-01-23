products = []
while True:
	name = input('請輸入商品名稱:')
	if name == 'q': #逃出迴圈
		break
	price = input('請輸入商品價格:')
	price = int(price)
	p = []
	p.append(name)
	p.append(price)
	products.append(p)
print(products)

for p in products:
	print(p)
	print(p[0]) #小清單第0格
	print(p[0], '的價格是:', p[1])

with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n' ) #','做不同型別的區隔, '\n'換行

#	products[0][0]


#	p = []
#	p.append(name)
#	p.append(price)

#	p = [name, price]
#	products.append(name, price)