import unittest


class ColloquiumProblems:
    @staticmethod
    def generate_fibonacci(n):
        if n <= 0:
            return []

        fibonacci_sequence = [0, 1]
        while len(fibonacci_sequence) < n:
            next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
            fibonacci_sequence.append(next_number)

        return fibonacci_sequence[:n]

    @staticmethod
    def is_palindrome(num):
        num_str = str(num)
        return num_str == num_str[::-1]

    @staticmethod
    def reverse_linked_list(head):
        prev = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev


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


if __name__ == "__main__":
    unittest.main()
