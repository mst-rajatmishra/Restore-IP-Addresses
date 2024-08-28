class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def is_valid(segment: str) -> bool:
            # Check if the segment is valid
            if len(segment) > 1 and segment[0] == '0':
                return False
            return 0 <= int(segment) <= 255

        def backtrack(start: int, path: List[str]):
            # If we have 4 segments and used all the string, join and add to result
            if len(path) == 4:
                if start == len(s):
                    result.append('.'.join(path))
                return
            
            # Try every possible length for the next segment
            for end in range(start + 1, min(start + 4, len(s) + 1)):
                segment = s[start:end]
                if is_valid(segment):
                    path.append(segment)
                    backtrack(end, path)
                    path.pop()  # backtrack
        
        result = []
        backtrack(0, [])
        return result
