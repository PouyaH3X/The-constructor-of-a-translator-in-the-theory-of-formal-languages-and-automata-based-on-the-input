n = int(input("please enter the number of vars : "))
var = []
for i in range(n):
    var.append(input(f"enter name of var {i} :"))
alph = input("Input alphanet : ").split(",")
o_alph = input("Output alphabet : ").split(",")
st = input('Start var : ')

if st not in var:
    print("start must be in var name")
else:

    print()
    print("""for transmitions, enter in the format (x1,x2,x3,x4) as :
          x1 = current var
          x2 = given input alph
          x3 = next var
          x4 = output
          
          """)
    tmp_trs = []
    count = 1
    print(f'You have to inter {len(var) * len(alph)} transition functions')
    print("--------------------------------")
    while True:
        c = True
        n = input(f"enter transition function no.{count} : ").split(",")
        if len(n) == 4:
            if n[0] in var and n[1] in alph and n[2] in var and n[3] in o_alph:
                for i in tmp_trs:
                    if n[0] == i[0] and n[1] == i[1]:
                        break
                else:
                    tmp_trs.append(n)
                    print(f"Sucess,{len(var)*len(alph)-len(tmp_trs)} left !")
                    count += 1
                    c = False
                if c:
                    print(f"{n[0], n[1]} used before !")
            else:
                print(
                    "Invalid input(notice your inputs must be the same with variables and input alphabet.)")
        else:
            print("Invalid form")

        if len(tmp_trs) == len(var)*len(alph):
            print("--------------------------------")
            break
    print()
    translate = []
    for al in var:
        lis = []
        for func in tmp_trs:
            if al == func[0]:
                lis.append(func)
        translate.append(lis)

    while True:
        tr = input("Now enter your string to translate : ")
        for i in tr:
            if i not in alph:
                print("Wrong input alphabet")
                break
        else:
            print("Output = ", end="")
            for i in tr:
                # print(st)
                x = int(var.index(st))
                for j in translate[x]:
                    # print(j,x)
                    if i == j[1]:
                        print(j[3], end="")
                        st = j[2]
                        break
            print()
