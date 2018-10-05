#include <stdio.h>
#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode *list1 = l1, *list2 = l2;
    int len1, len2;

    for (len1 = 1;; len1++) {
        if (list1->next == NULL) {
            break;
        } else {
            list1 = list1->next;
        }
    }
    for (len2 = 1;; len2++) {
        if (list2->next == NULL) {
            break;
        } else {
            list2 = list2->next;
        }
    }
    //计算两个链表的长度

    int maxlen, minlen;
    if (len1 >= len2) {
        maxlen = len1;
        minlen = len2;
    } else {
        maxlen = len2;
        minlen = len1;
    }

    list1 = l1;
    list2 = l2;

    int i = 0, add = 0;
    struct ListNode *list = (struct ListNode *) malloc(sizeof(struct ListNode));
    struct ListNode *head = list, *l;
    list->val = 0;
    if (len1 != len2) {
        for (i = 0; i < minlen; i++) {
            add = list1->val + list2->val + list->val;
            if (add >= 10) {
                list->val = add % 10;
                list->next = (struct ListNode *) malloc(sizeof(struct ListNode));
                list = list->next;
                list->val = 1;
            } else {
                list->val = add;
                list->next = (struct ListNode *) malloc(sizeof(struct ListNode));
                list = list->next;
                list->val = 0;
            }
            list1 = list1->next;
            list2 = list2->next;
        }
        if (list1 != NULL) {
            l = list1;
        } else {
            l = list2;
        }
        for (; i < maxlen; i++) {
            list->val = list->val + l->val;
            list->next = (struct ListNode *) malloc(sizeof(struct ListNode));
            if (list->val >= 10) {
                list->val -= 10;
                list->next->val = 1;
            } else {
                list->next->val = 0;
            }
            if (i != maxlen - 1) {
                list = list->next;
                l = l->next;
            } else {
                if (list->next->val == 0) {
                    list->next = NULL;
                } else {
                    list = list->next;
                    list->next = NULL;
                }
            }
        }
    } else {
        for (i = 0; i < minlen; i++) {
            add = list1->val + list2->val + list->val;
            if (add >= 10) {
                list->val = add % 10;
                list->next = (struct ListNode *) malloc(sizeof(struct ListNode));
                list->next->val = 1;
            } else {
                list->val = add;
                list->next = (struct ListNode *) malloc(sizeof(struct ListNode));
                list->next->val = 0;
            }
            if (i != minlen - 1) {
                list = list->next;
            } else {
                if (list->next->val == 0) {
                    list->next = NULL;
                } else {
                    list = list->next;
                    list->next = NULL;
                }
            }
            list1 = list1->next;
            list2 = list2->next;
        }
    }

    return head;
}

int main() {
    int num1[3] = {9, 1, 6};
    int num2[1] = {0};

    return 0;
}