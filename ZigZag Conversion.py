class Solution:
    def convert(self, s: str, numRows: int) -> str:
        row_collection = [[] for _ in range(numRows)]
        i = 0
        j = 0
        arrow = False
        total_str = ''
        
        if numRows == 1:
            return s

        for letter in s:
            row_collection[j].append(letter)
            j += 1 if not arrow else -1 
            
            if not j or j == numRows - 1:
                arrow = not arrow

        for stroka in row_collection:
            total_str += ''.join(stroka)

        return total_str


a = Solution()
res = a.convert("ANALYSRESHENIYA", 4)
print(res)