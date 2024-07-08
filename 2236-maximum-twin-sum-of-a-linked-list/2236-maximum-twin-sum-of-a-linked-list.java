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
    public int pairSum(ListNode head) {
        ListNode temp = head;
        int n=0;
        while(temp!=null){
            n+=1;
            temp = temp.next;
        }
        System.out.println(n);
        int[] arr = new int[n/2];
        Arrays.fill(arr,0);
        int idx = 0;
        boolean rev = false;
        while(head!=null){
            arr[idx] = arr[idx] + head.val;
            head = head.next;
            if(rev) idx--;
            else idx++;
            if(idx == n/2){
                idx--;
                rev = true;
            }
        }
        
        return Arrays.stream(arr).max().getAsInt();
    }
}