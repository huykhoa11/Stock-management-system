#学籍番号：19H060 　氏名：チャン　ヒュ　コア
import sqlite3
conn = sqlite3.connect('ec.db')
c = conn.cursor()

c.execute("""
 CREATE TABLE IF NOT EXISTS users (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 name TEXT,
 email TEXT,
 age INTEGER
 )
""")


c.execute("""
 CREATE TABLE IF NOT EXISTS items (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 name TEXT,
 code TEXT,
 price INTEGER
 )
""")

c.execute("""
 CREATE TABLE IF NOT EXISTS purchase_histories(
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 user_id INTEGER,
 item_id INTEGER
 )
""")

def UserCreate():
	print("=== USER CREATE PAGE ===")
	user_name = input('input - name: ')
	user_email = input('input - email: ')
	user_age = input('input - age: ')
	c.execute("""
	INSERT INTO users (name, email, age) values (:user_name,
	:user_email, :user_age)
	""", {'user_name': user_name, 'user_email': user_email, 'user_age': user_age})
	conn.commit()
	c.execute("""
	SELECT name, email, age FROM users WHERE name = :user_name AND email = :user_email AND age = :user_age
	""", {'user_name': user_name, 'user_email':user_email, 'user_age': user_age})
	user_show = c.fetchone()
	print("\nCREATE USER Name:", user_show[0], ", Email:", user_show[1], ", Age:", user_show[2])


def UserEdit():
	print("=== USER EDIT PAGE ===")
	user_id = input("EDIT USER ID:")
	c.execute("""
	SELECT name, email, age FROM users WHERE id = :user_id
	""", {'user_id': user_id})
	user_show = c.fetchone()
	print("\nEDIT TARGET USER INFO: Name:", user_show[0], ",Email:", user_show[1], ",Age:", user_show[2])
	#
	user_name = input('\nedit - name: ')
	user_email = input('edit - email: ')
	user_age = input('edit - age: ')
	c.execute("""
	UPDATE users SET name = :user_name, email = :user_email, age = :user_age WHERE id = :user_id 
	""",{'user_name': user_name, 'user_email':user_email, 'user_age': user_age, 'user_id':user_id})
	conn.commit()
	#
	c.execute("""
	SELECT name, email, age FROM users WHERE name = :user_name AND email = :user_email AND age = :user_age
	""", {'user_name': user_name, 'user_email':user_email, 'user_age': user_age})
	user_show = c.fetchone()
	print("\nEDIT USER Name:", user_show[0], ", Email:", user_show[1], ", Age:", user_show[2])


def UserDelete():
	print("=== USER DELETE PAGE ===")
	user_id = input("\nDELETE USER ID:")
	c.execute("""
	SELECT id, name, email, age FROM users WHERE id = :user_id
	""", {'user_id': user_id})
	user_show = c.fetchone()
	print("\nDELETE USER : Id:", user_show[0], ",Name:", user_show[1], ",Email:", user_show[2], ",Age:", user_show[3])
	c.execute("""DELETE FROM users WHERE id = :user_id""", {'user_id': user_id})
	conn.commit()


def UserList():
	print("=== USER LIST PAGE ===\n")
	c.execute("SELECT * FROM users WHERE 0 < id AND id <= 100")
	records = c.fetchall()

	for row in records:
		print("\nId:", row[0], ",Name:", row[1], ",Email:", row[2], ",Age:", row[3])


def ItemCreate():
	print("=== ITEM CREATE PAGE ===")
	item_name = input('input - name: ')
	item_code = input('input - code: ')
	item_price = input('input - price: ')
	c.execute("""
	INSERT INTO items (name, code, price) values (:item_name,
	:item_code, :item_price)
	""", {'item_name': item_name, 'item_code': item_code, 'item_price': item_price})
	conn.commit()
	c.execute("""
	SELECT name, code, price FROM items WHERE name = :item_name AND code = :item_code AND price = :item_price
	""", {'item_name': item_name, 'item_code':item_code, 'item_price': item_price})
	item_show = c.fetchone()
	print("\nCREATE ITEM Name:",item_show[0],", Code:",item_show[1],", Price:",item_show[2])


def ItemEdit():
	print("=== ITEM EDIT PAGE ===")
	item_id = input("EDIT ITEM ID:")
	c.execute("""
	SELECT name, code, price FROM items WHERE id = :item_id
	""", {'item_id': item_id})
	item_show = c.fetchone()
	print("\nEDIT TARGET ITEM INFO: Name:", item_show[0], ",Code:", item_show[1], ",Price:", item_show[2])
	#
	item_name = input('\nedit - name: ')
	item_code = input('edit - code: ')
	item_price = input('edit - price: ')
	c.execute("""
	UPDATE items SET name = :item_name, code = :item_code, price = :item_price WHERE id = :item_id 
	""",{'item_name': item_name, 'item_code':item_code, 'item_price': item_price, 'item_id':item_id})
	conn.commit()
	#
	c.execute("""
	SELECT name, code, price FROM items WHERE name = :item_name AND code = :item_code AND price = :item_price
	""", {'item_name': item_name, 'item_code':item_code, 'item_price': item_price})
	item_show = c.fetchone()
	print("\nEDIT USER Name:", item_show[0], ", Code:", item_show[1], ", Price:", item_show[2])


def ItemDelete():
	print("=== ITEM DELETE PAGE ===")
	item_id = input("\nDELETE ITEM ID:")
	c.execute("""
	SELECT id, name, code, price FROM items WHERE id = :item_id
	""", {'item_id': item_id})
	item_show = c.fetchone()
	print("\nDELETE ITEM : Id:", item_show[0], ",Name:", item_show[1], ",Code:", item_show[2], ",Price:", item_show[3])
	c.execute("""DELETE FROM items WHERE id = :item_id""", {'item_id': item_id})
	conn.commit()


def ItemList():
	print("=== ITEM LIST PAGE ===\n")
	c.execute("SELECT * FROM items WHERE 0 < id AND id <= 100")
	records = c.fetchall()

	for row in records:
		print("\nId:", row[0], ",Name:", row[1], ",Code:", row[2], ",Price:", row[3])	


def BuyMode():
	print("=== ITEM BUY MODE PAGE ===\n")
	user_id = input('USER_ID: ')
	item_code = input('BUY ITEM CODE: ')
	#
	c.execute("""
	SELECT id, name, email, age FROM users WHERE id = :user_id
	""", {'user_id': user_id})
	user_show = c.fetchone()
	print("\nUSER INFO ID:", user_show[0], ",Name:", user_show[1], ",Email:", user_show[2], ",Age:", user_show[3])
	#
	c.execute("""
	SELECT id, name, code, price FROM items WHERE code = :item_code
	""", {'item_code': item_code})
	item_show = c.fetchone()
	print("ITEM INFO ID:", item_show[0], ",Name:", item_show[1], ",Code:", item_show[2], ",Price:", item_show[3])
	
	confirm = input("\nCONFIRM BUY (y/n): ")
	if (confirm=="" or confirm=="y"):
		c.execute("""
		SELECT id FROM items WHERE code = :item_code
		""", {'item_code': item_code})
		item_id = c.fetchone()[0]
		c.execute("""
		INSERT INTO purchase_histories (user_id, item_id) values (:user_id,
		:item_id)
		""", {'user_id': user_id, 'item_id': item_id})
		conn.commit()
		c.execute("""
		SELECT id, user_id, item_id FROM purchase_histories WHERE user_id = :user_id and item_id = :item_id
		""", {'user_id': user_id, 'item_id': item_id})
		history_show = c.fetchone()
		print("\nITEM PURCHASE ID:", history_show[0], ",USER_ID:", history_show[1], ",ITEM_ID:", history_show[2])


def BuyHistoriesMode():
	print("=== ITEM BUY HISTORIES MODE PAGE ===\n")
	print("PURCHASE HISTORY INFO 10 RECORDS.\n")

	c.execute("""
	SELECT id FROM purchase_histories ORDER BY id DESC LIMIT 10
	""")
	history_id = c.fetchone()[0]
	c.execute("""
	SELECT purchase_histories.id, users.name, users.email, items.name, items.price
	 FROM purchase_histories
	 INNER JOIN users ON purchase_histories.user_id = users.id
	 INNER JOIN items ON purchase_histories.item_id = items.id
	 WHERE purchase_histories.id = :history_id
	""", {'history_id': history_id})
	records = c.fetchall()

	for row in records:
		print("Id:", row[0], ",USER_NAME:", row[1], ",USER_EMAIL:", row[2], ",ITEM_NAME:", row[3], "ITEM_PRICE:", row[4])	


def TotalMode():
	print("\n=== TOTAL AMOUNT AGGREGATION MODE PAGE ===\n")
	c.execute("""
	SELECT items.price 
	FROM items 
	INNER JOIN purchase_histories ON purchase_histories.id == items.id
	""")
	records = c.fetchall()

	total = 0
	for i in records:
		total += int(i[0])
	print("TOTAL AMOUNT: ", total)


def SystemExit():
	print("\nclose database and EC system\nbye.")
	return 1

if __name__ == '__main__':
	flag = 0
	while(flag == 0):
		print("\n\n=== EXEC PAGE ===\nexec list:\n")
		print("1. User create.\n2. User Edit.\n3. User Delete.\n4. User List.\n5. Item Create.\n6. Item Edit.\n7. Item Delete.\n8. Item List.\n9. To Item Buy Mode.\n10.To Item Buy Histories Mode.\n11. To Total Amount Aggregation Mode.\n12. System Exit.\n")
		n = input("exec:")
		mode = int(n)
		if(mode == 1):
			UserCreate()
		elif(mode == 2):
			UserEdit()
		elif(mode == 3):
			UserDelete()
		elif(mode == 4):
			UserList()
		elif(mode == 5):
			ItemCreate()
		elif(mode == 6):
			ItemEdit()
		elif(mode == 7):
			ItemDelete()
		elif(mode == 8):
			ItemList()
		elif(mode == 9):
			BuyMode()
		elif(mode == 10):
			BuyHistoriesMode()
		elif(mode == 11):
			TotalMode()
		elif(mode == 12):
			flag = SystemExit()
	conn.close()