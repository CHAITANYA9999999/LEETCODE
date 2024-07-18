/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {
        if(head==null) return head;
        
        HashMap<Node, Node> map = new HashMap<>();

        Node temp = head, newHead = new Node(head.val), newTemp = newHead;
        map.put(head, newHead);
        temp = temp.next;
        while(temp != null){
            Node newNode = new Node(temp.val);
            newTemp.next = newNode;
            map.put(temp,newNode);
            temp = temp.next;
            newTemp = newTemp.next;
        }

        for(Map.Entry<Node,Node> entry : map.entrySet()){
            Node oldNode = entry.getKey();
            Node newNode = entry.getValue();
            newNode.random = map.get(oldNode.random);
        }
        return newHead;
    }
}