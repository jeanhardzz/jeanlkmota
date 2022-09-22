# Red Black Tree implementation in Python 2.7
# Author: Algorithm Tutor
# Tutorial URL: https://algorithmtutor.com/Data-Structures/Tree/Red-Black-Trees/


import sys
from pyvis import network as net
from IPython.core.display import display, HTML
import networkx as nx
import matplotlib.pyplot as plt
from random import *
import statistics
import streamlit as st

# data structure that represents a node in the tree
class Node():
    def __init__(self, id_reta,data):
        self.id = 0
        self.id_reta = id_reta
        self.data = data  # holds the key
        self.parent = None #pointer to the parent
        self.left = None # pointer to left child
        self.right = None #pointer to right child
        self.color = 1 # 1 . Red, 0 . Black


# class RedBlackTree implements the operations in Red Black Tree
class RedBlackTree():
    def __init__(self):
        self.g = None        
        self.cont = 0
        self.TNULL = Node(0,0)
        self.TNULL.color = 0
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL

    def __pre_order_helper(self, node):
        if node != TNULL:
            sys.stdout.write(node.data + " ")
            self.__pre_order_helper(node.left)
            self.__pre_order_helper(node.right)

    def __in_order_helper(self, node):
        if node != TNULL:
            self.__in_order_helper(node.left)
            sys.stdout.write(node.data + " ")
            self.__in_order_helper(node.right)

    def __post_order_helper(self, node):
        if node != TNULL:
            self.__post_order_helper(node.left)
            self.__post_order_helper(node.right)
            sys.stdout.write(node.data + " ")

    def __search_tree_helper(self, node, key):
        if node == None or key == node.data:
            return node

        if key < node.data:
            return self.__search_tree_helper(node.left, key)
        return self.__search_tree_helper(node.right, key)

    # fix the rb tree modified by the delete operation
    def __fix_delete(self, x):
        while x != self.root and x.color == 0:
            if x == x.parent.left:
                s = x.parent.right
                if s.color == 1:
                    # case 3.1
                    s.color = 0
                    x.parent.color = 1
                    self.left_rotate(x.parent)
                    s = x.parent.right

                if s.left.color == 0 and s.right.color == 0:
                    # case 3.2
                    s.color = 1
                    x = x.parent
                else:
                    if s.right.color == 0:
                        # case 3.3
                        s.left.color = 0
                        s.color = 1
                        self.right_rotate(s)
                        s = x.parent.right

                    # case 3.4
                    s.color = x.parent.color
                    x.parent.color = 0
                    s.right.color = 0
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == 1:
                    # case 3.1
                    s.color = 0
                    x.parent.color = 1
                    self.right_rotate(x.parent)
                    s = x.parent.left

                if s.left.color == 0 and s.right.color == 0:
                    # case 3.2
                    s.color = 1
                    x = x.parent
                else:
                    if s.left.color == 0:
                        # case 3.3
                        s.right.color = 0
                        s.color = 1
                        self.left_rotate(s)
                        s = x.parent.left 

                    # case 3.4
                    s.color = x.parent.color
                    x.parent.color = 0
                    s.left.color = 0
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = 0

    def __rb_transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def __delete_node_helper(self, node, key):
        # find the node containing key
        z = self.TNULL
        while node != self.TNULL:
            if node.data == key:
                z = node

            if node.data <= key:
                node = node.right
            else:
                node = node.left

        if z == self.TNULL:
            print ("Couldn't find key in the tree")
            return

        y = z
        y_original_color = y.color
        if z.left == self.TNULL:
            x = z.right
            self.__rb_transplant(z, z.right)
        elif (z.right == self.TNULL):
            x = z.left
            self.__rb_transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.__rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.__rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 0:
            self.__fix_delete(x)
    
    # fix the red-black tree
    def  __fix_insert(self, k):
        while k.parent.color == 1:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left # uncle
                if u.color == 1:
                    # case 3.1
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        # case 3.2.2
                        k = k.parent
                        self.right_rotate(k)
                    # case 3.2.1
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right # uncle

                if u.color == 1:
                    # mirror case 3.1
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent 
                else:
                    if k == k.parent.right:
                        # mirror case 3.2.2
                        k = k.parent
                        self.left_rotate(k)
                    # mirror case 3.2.1
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 0

    def __print_helper(self, node, indent, last):
        # print the tree structure on the screen
        if node != self.TNULL:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "

            s_color = "RED" if node.color == 1 else "BLACK"
            print (str(node.data) + "(" + s_color + ")" + "id:", node.id)
            self.__print_helper(node.left, indent, False)
            self.__print_helper(node.right, indent, True)
    
    # Pre-Order traversal
    # Node.Left Subtree.Right Subtree
    def preorder(self):
        self.__pre_order_helper(self.root)

    # In-Order traversal
    # left Subtree . Node . Right Subtree
    def inorder(self):
        self.__in_order_helper(self.root)

    # Post-Order traversal
    # Left Subtree . Right Subtree . Node
    def postorder(self):
        self.__post_order_helper(self.root)

    # search the tree for the key k
    # and return the corresponding node
    def searchTree(self, k):
        return self.__search_tree_helper(self.root, k)
    

    # find the node with the minimum key
    def minimum(self, node):
        while node.left != self.TNULL:
            node = node.left
        return node

    # find the node with the maximum key
    def maximum(self, node):
        while node.right != self.TNULL:
            node = node.right
        return node

    # find the successor of a given node
    def successor(self, x):
        # if the right subtree is not None,
        # the successor is the leftmost node in the
        # right subtree
        if x.right != self.TNULL:
            return self.minimum(x.right)

        # else it is the lowest ancestor of x whose
        # left child is also an ancestor of x.
        y = x.parent
        while y != self.TNULL and x == y.right:
            x = y
            y = y.parent
        return y

    # find the predecessor of a given node
    def predecessor(self,  x):
        # if the left subtree is not None,
        # the predecessor is the rightmost node in the 
        # left subtree
        if (x.left != self.TNULL):
            return self.maximum(x.left)

        y = x.parent
        while y != self.TNULL and x == y.left:
            x = y
            y = y.parent

        return y

    # rotate left at node x
    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    # rotate right at node x
    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    # insert the key to the tree in its appropriate position
    # and fix the tree
    def insert(self, key):
        # Ordinary Binary Search Insertion
        self.cont = self.cont + 1
        node = Node(key.id,key.inicio().x)
        node.id = self.cont
        node.id_reta = key.id
        node.parent = None
        node.data = key.inicio().y
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = 1 # new node must be red

        y = None
        x = self.root

        while x != self.TNULL:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right

        # y is parent of x
        node.parent = y
        if y == None:
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node

        # if new node is a root node, simply return
        if node.parent == None:
            node.color = 0
            return

        # if the grandparent is None, simply return
        if node.parent.parent == None:
            return

        # Fix the tree
        self.__fix_insert(node)

    def get_root(self):
        return self.root

    # delete the node from the tree
    def delete_node(self, key):
        self.__delete_node_helper(self.root, key.inicio().y)

    # print the tree structure on the screen
    def pretty_print(self):
        self.__print_helper(self.root, "", True)

    def above(self,key):
      no = self.searchTree(key.inicio().y)
      if no == None:
        return None
      elif no.parent == None:
        return None
      else:
        return no.parent.id_reta
    
    def below(self,key):
      no = self.searchTree(key.inicio().y)
      if no == None:
        return None
      elif no.left != None:
        if no.left.id_reta == 0: return None
        return no.left.id_reta
      elif no.right != None:
        if no.right.id_reta == 0: return None
        return no.right.id_reta
      else:
        return None

    def __show_tree_helper(self, node,father):
        # print the tree structure on the screen
        if node != self.TNULL:                        

            s_color = "#FF0000" if node.color == 1 else "#000000"                        
            
            #self.g.add_node(node.id,label=str(node.id_reta),color= s_color)


            if father > -1:
              #self.g.add_edge(father,node.id)               
              self.g.add_edges_from([(father,node.id_reta)])
                   
            
            self.__show_tree_helper(node.left,node.id_reta)
            self.__show_tree_helper(node.right,node.id_reta)
    
    def show_tree(self): 
      """
      import networkx as nx

      g=nx.DiGraph()
      g.add_edges_from([(1,2)])
      g.add_edges_from([(1,3), (1,4), (2,5), (2,6), (2,7), (3,8), (3,9)])
      g.add_edges_from([(4,10), (5,11), (5,12), (6,13)])
      nx.drawing.nx_pydot.to_pydot(g)
      p.write_png('example.png')
      from IPython.display import Image
      Image('example.png')
      """
      self.g=nx.Graph()
      self.__show_tree_helper(self.root,-1)
      p=nx.drawing.nx_pydot.to_pydot(self.g)
      p.write_png('a.png')
      from IPython.display import Image
      display(Image('a.png'))

      """
      self.g=net.Network(directed =False, height='500px', width='80%',layout = True)    
      

      self.__show_tree_helper(self.root,-1)

      self.g.toggle_physics(True)
      self.g.show('afd.html')         
      display(HTML('afd.html'))
      """

"""
if __name__ == "__main__":
    bst = RedBlackTree()
    bst.insert(1)
    bst.insert(2)
    bst.insert(3)
    bst.insert(4)
    bst.insert(5)    
    bst.insert(25)
    bst.insert(35)
    bst.insert(9)
    bst.pretty_print()
    bst.show_tree()
"""

class Ponto:
  def __init__(self,id,x,y):    
    self.x = x
    self.y = y
    self.id = id
  
  def x(self):
    return self.x
  
  def y(self):
    return self.y
  
  def id(self):
    return self.id

class Reta:
  def __init__(self,id,x1,y1,x2,y2):    
    self.p1 = Ponto(id,x1,y1)
    self.p2 = Ponto(id,x2,y2)
    self.id = id

  def x(self):
    x = [self.p1.x,self.p2.x]    
    return x
  
  def y(self):
    return [self.p1.y,self.p2.y]

  def inicio(self):
    if self.p1.x <= self.p2.x:
      return self.p1
    else:
      return self.p2
  
  def final(self):
    if self.p1.x >= self.p2.x:
      return self.p1
    else:
      return self.p2
  
  def id(self):
    return self.id

class Conjunto:
  def __init__(self,n):
    self.t = 0 #Id e mostra a quantidade de retas 
    self.s = []
    self.GeraRetas(n)
  
  def Insere(self,x1,y1,x2,y2):    
    self.t = self.t + 1
    r = Reta(self.t,x1,y1,x2,y2)
    self.s.append(r)

  def GetLista(self):
    return self.s
  
  def __len__(self):
    return self.t

  def xvalues(self): #lista de pares
    xvalues =[]
    for i in range(self.t):
      xvalues.append(self.s[i].x())
    return xvalues
    
  
  def yvalues(self):
    yvalues = []
    for i in range(self.t):
      yvalues.append(self.s[i].y())
    return yvalues

  def GeraRetas(self,n):
    for i in range(n):
      x1 = random()*100
      y1 = random()*100
      x2 = random()*100
      y2 = random()*100
      self.Insere(x1,y1,x2,y2)
  
  def ShowRetas(self):    
    xvalues =  self.xvalues()
    yvalues =  self.yvalues()
    fig = plt.figure()

    for i in range(self.t):
      plt.plot(xvalues[i], yvalues[i], 'bo', linestyle="-")
      plt.text(statistics.median(xvalues[i]), statistics.median(yvalues[i]), "reta "+str(i+1))
    
    return fig

  def Direction(self,p0,p1,p2):    
    #(x1-x0)(y2-y0)-(x2-x0)(y1-y0) 
    a = p1.x - p0.x
    b = p2.y - p0.y
    c = p2.x - p0.x
    d = p1.y - p0.y
    return (a*b) - (c*d)

  def Intersect(self,r1,r2):    
    p1 = r1.inicio()
    p2 = r1.final()
    p3 = r2.inicio()
    p4 = r2.final()

    d1 = self.Direction(p3,p4,p1)
    d2 = self.Direction(p3,p4,p2)
    d3 = self.Direction(p1,p2,p3)
    d4 = self.Direction(p1,p2,p4)

    if(( d1>0 and d2<0 ) or ( d1<0 and d2>0 )) and (( d3>0 and d4<0 ) or ( d3<0 and d4>0)):
      return True
    else:
      return False


def AnySegmentsIntersect(S):
  #Inicializando arvore rubro negra
  T = RedBlackTree()
  S = Conjunto(S)  
  #Primeiro passo ordenar todos os pontos, os de inicio e os finais juntos.
  retas = S.GetLista()
  pontos = []
  for r in retas:
    #print("reta ",r.id," inicio (",r.inicio().x,",",r.inicio().y,")"," final (",r.final().x,",",r.final().y,")")
    pontos.append(r.inicio())
    pontos.append(r.final())

  #Ordenando rapidamente com python
  pontos = sorted(pontos, key=lambda ponto: ponto.x)
  
  #Percorrendo os pontos e procurando interceções
  achou = False
  for p in pontos:
    #print("reta ",p.id," ponto (",p.x,",",p.y,")")
    for r in retas:
      if r.id == p.id:
        if p.x == r.inicio().x:
          T.insert(r)
          reta_ab = None
          reta_be = None
          ab = T.above(r)
          be = T.below(r)
          for rj in retas:
            if ab == rj.id:
              reta_ab = rj
            if be == rj.id:
              reta_be = rj
          if (ab != None and S.Intersect(reta_ab,r)) or (be != None and S.Intersect(reta_be,r)):
            #print("Temos interceção")
            achou = True
        if p.x == r.final().x:
          reta_ab = None
          reta_be = None
          ab = T.above(r)
          be = T.below(r)
          for rj in retas:
            if ab == rj.id:
              reta_ab = rj
            if be == rj.id:
              reta_be = rj
          if (ab != None and be != None) and S.Intersect(reta_ab,reta_be) :
            achou = True
            #print("Temos interceção")

          #T.show_tree()
          T.delete_node(r)                  
  
  msg = "Erro"
  if(achou):
    #print("Existe interceção")
    msg = "Existe interceção"
  else:
    print("Não existe interceção")
    msg = "Não existe interceção"

  return S.ShowRetas(),msg

