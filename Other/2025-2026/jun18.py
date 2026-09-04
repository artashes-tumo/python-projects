# def front3(str):
#     if len(str) < 3:
#         print(str * 3)
#     else:
#         print(str[:3] * 3)

# front3("Java")
# front3("Chocolate")
# front3("abc")
# front3("abcXYZ")
# front3("ab")
# front3("a")
# front3("")

def sleep_in(weekday, vacation):
    if not weekday or vacation:
        print("True")
    else:
        print("False")

sleep_in(False, False)
sleep_in(True, False)
sleep_in(False, True)