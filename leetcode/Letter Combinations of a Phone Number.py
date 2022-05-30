from itertools import product
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        numtoal = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7" :"pqrs", "8":"tuv", "9":"wxyz"}
        data = []
        answer = []
        for num in digits:
            data.append(numtoal[num])
        if len(data) == 0:
            return []
        elif len(data) == 1:
            for pro in product(data[0]):
                answer.append("".join(pro))
        elif len(data) == 2:
            for pro in product(data[0], data[1]):
                answer.append("".join(pro))
        elif len(data) == 3:
            for pro in product(data[0], data[1], data[2]):
                answer.append("".join(pro))
        elif len(data) == 4:
            for pro in product(data[0], data[1], data[2],data[3]):
                answer.append("".join(pro))

        return answer

sol = Solution()
digits = "2345"
sol.letterCombinations(digits)
