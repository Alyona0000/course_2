a = input("введіть код: ")
d = int(a)
#def code_card(a):
 #   d = int(a)
  #  return d % 100, "масть: " + str(d // 100)
if d>=414 or d <= 101:
    print ("код не коректний")
    exit()


suits = {1 :"♠️", 2 :  "♥️", 3 : "♦️", 4 : "♣️"}
ranks = {11 : "J", 12 : "Q", 13 : "K", 14 : "A"}
def code_card(a):
    d = int(a)
    if d % 100 in ranks:
        rank = ranks[d % 100]
    else:
        rank = str(d % 100)
    suit = suits[d // 100]
    return f"масть: {suit}, ранг: {rank}"

# мені подрібно щоб виводило масть і ранг карти через словарь 
print(code_card(a))



# обороботать неверние значение 134,414,101,201,-38,привет.