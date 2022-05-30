    class Solution:
        def convert(self, s: str, numRows: int) -> str:
            if numRows == 1: return s
            answer = [[] for _ in range(numRows)]
            cycle = (numRows - 1) * 2
            check = True
            count = 0
            start = 0
            for i in range(0,len(s),cycle):
                print(s[i:i+numRows], s[i+numRows:i+numRows+(cycle - numRows)])
                tmp1 = s[i:i+numRows]
                tmp2 = s[i+numRows:i+numRows+(cycle - numRows)]
                for j in range(len(tmp1)):
                    answer[j].append(tmp1[j])
                index = numRows-1
                for j in range(len(tmp2)):
                    index -= 1
                    answer[index].append(tmp2[j])
            result = []
            for data in answer:
                result += data
            return "".join(result)
    sol = Solution()
    s = "PAYPALISHIRING"
    sol.convert(s,4)