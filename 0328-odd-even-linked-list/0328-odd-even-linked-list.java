/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode oddEvenList(ListNode head) {
        ListNode odd = new ListNode();
        ListNode odd_last = odd;
        ListNode even = new ListNode();
        ListNode even_last = even;
        ListNode temp = head;
        int i=1;
        while(temp!=null){
            if(i%2==0){
                even_last.next = new ListNode(temp.val);
                even_last = even_last.next;
            }
            else{
                odd_last.next = new ListNode(temp.val);
                odd_last = odd_last.next;
            }
            temp = temp.next;
            i++;
        }
        odd_last.next = even.next;
        return odd.next;
    }
}