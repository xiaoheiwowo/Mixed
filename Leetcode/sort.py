import random


def bubble_sort(array):
    """
    冒泡排序递归循环实现
    """
    length = len(array)
    for i in range(length):
        if array[i] > array[-1]:
            array[i], array[-1] = array[-1], array[i]

    if len(array) > 2:
        array[:-1] = bubble_sort(array[:-1])
    else:
        return array
    return array


def insert_sort(array):
    """
    插入排序 循环实现
    使用insert, remove函数
    """

    length = len(array)
    for i in range(length - 1):
        if array[i] > array[i + 1]:
            temp = array.pop(i + 1)
            for j in range(length - 1):
                if temp < array[j]:
                    array.insert(j, temp)
                    break
    return array


def quick_sort(array):
    length = len(array)

    mid = array[int(length / 2)]
    samll = 0
    big = length - 1

    for j in range(mid):
        for i in range(mid - 1):
            if array[i] < array[mid]:
                small = i
                break
        else:
            break

        for i in range(length - mid):
            if array[i + mid + 1] > array[mid]:
                big = i
                break
        else:
            break
    array[small], array[big] = array[big], array[small]


def quick_sort_recursion(array):
    """
    
    """
    if len(array) <= 1:
        return array

    mid = array.pop()
    small = []
    big = []

    for i in array:
        if i < mid:
            small.append(i)
        else:
            big.append(i)

    return quick_sort_recursion(small) + [mid] + quick_sort_recursion(big)


def quick_sort_yd(array):
    pass


# class node(object):
#     def __init__(self,data=None,left=None,right=None):
#         self.data=data
#         self.left=left
#         self.right=right

#     #深度
#     def depth(tree):
#         if tree==None:
#             return 0
#         left,right=depth(tree.left),depth(tree.right)
#         return max(left,right)+1
#     #前序遍历   
#     def pre_order(tree):
#         if tree==None:
#             return
#         print tree.data
#         pre_order(tree.left)
#         pre_order(tree.right)
#     #中序遍历   
#     def mid_order(tree):
#         if tree==None:
#             return
#         mid_order(tree.left)
#         print tree.data
#         mid_order(tree.right)    
#     #后序遍历   
#     def post_order(tree):
#         if tree==None:
#             return
#         post_order(tree.left)
#         post_order(tree.right)   
#         print tree.data

#     #层次遍历    
#     def level_order(tree):
#          if tree==None:
#             return 
#          q=[]
#          q.append(tree)
#          while q:
#              current=q.pop(0)
#              print current.data
#              if current.left!=None:
#                 q.append(current.left)
#              if current.right!=None:
#                 q.append(current.right)
# 实现一个二分查找
# 输入:一个顺序list
# 输出: 待查找的元素的位置
def binary_search(alist, item):
    first = 0
    last = len(alist) - 1

    while first <= last:
        mid = (first + last) // 2
        print(mid)
        if alist[mid] > item:
            last = mid - 1
        elif alist[mid] < item:
            first = mid + 1
        else:
            return mid + 1
    return -1


def my_deepcopy_plus(original):
    if isinstance(original, (int, str, float,)):
        return original
    elif isinstance(original, list):
        new = []
        for i in original:
            new.append(my_deepcopy_plus(i))
        return new
    elif isinstance(original, dict):
        new = {}
        for k, v in original.items():
            new[k] = my_deepcopy_plus(v)
        return new


def test_dpcp():
    nst = [1, 2, [3, 4, 5, [6, 7, {3: 3}]], [8, 9], 10]
    a = my_deepcopy_plus(nst)
    print('a', a)
    print('nst', nst)
    a[-2].append('insert')
    print('change a', a)
    print('nst', nst)


def add_time(func):
    def print_time():
        import time
        print(time.strftime('%Y.%m.%d', time.localtime(time.time())))
        return func()

    return print_time


@add_time
def hello():
    print('hello')


# hello = add_time(hello)

if __name__ == '__main__':
    ar = list(range(100))
    random.shuffle(ar)
    print(ar)
    # print(bubble_sort(ar))
    # print(insert_sort(ar))
    # print(quick_sort_recursion(ar))

    test_dpcp()

    # hello()
    # test = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    # print(binarySearch(test, 3))
