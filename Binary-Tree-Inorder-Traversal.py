def inorder(root):
    if not root:
        return root
    else:
        inorder(root.left)
        s.append(root.val)
        inorder(root.right)
      
root = [1,null,2,3]
s=[]
inorder(root)
return s
