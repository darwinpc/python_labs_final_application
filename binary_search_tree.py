#!/usr/bin/env python3
import os

# Una tienda de  ropa esta realizando un inentario de almacen y los datos que requiere son el id del articulo y la cantidad exisente.

# Utilizar un arbol binario para ingresar a una estructura dinamica el ID del articulo y la cantidad existente

# El output del programa es:

# ID del articulo: 1
# Cantidad ID del articulo 2
# Cantidad Id del articulo 3


class Node:
  def __init__(self, key):
    self.left = None
    self.right = None
    self.val = key

def insert(root, key):
  if root is None:
    return Node(key)
  else:
    if root.val == key:
      return root
    elif root.val < key:
      root.right = insert(root.right, key)
    else:
      root.left = insert(root.left, key)

  return root

def inorder(root, order=None):
  if root:
    inorder(root.left, 'amount')
    inorder(root.right, 'amount')
    if order == 'amount':
      print("Cantidad: {}".format(root.val))
    else:
      print("ID Articulo: {}".format(root.val))

def search(root, key):
  if root == None:
    print("\nEl ID {} no fue encontrado.".format(key))
  else:
    if root.val == key:
      print("ID {} encontrado".format(key))
      inorder(root)

def preorder(root):
  if root == None:
    return None
  else:
    print(root.val)
    self.preorder(root.left)
    self.preorder(root.right)
    
def postorder(root):
  if root == None:
    return None
  else:
    self.postorder(root.left)
    self.postorder(root.right)
    print(root.val)


while True:
  opc = input("\n1.-Insertar ID Articulo(Nodo) \n2.-Inorden \n3.-Preorden \n4.-Postorden \n5.-Buscar \n6.-Salir \n\nElige una opcion -> ")

  if  opc == '1':
    node = input("\nIngresa ID del articulo -> ")
    if node.isdigit():
      node = int(node)
      r = Node(node)
      while True:
        pc = input ("\nIngresa una cantidad -> ")
        if pc.isdigit():
          r = insert(r, int(pc))
          request = input("\nDesea ingresar otra cantidad? (S/N) -> ")
          if request == 'N':
            break
        else:
          print("\nIngresa solo digitos...")
    else:
      print("\nIngresa solo digitos...")
  elif opc == '2':
    try:
      inorder(r)
    except Exception as e:
      inorder(None)
  elif opc == '3':
    try:
      preorder(r)
    except Exception as e:
      preorder(None)
  elif opc == '4':
    try:
      postorder(r)
    except Exception as e:
      postorder(None)
  elif opc == '5':
    node = input("\nIngresa ID del articulo -> ")
    if node.isdigit():
      try:
        search(r, int(node))
      except Exception as e:
        search(None, int(node))
    else:
      print("\nIngresa solo digitos...")
  elif opc == '6':
    print("\nElegiste salir...\n")
    os.system("pause")
    break

print()


      
