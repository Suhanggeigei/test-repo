#列表用[]来表示，里面包含多种元素
#形式为xxx=[] 注意[]里面还可插入新的列表[[]];能包含更多的元素
#例如——table = [["Name", "Age", "Country"],["Alice", 25, "USA"],["Bob", 30, "Canada"],["Charlie", 22, "UK"]]
#索引从零开始，同时可使用负的即倒着数。
#列表长度-查数量-len()函数
#将元素添加到列表有集中方式——1.使用append()：将一个元素添加到列表末尾。直接在括号内加引号插入元素。2.使用insert()：在指定索引处插入元素。(1.,"ki")
#                          3.extend()：将另一个列表（或任何可迭代对象）中的元素添加到当前列表的末尾。
#从列表中删除元素——1.remove()——fruits.remove("kiwi") 2.pop() removed_fruit = fruits.pop(1)3.del——删除指定元素 del fruits[0] 4.clear()清空列表
#
#列表排序 sorted()创建一个新的已排序的书单，原始书单保持不变  # sorted（）没有点-只有书单，不改变排序
#        .sort()直接改变书单
#fruits = ["apple", "kiwi", "orange", "cherry", "mango", "grape", "pineapple", "banana"]
#sorted_fruits = sorted(fruits, reverse=True)
#print(sorted_fruits)  # Output: ['pineapple', 'orange', 'mango', 'kiwi', 'grape', 'cherry', 'banana', 'apple']
#fruits.sort(reverse=True)
#print(fruits)  # Output: ['pineapple', 'orange', 'mango', 'kiwi', 'grape', 'cherry', 'banana', 'apple']
#反转排序
#.reverse() 只反转原来列表中元素的排列——数字 = [你，好，啊]就会变成 数字 = [好，啊，你]
#reverse=True的意思是反转后按照降序排序，以前从小到大，现在从大到小。
#key排序就是按照自己设计的规则排序 
fruits = ["apple", "kiwi", "orange", "cherry", "mango", "grape", "pineapple", "banana"]
fruits.sort(key=len)  # Sorting by length of word
print(fruits)  # Output: ['kiwi', 'apple', 'mango', 'grape', 'orange', 'cherry', 'banana', 'pineapple']
#
#
#
#
#
#
#
#
#
#