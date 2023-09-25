#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """divide element by element 2 lists

    Args:
        my_list_1: first list
        my_list_2: second list
        list_length: the length of the new list

    Return: return a newlist with all division
    """
    new_list = []
    for i in range(list_length):
        ans = 0
        try:
            ans = my_list_1[i] / my_list_2[i]
        except (TypeError, ValueError):
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(ans)
    return new_list
