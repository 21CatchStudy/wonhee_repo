def bfs(begin, words):
    q = deque()
    q.append(words)
    while q:
        word = q.popleft()
        for i in range(len(begin)):
            if begin[i] == word[i]:
                begin = word
                bfs(begin, words)





  def find(x, y):
        difference = 0
        for i in range(len(x)):
            if x[i] != y[i]:
                difference += 1
        if difference == 1:
            return True
        return False





from collections import deque
def solution(begin, target, words):
    answer = 0
    visited = [0 for _ in range(len(words))]
    if target not in words:
        return 0

    """
    helper 함수를 통해, 오직 한 부분만 다른 단어를 찾는다. 
    """
    def compare_helper(aWord,bWord):
        difference=0
        for i in range(len(aWord)):
            if aWord[i] != bWord[i]:
                difference+=1
        if difference ==1:
            return True
        return False



    """
    주의사항. 변환할 수 없는 경우는, 
    1) target word가 아예 리스트에 없다. line6에서 해결 
    2) target word가 있음에도 불구하고, 어떠한 경로를 거치더라도 (최대 len(words)겠지) visited가 꽉 찼는데도, current 와 target이 같아지지 않는 경우.
    """
    def bfs(current, words,visited):
        """
        words 중에서 aword(현재 단어)에서 변환이 가능한 조건을 지닌 단어들만을 큐에 추가한다.
        헬퍼 함수의 도움을 받는다.
        """
        queue= deque()
        queue.append((current,0))
        while queue:
            aword = queue.popleft()
            if aword[0] == target:
                return aword[1]

            for i in range(len(words)):
                if compare_helper(aword[0], words[i]) and visited[i] ==0:
                    queue.append((words[i],aword[1]+1))
                    # print(words[i], end =' ')
                    visited[i] = 1
        return 0

    return bfs(begin, words, visited)


def diff_check(word1, word2):
    diff = 0
    for a, b in zip(word1, word2):
        if a != b:
            diff += 1
    if diff == 1:
        return True
    else:
        return False


def solution(begin, target, words):
    from collections import deque
    Q = deque()
    cnt = 0
    Q.append((begin, 0))
    while Q:
        current, cnt = Q.popleft()
        if current == target:
            return cnt
        # hot -> hit -> hot
        if cnt == len(words):
            continue
        for word in words:
            if diff_check(current, word):
                Q.append((word, cnt + 1))

    return 0
