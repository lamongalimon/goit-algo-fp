import uuid
import heapq
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


class Node:
  def __init__(self, key, color="skyblue"):
    self.left = None
    self.right = None
    self.val = key
    self.color = color # Додатковий аргумент для зберігання кольору вузла
    self.id = str(uuid.uuid4()) # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
  if node is not None:
    graph.add_node(node.id, color=node.color, label=node.val) # Використання id та збереження значення вузла
    if node.left:
      graph.add_edge(node.id, node.left.id)
      l = x - 1 / 2 ** layer
      pos[node.left.id] = (l, y - 1)
      l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
    if node.right:
      graph.add_edge(node.id, node.right.id)
      r = x + 1 / 2 ** layer
      pos[node.right.id] = (r, y - 1)
      r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
  return graph


def draw_tree(tree_root, title=""):
  tree = nx.DiGraph()
  pos = {tree_root.id: (0, 0)}
  tree = add_edges(tree, tree_root, pos)

  colors = [node[1]['color'] for node in tree.nodes(data=True)]
  labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)} # Використовуйте значення вузла для міток

  plt.figure(figsize=(8, 5))
  plt.title(title)  
  nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
  plt.show()


def build_heap_tree(heap, index=0):

  if index >= len(heap):
    return None
  node = Node(heap[index])
  node.left = build_heap_tree(heap, 2 * index + 1)
  node.right = build_heap_tree(heap, 2 * index + 2)
  return node


def draw_heap(heap):

  if not heap:
    print("Купа порожня — нічого візуалізувати.")
    return
  root = build_heap_tree(heap)
  draw_tree(root)

def bfs_order(root):
    queue = deque([root])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return order

def dfs_order(root):
    stack = [root]
    order = []
    while stack:
        node = stack.pop()
        order.append(node)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return order

def generate_colors(n, start=(18, 50, 100), end=(200, 230, 255)):
    colors = []
    for i in range(n):
        t = i / (n - 1) if n > 1 else 0
        r = int(start[0] + (end[0] - start[0]) * t)
        g = int(start[1] + (end[1] - start[1]) * t)
        b = int(start[2] + (end[2] - start[2]) * t)
        colors.append(f"#{r:02X}{g:02X}{b:02X}")
    return colors

def visualize_traversal(root, traversal, title):
    order = traversal(root)
    colors = generate_colors(len(order))
    for i, node in enumerate(order):
        node.color = colors[i]
    print(title + ":", [node.val for node in order])
    draw_tree(root, title)


if __name__ == "__main__":
  

  data = [10, 4, 5, 0, 1, 3, 8, 7, 2]
  heapq.heapify(data)
  print("Мін-купа у вигляді масиву:", data)
  root = build_heap_tree(data)
  print([n.val for n in bfs_order(root)])
  print([n.val for n in dfs_order(root)])
 
  visualize_traversal(root, bfs_order, "Обхід у ширину (BFS)")
  visualize_traversal(root, dfs_order, "Обхід у глибину (DFS)")
