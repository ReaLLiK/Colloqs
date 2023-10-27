import unittest

from FirstQuestionsGroup import ColloquiumProblems


class TestCommonProblems(unittest.TestCase):
    def test_generate_fibonacci(self):
        cp = ColloquiumProblems()
        self.assertEqual(cp.generate_fibonacci(5), [0, 1, 1, 2, 3])
        self.assertEqual(cp.generate_fibonacci(1), [0])

    def test_is_palindrome(self):
        cp = ColloquiumProblems()
        self.assertTrue(cp.is_palindrome(121))
        self.assertFalse(cp.is_palindrome(123))

    def test_reverse_linked_list(self):
        cp = ColloquiumProblems()

        # Creating a sample linked list: 1 -> 2 -> 3
        class ListNode:
            def __init__(self, val=0, _next=None):
                self.val = val
                self.next = _next

        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)

        reversed_head = cp.reverse_linked_list(head)
        values = []
        while reversed_head:
            values.append(reversed_head.val)
            reversed_head = reversed_head.next
        self.assertEqual(values, [3, 2, 1])
