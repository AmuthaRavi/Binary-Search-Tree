class Node:
  def __init__(self,key):
    self.key=key
    self.left=None
    self.right=None
class BST:
  def __init__(self):
    self.root=None
    self.counter=0
  def searchBST(self,head,data,parent):
    if(head==None or head.key==data):
      return [head,parent]
    elif(head.key > data):
      parent=head
      return self.searchBST(head.left,data,parent)
    else:
      parent=head
      return self.searchBST(head.right,data,parent)
  def insertBST(self,node,head):
    if(self.root==None):
      self.root=node
      return
    elif(head.key > node.key):
      if(head.left == None):
        head.left=node
        return True
      else:
        self.insertBST(node,head.left)
    elif(head.key < node.key):
      if(head.right==None):
        head.right=node
        return True
      else:
        self.insertBST(node,head.right)
    else:
      print("DUPLICATION NOT POSSIBLE")
      return head
  def getHead(self):
    return self.root
  def deleteBST(self,head,data):
    if(self.root==None):
      return False
    else:
      parent=None
      list1=self.searchBST(head,data,parent)
      if(list1[0]==None):
        print("Element Not Found")
        return False
      else:
        parent=list1[1]
        delNode=list1[0]
        if(delNode.left==None and delNode.right==None):
          try:
            if(parent.left==delNode):
              parent.left=None
            else:
              parent.right=None
          except:
            self.root=None
          delNode=None
          del delNode
          return True
        else:
          if((delNode.left==None)and(delNode.right!=None)):
            try:
              if(parent.left==delNode):
                parent.left=delNode.right
              else:
                parent.right=delNode.right
            except:
              self.root=delNode.right
            delNode=None
            del delNode
            return True
          elif((delNode.left != None)and(delNode.right == None)):
            try:
              if(parent.left==delNode):
                parent.left=delNode.left
              else:
                parent.right=delNode.left
            except:
              self.root=delNode.left
            delNode=None
            del delNode
            return True
          else:
            minelt=self.findMin(delNode.right)
            self.deleteBST(delNode,minelt.key)
            delNode.key=minelt.key
            return True
  def findMin(self,head):
    if(self.root==None):
      return None
    else:
      if(head.left != None):
        return self.findMin(head.left)
      else:
        return head
  def findMax(self,head):
    if(self.root == None):
      return None
    else:
      if(head.right!= None):
        return self.findMax(head.right)
      else:
        return head
  def inOrder(self,head):
    if(head==None):
      return
    else:
      self.inOrder(head.left)
      print(head.key)
      self.inOrder(head.right)
  def preOrder(self,head):
    if(head==None):
      return 
    else:
      print(head.key)
      self.preOrder(head.left)
      self.preOrder(head.right)
  def postOrder(self,head):
    if(head==None):
      if(head==None):
        return
      else:
        self.postOrder(head.left)
        self.postOrder(head.right)
        print(head.key)
  def findKthlargest(self,head,k):
    if(head==None or mybst.counter >= k):
      return head
    else:
      self.findKthlargest(head.right,k)
      mybst.counter+=1
      if(mybst.counter==k):
        print(head.key)
        return head
      self.findKthlargest(head.left,k)
  def findLCA(self,head,s,g):
    if(head.key < s or (head.key > g)):
      while(head.key<s and (head!=None)):
        head=head.right
      while(head.key>g and (head!=None)):
        head=head.left
    return head
  def findSumPath(self,head,sum_req,path):
    if(head==None):
      return
    else:
      if(head.key > sum_req):
        return
      else:
        sum_req=sum_req-head.key
        path=path+" "+str(head.key)
        if(sum_req==0):
          print(path)
        self.findSumPath(head.left,sum_req,path)
        self.findSumPath(head.right,sum_req,path)
n=int(input("Enter Size of BST:"))
mybst=BST()
for i in range(n):
  x=int(input("Enter element to insert"))
  node1=Node(x)
  head=mybst.getHead()
  mybst.insertBST(node1,head)
ch=1
while(ch!=11):
  print("======================")
  print("1.InOrder:")
  print("2.PreOrder:")
  print("3.PostOrder:")
  print("4.Delete a Element:")
  print("5.K largest Element:")
  print("6.Search an Element:")
  print("7.Find Common LCA (Lowest Common Ancestor):")
  print("8.Find Minimum Element:")
  print("9.Find Maximum Element:")
  print("10.Different Paths where Sum can be present:")
  print("11.Exit")
  print("=======================")
  ch=int(input("Enter your choice:"))
  if(ch==1):
    head=mybst.getHead()
    mybst.inOrder(head)
  elif(ch==6):
    t=int(input("Enter element to find: "))
    head=mybst.getHead()
    parent=None
    f=(mybst.searchBST(head,t,parent))
    if(f[0] == None):
      print("Element Not Found")
    else:
      print("Element Found")
  elif(ch==8):
    head=mybst.getHead()
    print("Minimum Element in BST:"+str(mybst.findMin(head).key))
  elif(ch==9):
    head=mybst.getHead()
    print("Maximum element in BST:"+str(mybst.findMax(head).key))
  elif(ch==4):
    j=int(input("Enter a element to delete in BST"))
    head=mybst.getHead()
    h=mybst.deleteBST(head,j)
    if(h):
      print("Element Deleted")
  elif(ch==1):
    head=mybst.getHead()
    mybst.inOrder(head)
  elif(ch==2):
    head=mybst.getHead()
    mybst.preOrder(head)
  elif(ch==3):
    head=mybst.getHead()
    mybst.postOrder(head)
  elif(ch==5):
    k=int(input("Enter k:"))
    mybst.counter=0
    head=mybst.getHead()
    mybst.findKthlargest(head,k)
  elif(ch==7):
    #Find common LCA for given 2 nodes
    s=int(input("Enter s:"))
    g=int(input("Enter g:"))
    head=mybst.getHead()
    sam=mybst.findLCA(head,s,g)
    if(sam):
      print("GOT LCA")
      print(sam.key)
  elif(ch==10):
    s1=int(input("Enter Sum:"))
    head=mybst.getHead()
    path=""
    mybst.findSumPath(head,s1,path)
