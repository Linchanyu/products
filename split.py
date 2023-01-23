#讀取檔案並切割大表單成小清單
products = []
with open('products.csv', 'r', encoding = 'utf-8') as f:
	for line in f:
		s = line.strip().split(',') #遇到\n逗點就分割
		print(s)

		name, price = line.strip().split(',') #分別存為名稱與價格
		products.append([name, price])

print(products)