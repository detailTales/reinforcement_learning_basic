from unicodedata import name
import numpy as np

def evaluate_and_improve_black_jack_policy():
    step = 0
    Q_map = {}
    while step < 10:
        policys = initial_policys()
        deck = initial_deck()    
        # 카드 두장 받기
        player_cards = np.array([],dtype=int)
        player_cards = np.append(player_cards,deck[-2:])
        deck = np.delete(deck, [-1,-2])
        dealer_open_card = deck[-1] if deck[-1] !=1 else deck[-1] + 10
        deck = np.delete(deck, -1)
        has_ace = 1 if 1 in player_cards else 0
        print(player_cards)
        print(dealer_open_card)
        while sum(player_cards) < 12 and not has_ace:
            player_cards = np.append(player_cards, deck[-1])
            deck = np.delete(deck, -1)
        # 정책 평가
        acts = []
        while sum(player_cards) < 21:
            act = policys[(sum(player_cards),dealer_open_card,has_ace)]
            acts.append(act)
            if act == 0:
                break
            player_cards = np.append(player_cards, deck[-1])
            deck = np.delete(deck, -1)
            print(player_cards)
        print(player_cards)
        if sum(player_cards) < 21:
            while dealer_open_card < 17:
                dealer_open_card += deck[-1] if deck[-1] !=1 else deck[-1] + 10
                deck = np.delete(deck, -1)
                print(dealer_open_card)
                if dealer_open_card > 21:
                    print("player win")
                    return
            if dealer_open_card > sum(player_cards):
                print("dealer win")
            elif dealer_open_card == sum(player_cards):
                print("draw")
            else:
                print("player win")
        elif sum(player_cards) == 21:
            print("player win")
        else:
            print("dealer win")
        break

    
def initial_policys():
    """
    각 상태(player의 카드 합, 딜러의 오픈된 카드, ace 유무) 에 대한 정책을 
    랜덤으로 초기화 후 return
    """
    policys = {}
    for players_sum in range(11,21):
        for dealer_open_card in range(2,12):
            for has_ace in range(2):
                policys[(players_sum,dealer_open_card,has_ace)] = np.random.randint(2)
    return policys
    
def initial_deck():
    """
    덱 초기화 후 return
    10,j,q,k는 모두 10으로 취급    
    """
    deck = np.array([],dtype=int)
    for i in range(10):
        deck = np.append(deck, [i+1]*4)
    for i in range(3):
        deck = np.append(deck, [10] * 4)
    np.random.shuffle(deck)
    return deck

def print_policys(policys):
    """
    각 상태에서 의 정책 출력
    """
    print("ace가 없을 때의 정책")
    policy_table = [["x"] + list(range(2,12))]
    for i in range(20, 10, -1):
        row = [i]
        for j in range(2,12):
            row.append(policys[(i, j, 0)])
        policy_table.append(row)
    for row in policy_table:
        print(row)

if __name__ == "__main__":
    evaluate_and_improve_black_jack_policy()