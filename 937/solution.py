class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def sorting_algorithm(log):
            if log[-1].isnumeric():
                return (1,)
            left_side, right_side = log.split(" ", 1)
            return (0, right_side, left_side)
        return sorted(logs, key=sorting_algorithm)

# ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]

# ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
