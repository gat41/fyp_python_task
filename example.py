import numpy as np
import btree as bt

#temporarily set seed to ensure that every time the code is run, the same set of numbers will appear 
np.random.seed(0)

# generate data
data = np.random.normal(50, 10, 10) 
# data = np.random.normal(50,10,100) #what does the 50, 10, and 100 represent?

# if __name__ == '__main__': #I think this is not needed

# create a btree instance 
tree = bt.Tree(data) 

# for i in range(2,100):
# tree.add_node(i)

tree.output_tree()
# print(tree.list[5].left.data)
# print(tree.list[6].right.data)
