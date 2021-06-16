# dev-prog-problems-solving


Search Tree:
  - is Binary search tree algorithm (written in python)
  - => log(n)
  - The search algorithm depends on the height of the tree, unless in worst case it's only one branch of the tree, it makes 
  the complexity of the algorithm O(n)

| Height  | Nodes | Log calculation |
| ------------- | ------------- | ------------- |
| 0  | 1  | log2(1) = 0  |
| 1  | 3 | log2(3) = 1 |
| 2  | 7  | log2(7) = 2  |
| 3  | 15 | log2(15) = 3   |

Reverse Linked List:
   - Linked list: [{value, next} ...]
   - Reversing [1,2,3] => [3,2,1]
   - Algorithm used: => head.next.next: if head is [1] then next.next => [2,1] and head.next = none
   - The complexity of the algorithm is O(n) since we pass through the whole linked list and its elements.
   
Max Element Stack:
   - 2 arrays: stack, maxes
   - Stack has all elements, maxes has only max value per push
   - Last element of maxes contains the max element of the stack
   - Time and space complexity are both O(n): since we check all the stack and we store all elements, since having 2 arrays means double instruction O(2n) -> O(const * n) -> O(n)