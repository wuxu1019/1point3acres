
mini = float('INF')
rt = None

def findTarget(root, target):
    """find the target function"""
    findTargetHelper(root, target)
    return rt

def findTargetHelper(root, target):
    """find the target helper"""
    if not root:
        return
    if root.val == target:
        rt = root
        return
    if abs(root.val - target) < mini:
        rt = root
    else:
        return
    if root.val > target:
        findTarget(root.left, target)
    else:
        findTarget(root.right, target)




