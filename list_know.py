nested_list = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
print(nested_list[1])
print(nested_list[-1][2])

numbers = [10, 20, 30]
sum = numbers[0] + numbers[1]  # Adds 10 and 20
sum = numbers[0] +numbers [2]  # Adds 10 and 30



shopping_basket = ["apple", "banana", "cherry", "orange", "pear", "blueberry"]
basket_size = len(shopping_basket)
print(basket_size)
print(shopping_basket[-3])
shopping_basket[2]="biechile"
shopping_basket.append("daxigua")
shopping_basket.insert(3,"niunainai")
print(shopping_basket)


fruits = ["apple", "orange", "cherry", "mango", "grape", "pineapple"]
removed_fruit = fruits.pop(1)
print(removed_fruit)
print(fruits)

fruits = ["apple", "orange", "cherry", "mango", "grape", "pineapple"]
del fruits[1]
print(fruits)

fruits = ["apple", "orange", "cherry", "mango", "grape", "pineapple"]
del fruits[:]
print(fruits)


fruits = ["apple", "kiwi", "orange", "cherry", "mango", "grape", "pineapple", "banana"]
sorted_fruits = sorted(fruits, reverse=True) #reverse=True是降序排列，默认是升序；
print(sorted_fruits)  # Output: ['pineapple', 'orange', 'mango', 'kiwi', 'grape', 'cherry', 'banana', 'apple']

books = ["Harry Potter", "Python Crash Course", "Lord of the Rings", "The Great Gatsby"]
sorted_books = sorted(books)
# 创建一个新的已排序的书单，原始书单保持不变  # sorted（）没有点-只有书单，不改变排序

# .sort()有点-改变排序
# .reverse()-反转顺序
books = ["Harry Potter", "Python Crash Course", "Lord of the Rings", "The Great Gatsby"]
books.sort()
# 直接在原始书单上进行排序



for i in range(8):
    print(i)

for i in range(5, 6):
    print(i)

for i in range(0, 20, 3):
    print(i)
