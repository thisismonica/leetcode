class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if head is None:
            return None
        copied = {} #key: original, copy
        
        # BFS RandomList for deep copy
        queue = [head]
        copy = RandomListNode(head.label)
        copied[head] = copy
        
        while  queue != []:
            node = queue.pop(0)
            copy = copied[node]
                
            if node.next and node.next in copied:
                copy.next = copied[node.next]
            elif node.next and node.next not in copied:
                copy.next = RandomListNode( node.next.label )
                copied[node.next] = copy.next
                queue.append(node.next)
                
            if node.random and node.random in copied:
                copy.random = copied[node.random]
            elif node.random and node.random not in copied:
                copy.random = RandomListNode( node.random.label )
                copied[node.random] = copy.random
                queue.append(node.random)
                
        return copied[head]
                