from binary_search_tree import BST

bst = BST()
bst.insert(60, 'sixty')
bst.insert(40, 'forty')
bst.insert(30, 'thirty')
bst.insert(50, 'fifty')
bst.insert(45, 'forty five')
bst.insert(70, 'seventy')
min = bst.find_min()
max = bst.find_max()
result = bst.remove(70)
print(result)
result = bst.remove(70)
print(result)

print(bst.root.left_child.right_child.left_child.value)
print(min.value)
print(max.value)