list1 = ["a","b","c"]
list2 = ["Ken","vivin","joy"]
print(len(list1))
print(list1)
print("id:",id(list1))
#+= 等同於extend
#+ 會產生新的List
#list1 +=  list2
list1 = list1 + list2
print("id:",id(list1))
print(len(list1))
print(list1)
