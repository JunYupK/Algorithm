from collections import defaultdict
class Node(object):
    def __init__(self, data, isEnd = None):
        self.data = data
        self.passnumber = defaultdict(int)
        self.children = {}
        self.isEnd = isEnd

class Trie(object):
    def __init__(self):
        self.head = Node(None)
    def insert(self, string):
        current_node = self.head
        current_node.passnumber[len(string)] += 1
        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]
            current_node.passnumber[len(string)] += 1

        current_node.isEnd = True

    def search(self, string):
        current_node = self.head
        for q in string:
            if q == '?':
                break
            if q in current_node.children:
                current_node = current_node.children[q]
            else:
                return 0
        return current_node.passnumber[len(string)]
def solution(words, queries):
    answer = []
    trie = Trie()
    trie_reverse = Trie()

    for word in words:
        trie.insert(word)
        trie_reverse.insert(word[::-1])

    for q in queries:
        if q[0] == '?':
            answer.append(trie_reverse.search(q[::-1]))
        else:
            answer.append(trie.search(q))
    return answer
words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
solution(words,queries)
s = 'abcdef'

#처음엔 비슷한 카카오 문제를 본적이 있어서 딕셔너리 형태로 frodo가 들어오면 frod?, fro??, 형식으로 모든 ?가 들어간 경우의 수를 딕셔너리에 넣고 frodo를
#defaultdict 에 넣어서 len 함수만 써도 바로 검색이 되게 구현을 했다.
#결과는 정확도는 모두 pass, 효율성에서 1,2,3 은 통과를 했지만 4,5 번만 통과를 못했다.
# 아무리 생각해도 더 시간을 줄일 방법이 생각나지 않아서 검색을 해보니 trie 자료 구조를 사용해야만 풀 수가 있는 문제였다.
# 보통 4, 5 번 케이스만 통과하고 1,2,3을 통과못한다는데 나는 1, 2, 3은 통과하고 4, 5 번만 통과를 못했다.
# 아마 보통 검색을 하는 과정에서 효율성테스트에 걸리는거 같은데 나는 검색은 o(n)의 시간이 걸리지만 ?를 붙이는 과정에서 시간초과가 난 것 같다.
# 결론은 trie 자료구조를 사용 안하면 애초에 풀 수 없도록 설계된 문제인거 같다. 문자열 검색에서 n의 개수가 매우 크다면 딕셔너리와 trie를 동시에 떠올려야겠다.



# trie 자료구조도 좋지만 이분탐색을 사용하면 간단하게 해결이 가능해진다! good