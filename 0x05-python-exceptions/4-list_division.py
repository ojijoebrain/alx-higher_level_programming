#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    my_list_div = []
    for j in range(list_length):
        div = 0
        try:
            div = my_list_1[j] / my_list_2[j]
        except TypeError:
            print('wrong type')
        except ZeroDivisionError:
            print('division by 0')
        except IndexError:
            print('out of range')
        finally:
            my_list_div.append(div)
    return my_list_div
