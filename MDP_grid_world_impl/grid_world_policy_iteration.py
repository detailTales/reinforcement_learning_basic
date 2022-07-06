import copy
import numpy as np

def grid_world_policy_iteration(row, col, goal, traps, walls):
    # 행동 정의
    np.random.seed(30)
    acts = [(1,0),(-1,0),(0,1),(0,-1)]
    # 격자 각 칸의 보상 초기화 
    rewards = np.zeros((row, col))
    rewards[goal[0], goal[1]] = 1
    for trap in traps:
        rewards[trap[0], trap[1]] = -1
    policys = [[None]*col for i in range(row)]
    # 정책 초기화 
    for i in range(row):
        for j in range(col):
            if (i,j) == goal or (i,j) in traps + walls:
                continue
            act_candidate = []
            for act in acts:
                new_i, new_j = i + act[0], j + act[1]
                if (0 <= new_i < row) and (0 <= new_j < col) and (new_i,new_j) not in walls :
                    act_candidate.append(act)
            policys[i][j] = act_candidate[np.random.randint(len(act_candidate))]
    print("초기화된 정책")
    print_policys(policys)
    step = 0
    while True:
        step += 1
        # 정책 평가
        while True:
            new_rewards = np.copy(rewards)
            max_change = 0
            for i in range(row):
                for j in range(col):
                    policy = policys[i][j]
                    if policy == None:
                        continue
                    new_rewards[i][j] = 0.9 * 0.8 * rewards[i + policy[0]][j + policy[1]]
                    new_i = i + policy[1]
                    new_j = j + policy[0]
                    if (0 <= new_i < row) and (0 <= new_j < col) and (new_i,new_j) not in walls :
                        new_rewards[i][j] += rewards[new_i][new_j] * 0.9 * 0.1
                    else:
                        new_rewards[i][j] += rewards[i][j] * 0.9 * 0.1
                    new_i = i - policy[1]
                    new_j = j - policy[0]
                    if (0 <= new_i < row) and (0 <= new_j < col) and (new_i,new_j) not in walls :
                        new_rewards[i][j] += rewards[new_i][new_j] * 0.9 * 0.1
                    else:
                        new_rewards[i][j] += rewards[i][j] * 0.9 * 0.1
                    if abs(new_rewards[i][j] - rewards[i][j]) > max_change:
                        max_change = abs(new_rewards[i][j] - rewards[i][j]) 
            if max_change < 0.001:
                break
            rewards = new_rewards
        # 정책 개선
        pre_policys = copy.deepcopy(policys)
        is_changed = False
        for i in range(row):
            for j in range(col):
                if policys[i][j] == None:
                    continue
                max_near_reward = -np.inf
                for act in acts:
                    new_i = i + act[0]
                    new_j = j + act[1]
                    if (0 <= new_i < row) and (0 <= new_j < col) and (new_i,new_j) not in walls :
                        if rewards[new_i][new_j] > max_near_reward:
                            max_near_reward = rewards[new_i][new_j]
                            policys[i][j] = act
        if pre_policys == policys:
            break
        print(f"{step}번째 반복")
        print(f"개선 전 정책 측정 \n{rewards}")
        print("개선 된 정책")
        print_policys(policys)
        
             
def print_policys(policys):
    act_dict = {
        (-1,0) : "↑",
        (1,0) : "↓",
        (0,1) : "→",
        (0,-1) : "←",
        None : "X"
    }  
    for rows in policys:
        print([act_dict[i] for i in rows])
        

def main():
    grid_world_policy_iteration(
        row = 3, 
        col = 4, 
        goal = (0,3), 
        traps = [(1,3)], 
        walls = [(1,1)]
    )

if __name__ == "__main__":
    main()
