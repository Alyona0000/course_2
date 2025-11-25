# в чому ідея : ідея в тому _ в залежності від кількості
#  карт ми можемо визначити мінімальний ранг карт цієї масті для того щоб ця комбінація була виграшною у розрізі цієї масті
# тобто напр: якщо в нас є 1 катра - туз : виграшна комбінація
# якщо 2 карти - виграшна комбінація туз та король
# і тд  
# тобто ми у розрізі масті розраховуємо сумарний ранг карт та визначаємо кількість карт цієї масті
# вважаєма що розклад карт цієї масті є виграшом якщо сумарний ранг карт цієї масті більше або = мінімальному рангу для цієї кількості.






import numpy as np 

test1 = np.array([108,208,308,408 ])  
test2 = np.array([311, 112, 213, 314, 413, 209, 111, 107, 414,411, 412])
test3 = np.array([313, 113, 407, 213, 314, 413, 214, 114, 414,411, 412])


def get_cards_by_suit(hand_numbers, suit_index):
    return hand_numbers[ hand_numbers // 100 == suit_index]

def check_winning_combination(hand_numbers,suit_index):
    #розрахувати сумарний ранг та кількість карт у розрізі масті
    dd = get_cards_by_suit(hand_numbers,suit_index)
    #print(dd)
    ff_size = np.size(dd)
    #print(ff_size)
    rang = np.sum(dd%100)
    #print(rang)
    # мінімальний ранг для виграшу 39 для 3 карт туз король дама
    # індекс в масиві це кількість карт
    min_rangs = np.array([ 0, 14, 27, 39, 50, 54, 61, 71, 84])
    min_rang_for_hand = min_rangs[ff_size]
    #print(min_rang_for_hand)
    return rang >= min_rang_for_hand

def case_5(hand_numbers):
    r = np.array([
        check_winning_combination(hand_numbers,1),
        check_winning_combination(hand_numbers,2),
        check_winning_combination(hand_numbers,3),
        check_winning_combination(hand_numbers,4)
    ])
    return np.all(r)





print("test1:", case_5(test1))  
print("test2:", case_5(test2)) 
print("test3:", case_5(test3)) 



