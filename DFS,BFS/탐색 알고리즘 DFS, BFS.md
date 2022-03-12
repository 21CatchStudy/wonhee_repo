## 자료구조

**자료구조 (Data Structure)** : <mark>데이터를 표현하고 관리하고 처리하기 위한 구조</mark>

- 스택과 큐는 자료구조의 개초 개념
  - 삽입 (Push)
  - 삭제 (Pop)

**탐색 (Search)** : <mark>많은 양의 데이터 중에서 원하는 데이터를 찾는 과정</mark>

- 그래프, 트리 등의 잘구조 안에서 탐색을 하는 문제를 자주 다룸
  - DFS
  - BFS



#### 그래프

- 기본구조 : **노드 (정점), 간선**

- 두 노드는 인접하다 = 두 노드가 간섭으로 연결되어 있다.

- **인접 행렬** : 2차원 배열로 그래프의 연결 관계를 표현하는 방식
  - 2차원 배열에 각 노드가 연결된 형태를 기록하는 방식

- **인접 리스트** : 리스트로 그래프의 연결 관계를 표현하는 방식
  - 모든 노드에 연결된 노드에 대한 정보를 차례대로 연결하여 저장

```python
# 인접 행력 방식 예제
INF = 1e9
graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]
print(graph)

# 인접 리스트 방식 예제
graph = [[] for _ in range(3)]
graph[0].append((1, 7))
graph[0].append((2, 5))
graph[0].append((0, 7))
graph[0].append((0, 5))
print(graph)
```



### DFS

DFS <sub>Depth-First-Search</sub>

- 깊이 우선 탐색
- 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘
  - 최대한 멀리 있는 노드를 우선적으로 탐색하는 방식으로 동작

- 스택 자료구조에 기초
- <u>시간 복잡도 : O(N)</u>

**DFS 예제**

```python
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, v, visited)
            
graph = [[] for _ in range(n+1)]
for _ in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)

dfs(graph, 1, visited)
```



### BFS

BFS <sub>Breadth First Search</sub>

- 너비 우선 탐색

- 가까운 노드부터 탐색하는 알고리즘

- 큐 자료구조 이용

  - 인접한 노드를 반복적으로 큐에 넣어 알고리즘 작성

    1️⃣ 탐색 시작 노드를 큐에 삽입하고 방문 처리 

    2️⃣ 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리

- <u>시간 복잡도 : O(N)</u>
  - 보통의 경우 DFS보다 수행 시간이 좋은 편

**BFS 예제**

```python
from collections import deque

def bfs(graph, start, visited):
    q = deque([start])
    visited[start] = True
    while q:
        now = queue.popleft()
        print(now, end=' ')
        for i in graph[now]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

visited = [False] * (n+1)
bfs(graph, 1, visited)
```



### DFS / BFS 구현 정리

|           | DFS            | BFS               |
| --------- | -------------- | ----------------- |
| 동작 원리 | 스택           | 큐                |
| 구현 방법 | 재귀 함수 이용 | 큐 자료 구조 이용 |

