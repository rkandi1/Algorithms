""" Question 3 """
def make_calculation(lst):
    num_lst = []
    evaluation = 0
    for val in lst:
        if type(val) is int:
            num_lst.append(val)
        else:
            last = num_lst.pop()
            second_last = num_lst.pop()
            if val == "+":
                evaluation = second_last + last
                num_lst.append(evaluation)
            elif val == "-":
                evaluation = second_last - last
                num_lst.append(evaluation)
            elif val == "*":
                evaluation = second_last * last
                num_lst.append(evaluation)
            else:
                evaluation = second_last / last
                num_lst.append(evaluation)

    return num_lst[0]


def list_variable(lst):
    word_lst = inp.split(" ")
    variable_name = word_lst[0]
    num_lst= []
    for i in range(2, len(word_lst)):
        if word_lst[i].isdigit():
            num_lst.append(int(word_lst[i]))
        else:
            num_lst.append(word_lst[i])
    evaluation = make_calculation(num_lst)

    return variable_name, evaluation


if __name__ == "__main__":
    variable_eval = {}
    while True:
        print("-->", end=" ")
        inp = str(input())

        if inp == "done()":
            break

        if not inp[0].isdigit():
            num_lst = inp.split(" ")
            if "=" in num_lst:
                print(list_variable(num_lst)[0])
                variable_eval[list_variable(num_lst)[0]] = list_variable(num_lst)[1]
            else:
                if len(num_lst) > 1:
                    temp_lst = []
                    for var in num_lst:
                        if var not in "-+*/":
                            if var in variable_eval.keys():
                                temp_lst.append(variable_eval[var])
                        else:
                            temp_lst.append(var)
                    print(make_calculation(temp_lst))

                else:
                    val = variable_eval[num_lst[0]]
                    print(val)

        else:
            num_lst = inp.split(" ")
            for i in range(len(num_lst)):
                if num_lst[i].isdigit():
                    num_lst[i] = int(num_lst[i])
            print(make_calculation(num_lst))

