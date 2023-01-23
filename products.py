products = []
# 檢查載入的檔案
import os #operation system 作業系統模組
if os.path.isfile('products.csv'): #檢查檔案是否存在
	print('yaeh')
	with open('products.csv', 'r', encoding = 'utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue # 繼續
			name, price = line.strip().split(',') #分別存為名稱與價格
			products.append([name, price])
	print(products)
else:
	print('找不到檔案')

# 讓使用者輸入
while True:
	name = input('請輸入商品名稱:')
	if name == 'q': #逃出迴圈
		break
	price = input('請輸入商品價格:')
	price = int(price)
	products.append([name, price])
print(products)

# 印出所有購買紀錄
for p in products:
	print(p[0], '的價格是:', p[1])

# 寫入檔案
with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n' ) #','做不同型別的區隔, '\n'換行