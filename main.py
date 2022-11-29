
guest_list = []

for i in range(1,6):
    guest =input("security yourname plese :")
    guest_list.append(guest)
    print(guest_list)

print(guest_list)
a = 0

abc = {}
a = 1

while True:
    name_pease =input("youre nmae  :")
    b = a
    if name_pease in guest_list:
        khaichhantiki  = input("kichhanti : y: n: ").lower()
        if khaichhantiki == "y":
            abc[name_pease]  = b+1
            print(f"khaichhi {abc}times")
        else:
            print("give him chien for the first time ")
            abc[name_pease] = b
            print(f"khaichhi {abc}times")

