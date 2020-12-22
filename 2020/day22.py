'''
Day 22
https://adventofcode.com/2020/day/22

I realized after doing this that the implementation here would be a lot cleaner 
with lists instead of queues since I didn't actually use a lot of the added 
functionality of the queue. I may go back at some point and clean this all up 
but here is the rough solution I used the night of.
'''
import Queue
import util
import time

def generate_hands(hand):
    player, cards = hand.split(":\n")
    vals = cards.split("\n")
    q = Queue.Queue(maxsize = 2*len(vals))
    for val in vals:
        q.put(int(val))
    return (player, q)

def task1(player1, player2):
    _, hand_1 = generate_hands(player1)
    _, hand_2 = generate_hands(player2)
    while (not hand_1.full()) and (not hand_2.full()):
        val_1, val_2 = hand_1.get(), hand_2.get()
        assert(val_1 != val_2)
        if val_1 > val_2:
            hand_1.put(val_1)
            hand_1.put(val_2)
        else:
            hand_2.put(val_2)
            hand_2.put(val_1)
    result = 0
    queue_lst = []
    if hand_1.full():
        mult_lst = [i for i in range(1, hand_1.qsize() + 1)]
        for i in range(hand_1.qsize()):
            queue_lst = [hand_1.get()] + queue_lst
        
    else:
        mult_lst = [i for i in range(1, hand_2.qsize() + 1)]
        for i in range(hand_2.qsize()):
            queue_lst = [hand_2.get()] + queue_lst
    for i, elt in enumerate(queue_lst):
        result += (i+1) * elt
    return result

    
def task2(player_1, player_2):
    _, hand_1 = generate_hands(player_1)
    _, hand_2 = generate_hands(player_2)
    winning_score, winner = recursive_combat(hand_1, hand_2)
    return winning_score, winner

def recursive_combat(hand_1, hand_2):
    if hand_1.empty():
        return get_score(hand_2), 2
    elif hand_2.empty():
        return get_score(hand_1), 1
    else:
        prior_hands = []
        prior_hands.append((make_list_from_queue(hand_1), make_list_from_queue(hand_2)))
        while (not hand_1.empty()) and (not hand_2.empty()):
            card_1, card_2 = hand_1.get(), hand_2.get()
            if card_1 > hand_1.qsize() or card_2 > hand_2.qsize():
                #play normal game
                assert(card_1 != card_2)
                if card_1 > card_2:
                    hand_1.put(card_1)
                    hand_1.put(card_2)
                else:
                    hand_2.put(card_2)
                    hand_2.put(card_1)
            elif card_1 <= hand_1.qsize() and card_2 <= hand_2.qsize():
                current_hand_1, current_hand_2 = save_hand_state(hand_1), save_hand_state(hand_2)
                sub_hand_1, sub_hand_2 = Queue.Queue(), Queue.Queue()
                for i in range(card_1):
                    sub_hand_1.put(hand_1.get())
                for j in range(card_2):
                    sub_hand_2.put(hand_2.get())
                _, winner = recursive_combat(sub_hand_1, sub_hand_2)
                hand_1, hand_2 = reconstruct_hand_state(hand_1, current_hand_1), reconstruct_hand_state(hand_2, current_hand_2)
                if winner == 1:
                    hand_1.put(card_1)
                    hand_1.put(card_2)
                elif winner == 2:
                    hand_2.put(card_2)
                    hand_2.put(card_1)
            current_hands = (make_list_from_queue(hand_1), make_list_from_queue(hand_2))
            if current_hands in prior_hands:
                return get_score(hand_1), 1
            else: 
                prior_hands.append(current_hands)
        if hand_1.empty():
            return get_score(hand_2), 2
        elif hand_2.empty():
            return get_score(hand_1), 1


def save_hand_state(q):
    saved_lst = []
    for i in range(q.qsize()):
        saved_lst.append(q.get())
        q.put(saved_lst[i])
    return saved_lst


def reconstruct_hand_state (q, lst):
    while not q.empty():
        q.get()
    for elt in lst:
        q.put(elt)
    return q


def make_list_from_queue(q):
    rv = []
    for i in range(q.qsize()):
        rv.append(q.get())
    for elt in rv:
        q.put(elt)
    return rv

def get_score(q):
    queue_lst = []
    result = 0
    mult_lst = [i for i in range(1, q.qsize() + 1)]
    for i in range(q.qsize()):
        queue_lst = [q.get()] + queue_lst
    for i, elt in enumerate(queue_lst):
        result += (i+1) * elt
    return result





if __name__ == "__main__":
    tst_player_1, tst_player_2 = util.read_strs("inputs/day22_test.txt", sep = "\n\n")
    player_1, player_2 = util.read_strs("inputs/day22_input.txt", sep = "\n\n")
    print("TASK 1")
    util.call_and_print(task1, tst_player_1, tst_player_2)
    util.call_and_print(task1, player_1, player_2)

    print("\nTASK 2")
    util.call_and_print(task2, tst_player_1, tst_player_2)
    start = time.time()
    util.call_and_print(task2, player_1, player_2)
    end = time.time()
    print(end - start)

