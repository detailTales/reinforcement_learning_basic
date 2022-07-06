# Grid World
![image](https://user-images.githubusercontent.com/95160107/177486623-fc4e7a24-79f5-481c-afbe-852617196b0a.png)
<h3> 문제 상황 </h3> 

1. agent는 막혀있지 않은 쪽으로 상 하 좌 우로 이동하는 행동을 취할 수 있다. (X표시가 된 곳도 벽이다.)
2. 특정 방향으로 이동하는 행동을 취했을 때 실제로 그 방향으로 이동할 확률을 0.8이고 반대 방향으로 이동하는 경우는 0 옆으로 이동할 확률은 각각 0.1이다.
    1. 예를 들어 위로 이동하는 행동을 취했을 때 위로 이동할 확률은 0.8 좌로 이동할 확률은 0.1 우로 이동할 확률은 0.1이다.
    2. 아래의 그림처럼 파란 화살표 방향으로 이동하는 행동을 할 경우 옆에 벽이 있는 경우는 이동하지 옆으로 이동하지 못하고 본인의 자리로 머무를 확률이 0.1이 된다.
3. 골과 함정은 종단 상태를 의미하고 각 상태의 보상은 골이 +1 함정이 -1 이고 나머지 상태들에 대한 보상은 0이다.
4. 할인율은 0.9이다.

- 아래 그림은 agent가 위로 가는 행동을 취했을 때 전이되는 상태(격자 위치)와 그로 전이되는 확률을 표현한 예시이다.

![image](https://user-images.githubusercontent.com/95160107/177489466-2387ba4e-899c-431c-b020-dc1a59376a90.png)

<h3> 실행 결과 </h3> 

<h4> value iteration </h4>

```
python grid_world_value_iteration.py
```

- 반복 초기 각 상태(격자)의 가치 

![image](https://user-images.githubusercontent.com/95160107/177491117-b823c70b-7226-4cb4-8dc5-e68543da0f6f.png)

- step 10 일 때 각 상태(격자)의 가치 

![image](https://user-images.githubusercontent.com/95160107/177491275-ba7c8412-3a92-4faa-9e9b-99d22bc1b572.png)

- 수렴된 각 상태(격자)의 가치 

![image](https://user-images.githubusercontent.com/95160107/177491626-e1d7acd0-5aba-4414-95c2-426bf841910f.png)

<h4> policy iteration </h4>

```
python grid_world_policy_iteration.py
```

- 랜덤으로 초기화된 각 상태에서의 정책

![image](https://user-images.githubusercontent.com/95160107/177493099-62cc7776-2b6a-4b03-8e22-73b827926552.png)

- 각 반복에서 정책 측정 결과와 정책 개선 결과, 3번의 측정 개선을 반복하여 정책 수렴

![image](https://user-images.githubusercontent.com/95160107/177494163-98384423-54d7-4252-9559-b9db42fa6d59.png)




