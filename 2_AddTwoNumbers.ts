// Conversion of python to typescript, see python file for methodology
// Repo Only
class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
}

//LeetCode
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
    var tempNode = new ListNode(0)
    var tailNode = tempNode
    var carry = 0

    while(l1 !== null || l2 !== null || carry !== 0) {
        var digit1 = l1?.val ?? 0
        var digit2 = l2?.val ?? 0

        var sum = digit1 + digit2 + carry
        carry = (sum > 9) ? 1 : 0

        tailNode.next = new ListNode(sum % 10)

        l1 = l1?.next ?? null
        l2 = l2?.next ?? null
        tailNode = tailNode.next
    }

    return tempNode.next
};