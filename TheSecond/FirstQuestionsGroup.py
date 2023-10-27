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
