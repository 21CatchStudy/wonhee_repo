### DFS / BFS

##### 1. [BOJ] dfs와 bfs / 실버 1

> https://www.acmicpc.net/problem/1260

**고려한 점**

- 전체 그래프를 `False (or 0)`로 표현해두고, 방문했다면 `True (or 1)`로 변경

- dfs / bfs 예제 익숙해지기
- 참고_ 이코테 5-8, 5-9

```python
n, m, v = map(int, input().split())
visited = [False] * (n + 1)  # 노드 방문 정보를 입력할 리스트 표현

graph = [[] for _ in range(n + 1)]  # 노드에 입력될 정보 리스트 범위 설정

# 각 노드 연결 정보 입력
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# dfs
def dfs(v):
    print(v, end=' ')
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
            visited[i] = True

# bfs
from collections import deque

def bfs(v):
    q = deque([v])
    visited[v] = True
    while q:
        now = q.popleft()
        print(now, end=' ')
        for i in graph[now]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


print(dfs(v))
visited = [False] * (n + 1)  # dfs, bfs 각각 표현해줘야 하므로 방문처리 초기화
print(bfs(v))
```



-------------------------------------------------------------------------------

##### 2. [BOJ] 바이러스 / 실버 3

> https://www.acmicpc.net/problem/2606

**고려한 점**

- dfs / bfs 예제 익숙해지기
- 정점 노드에 연결된 노드의 개수 구하기

```python
# https://www.acmicpc.net/problem/2606

computer = int(input())
pair = int(input())

graph = [[] for _ in range(computer+1)]

for i in range(pair):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (computer+1)
cnt = 0

def dfs(v):
    global cnt
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
            cnt += 1  # True 방문처리 했으므로 최초 방문시에만 +1

dfs(1)
print("dfs방식 :",cnt)

from collections import deque

def bfs(v):
    global cnt
    q = deque([v])
    visited[v] = True
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                q.append(i)
                visited[i] = True  # # True 방문처리 했으므로 최초 방문시에만 +1
                cnt += 1

bfs(1)
print("bfs방식 :",cnt)
```



-------------------------------------------------------------------

##### 3. [BOJ] 단지번호 붙이기 / 실버 1

> https://www.acmicpc.net/problem/2667

**고려한 점**

- `1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다.` ➡ 탐색하면서 1이 있다면 방문처리인 0으로 변경

- `좌우, 혹은 아래위로 다른 집이 있는 경우` ➡ nx, ny(상, 하, 좌, 우) 활용
- `지도를 입력하여 단지수를 출력` ➡ bfs 1회 진행시 => 1개의 단지의 모든 집 방문
- `단지에 속하는 집의 수를 오름차순으로 정렬` ➡ sort() 사용

- 출력을 위해 선언한 함수
  - 지도의 크기 N
  - N개의 자료 => graph
  - 개별 단지내의 집의 수 => cnt
  - 단지의 수 => result
  - 단지 내의 저장된 집의 수 => house
    - result가 3이라면 house는 3개의 단지에 대한 집 개수 모두 제공

```python
# https://www.acmicpc.net/problem/2667
from collections import deque

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    cnt = 1
    q = deque()
    q.append((x, y))
    graph[x][y] = 0  # 현재 위치 방문처리
    while q:
        x, y = q.popleft()  # 반복문 시작 위치 좌표 꺼내기
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i] 
            if nx < 0 or ny < 0 or nx >= n or ny >= n:  # 범위 밖이면 무시
                continue 
            elif graph[nx][ny] == 1:  # 범위 내에서 집이 있다면 방문 처리 후 저장
                graph[nx][ny] = 0
                q.append((nx, ny))
                cnt += 1  # 집 개수 추가 (최초 1회만)
    return cnt  # bfs 결과 값은 cnt

# 이코테 5-10 부분 참조
result = 0
house = []
for i in range(n):
    for j in range(n):
        # 다른 사람 풀이 참조
        if graph[i][j] == 1:  # 집이 존재한다면, cnt를 bfs함수 내에 선언
            house.append(bfs(i, j))  
            result += 1

print(result)
house.sort()  # 문제 오름차순 조건
for k in house:
    print(k)

```

<span style="color:red">개선해야할 점</span>

- 각 단지별 집의 수 출력하는 방법 (bfs결과를 append)
- bfs / dfs 형식 정확하게 이해하고 외우기



-------------------------------------------------

##### 4. [BOJ] 토마토 / 골드5 

> https://www.acmicpc.net/problem/7576

**고려한 점**

- `보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다.` ➡ 초기 1이 존재하는 x, y 좌표에서부터 시작해야함, <span style="color:red">bfs 사용 (인접한 곳</span>, dfs ❌)
- `왼쪽, 오른쪽, 앞, 뒤 네 방향` ➡ nx, ny 활용
- `정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸` ➡ 초기 1에서 시작해서 상, 하, 좌, 우 방향의 0을 1으로 방문처리 하기
- `토마토들이 며칠이 지나면 다 익게 되는지, 그 최소 일수` ➡ 방문처리 하며 cnt 1씩 증가시키기

- 출력을 위해 선언할 변수
  - 상자 x축 크기 => n, y축 크기 => m
  - 토마토 정보 => tomato
  - 최소 일수 => result

```python
# https://www.acmicpc.net/problem/7576
from collections import deque

m, n = map(int, input().split())
tomato = []
for _ in range(n):
    tomato.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 1이 있는 x, y좌표 찾은 후 queue에 저장하기
q = deque([])  # queue에 저장하기위해 선언, 좌표를 넣기 위한 [] 
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            q.append([i, j])

def bfs():
    # 큐 정의와 저장은 위에서 했으므로 바로 q 반복 돌리기
    while q:
        x, y = q.popleft()  # 초기 1이 존재하는 x, y 좌표 꺼내기
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:  # 범위 벗어나면 무시
                continue
            # 해당 노드를 처음 방문하는 경우에만 최소 일수 기록
            elif tomato[nx][ny] == 0:  # 범위 내에서 다음 좌표값이 0이라면 
                tomato[nx][ny] = tomato[x][y] + 1  # 이코테 5-11 참조
                q.append([nx, ny])  # 방문처리 완

# 다른 사람 풀이 참조
bfs()  # 방문 진행 
result = 0
# 전체 방문 진행 완료 후에 0(익지 않은 토마토) 존재 시 -1 출력
for i in tomato:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)  # '0' 값으로 파이썬 코드 종료
    # 0이 없는 tomato리스트에서 최댓값 출력 
    result = max(result, max(i))
print(result-1)  # 처음 시작이 1이므로 -1 해주기
```

<span style='color:red'>개선해야할 점</span>

- bfs()에 매개변수를 넣지 않고 진행되는 형식 이해 하기
- 출력값이 -1, 0 인 경우 어떻게 구현하는지
- bfs / dfs 형식 정확하게 이해하고 외우기
- 진호님 코드 참고 반영 

```python
result = 0
is_zero = 0
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 0:
            is_zero = 1
        result = max(result, tomato[i][j])

if is_zero == 1:
    print(-1)
else:
    print(result-1)
```

