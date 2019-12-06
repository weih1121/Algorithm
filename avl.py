class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1     # 树的最小高度为叶子节点层 1
    

def get_height(node):
    if not node:return 0
    return node.height

def get_balance_factor(node):
    if not node: return 0 
    return get_height(node.left) - get_height(node.right)

def left_rotate(node):
    '''
    x: new root
    y: x.left
    '''
    x = node.right
    y = x.left
    x.left = node
    node.right = y
    node.height = max(get_height(node.left), get_height(node.right)) + 1 # 左子树 先更新
    x.height = max(get_height(x.left), get_height(x.right)) + 1          # root 后更新
    return x

def right_rotate(node):
    '''
    x: new root
    y: x.right
    '''
    x = node.left
    y = x.right
    x.right = node
    node.left = y
    node.height = max(get_height(node.left), get_height(node.right)) + 1 # 同上
    x.height = max(get_height(x.left), get_height(x.right)) + 1          # 同上
    return x

def insert(root, val):
    if not root:
        return Node(val)
    
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)

    root.height = max(get_height(root.left), get_height(root.right)) + 1
    balance_factor = get_balance_factor(root)

    if balance_factor > 1 and val < root.left.val:
        return right_rotate(root)
    if balance_factor > 1 and val > root.left.val:
        root.left = left_rotate(root.left)
        return right_rotate(root)
    if balance_factor < -1 and val > root.right.val:
        return left_rotate(root)
    if balance_factor < -1 and val < root.right.val:
        root.right = right_rotate(root.right)
        return left_rotate(root)
    return root

def preorder_travel(root):
    if root:
        print(root.val, end=' ')
        preorder_travel(root.left)
        preorder_travel(root.right)


def delete(root, val):
    if not root:return
    pass



if __name__ == "__main__":
    vals = [x for x in range(1, 11)]
    root = None
    for val in vals:
        root = insert(root, val)
    preorder_travel(root)


