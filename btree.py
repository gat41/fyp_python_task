# def split_L(l, dataset):
#     d = (max(l)-min(l)) / 2
#     print('max=', max(l))
#     print('min=', min(l))
#     print('d=', d)
#     j = 0
#     m = []

#     for i in dataset:
#         if i in l:
#             j=j+1
#     print('Number of points=',j)

#     for k in l:
#         if k < min(l)+d:
#             m.append(k)

#     while j > 5:
#         return m

# def split_R(l, dataset):
#     d = (max(l)-min(l)) / 2
#     print('max=', max(l))
#     print('min=', min(l))
#     print('d=', d)
#     j = 0
#     m = []

#     for i in dataset:
#         if i in l:
#             j=j+1
#     print('Number of points=',j)

#     for k in l:
#         if k >= max(l)-d:
#             m.append(k)

#     while j > 5:
#         return m

# class Node:
#     def __init__(self,data):
#         self.data = data
        # self.left = None
        # self.right = None

class Tree:
    def __init__(self, data):
        self.data = data;
        # self.list = [self.root_node()]
        
    def split_left_node(self):
        pass
        
    def split_right_node(self):
        pass
        
    def make_tree(self):
        #the recursive part can come here where you can have a while loop and call the ssplit_left_node and split_right_node functions
    
    # def root_node(self):
    #     root_node = Node(1)
    #     return root_node


    # def add_node(self, data):
    #     new_node = Node(data)
    #     self.list.append(new_node)
    #     if len(self.list) % 2==0:
    #         self.list[len(self.list) // 2].left = new_node
    #     else:
    #         self.list[len(self.list) // 2].right = new_node

    def output_tree(self):
        print(self.data)
        # for i in range(len(self.data)):
        #     print(self.data[i])
