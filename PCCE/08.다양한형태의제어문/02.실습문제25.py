#25
push_up=int(input("팔굽혀펴기:"))
sit_up=int(input("윗몸일으키기:"))
chin_up=int(input("턱걸이:"))

if push_up>=30 or sit_up>=35 or chin_up>=5:
    print("pass")
else:
    print("fail")