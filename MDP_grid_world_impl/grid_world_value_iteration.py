import numpy as np

def grid_world_value_iteration(row, col, goal, traps, walls):
    # 행동 정의
    acts = [(1,0),(-1,0),(0,1),(0,-1)]
    # 격자 각 칸의 보상 초기화 
    rewards = np.zeros((row, col))
    rewards[goal[0], goal[1]] = 1
    for trap in traps:
        rewards[trap[0], trap[1]] = -1
    # 가치 반복법 
    step = 0
    while step < 100:
        new_rewards = rewards.copy()
        step += 1
        max_change = 0
        for i in range(row):
            for j in range(col):
                values = [0]
                # 보상 함정 벽에 대해선 pass
                if (i,j) == goal or (i,j) in traps + walls:
                    continue
                # 각 행동들에 대한 가치(value)를 구하고 가장 큰 가치로 업데이트
                for act in acts: 
                    new_i = i + act[0]
                    new_j = j + act[1]
                    if (0 <= new_i < row) and (0 <= new_j < col) and (new_i,new_j) not in walls :
                        value = rewards[new_i][new_j] * 0.9 * 0.8
                        new_i = i + act[1]
                        new_j = j + act[0]
                        if (0 <= new_i < row) and (0 <= new_j < col) and (new_i,new_j) not in walls :
                            value += rewards[new_i][new_j] * 0.9 * 0.1
                        else:
                            value += rewards[i][j] * 0.9 * 0.1
                        new_i = i - act[1]
                        new_j = j - act[0]
                        if (0 <= new_i < row) and (0 <= new_j < col) and (new_i,new_j) not in walls :
                            value += rewards[new_i][new_j] * 0.9 * 0.1
                        else:
                            value += rewards[i][j] * 0.9 * 0.1
                        values.append(value)
                new_rewards[i][j] = max(values)
                # 수렴 판단을 위한 최대 변경 값 세팅
                if abs(new_rewards[i][j] - rewards[i][j]) > max_change:
                    max_change = abs(new_rewards[i][j] - rewards[i][j])
        # 수렴 시 반복문 종료
        if max_change < 0.001:
            break
        rewards = new_rewards
        print(f"step: {step}")
        print(rewards)
    

def main():
    grid_world_value_iteration(
        row = 3, 
        col = 4, 
        goal = (0,3), 
        traps = [(1,3)], 
        walls = [(1,1)]
    )

if __name__ == "__main__":
    main()