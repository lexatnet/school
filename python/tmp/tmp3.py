N = int(input())
persons = []
for i in range(N-1):
  child, parent = input().split()
  persons.append((child, parent))

def get_root(persons):
  child_set = set([i[0] for i in persons])
  parent_set = set([i[1] for i in persons])
  return (parent_set - child_set).pop()

root = get_root(persons)

def grow_tree(root, persons, level = 0):
  childs = {}
  for i in persons:
    if i[1] == root:
      child = i[0]
      tmp = grow_tree(child, persons, level + 1)
      childs[child] = tmp
  return {
    'person': root,
    'childs': childs,
    'level':level
  }

tree = grow_tree(root, persons)

import json
print(json.dumps(tree, indent=4))

d = {}

for child, parent in persons:
  parents = [parent]
  if parent in d.keys():
    parents += d[parent]
  for k in d.keys():
    if child in d[k]:
      d[k] += parents
  d[child] = parents

X = int(input())

print(json.dumps(d, indent=4))


for i in range(X):
  person1, person2 = input().split()
  if(person1 == person2):
    print(person1)
    continue
  parents1 = [person1]
  parents2 = [person2]
  if person1 in d.keys():
    parents1 = d[person1]
  if person2 in d.keys():
    parents2 = d[person2]
  if(person1 in parents2):
    print(person1)
    continue
  if(person2 in parents1):
    print(person2)
    continue

  common = set(parents1) & set(parents2)
  diff = set(parents1).difference(common)
  t = parents1
  for p in diff:
    t.remove(p)
  if len(t) > 0:
    print(t[0])
    print('here')
