/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode()
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode toRet=new ListNode();
        ListNode head=toRet;
        ListNode curr1=list1;
        ListNode curr2=list2;

        while(curr1!=null && curr2!=null){
            if(curr1.val<=curr2.val){
                toRet.next=curr1;
                curr1=curr1.next;
            } else{
                toRet.next=curr2;
                curr2=curr2.next;
            }
            toRet=toRet.next;
        }

        if(curr1!=null){
            toRet.next=curr1;
        } else if(curr2!=null){
            toRet.next=curr2;
        }

        return head.next;
        
    }
}