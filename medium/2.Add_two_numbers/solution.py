/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode l3;
        ListNode *temp=&l3;
        ListNode *temp2=&l3;
        int sum=0,carry=0;
        while(l1!=NULL || l2!=NULL ||carry!=0)
        {
            sum=0;
            sum+=(l1==NULL)?0:l1->val;
            if(l1!=NULL)
                l1=l1->next;
            sum+=(l2==NULL)?0:l2->val;
            if(l2!=NULL)
                l2=l2->next;
            sum+=carry;
            carry=sum/10;
            sum%=10;
            temp->next =new ListNode(sum);
            temp=temp->next;
            
            

        }
        return temp2->next;
        
        
    }
};
