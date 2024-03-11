# List

A list maintains a linear order while allowing for accesses and updates in the ‘middle’. 

# Index-Based List

An index-based list is a linear sequence that supports access to its elements by their indices. 

## Main Index-Based List Operations

1. get(r): Return the element of S with index r **O(1)**
2. set(r, e): Replace with e the element at index r and return it **O(1)**
3. add(r, e): Insert a new element e into S to have index r **O(n)**
4. remove(r): Remove from S the element at index r **O(n)**

# Linked List

An linked list stores elements at ‘nodes’ or ‘positions’ 

1. first(): Return the position of the first element of S
2. last(): Return the position of the last element of S
3. before(p): Return the position of the element of S preceding the one at position p
4. after(p): Return the position of the element of S following the one at position p


### Single vs Double Linked List

A single linked list stores nodes in the next link that references to the next node in the list (traverses in only one direction). A double linked list stores two referencesn (next, prev)
 and traverses in either direction. 

