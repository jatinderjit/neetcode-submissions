// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//     pub val: i32,
//     pub next: Option<Box<ListNode>>,
// }
//
// impl ListNode {
//     #[inline]
//     pub fn new(val: i32) -> Self {
//         ListNode { next: None, val }
//     }
// }

impl Solution {
    pub fn merge_two_lists(mut list1: Option<Box<ListNode>>, mut list2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        if list1.is_none() {
            return list2;
        }
        if list2.is_none() {
            return list1;
        }

        let mut head = Box::new(ListNode::new(0));
        let mut curr = &mut head;
        while let Some(mut l1) = list1 && let Some(mut l2) = list2 {
            if l1.val <= l2.val {
                let next = l1.next.take();
                curr.next = Some(l1);
                curr = curr.next.as_mut().unwrap();
                list1 = next;
                list2 = Some(l2);
                if list1.is_none() {
                    curr.next = list2.take();
                }
            } else {
                let next = l2.next.take();
                curr.next = Some(l2);
                curr = curr.next.as_mut().unwrap();
                list1 = Some(l1);
                list2 = next;
                if list2.is_none() {
                    curr.next = list1.take();
                }
            }
        }
        head.next
    }
}
