def list_sort(particular_list):
    odds,evens,chars=[],[],[]
    for x in particular_list:
        if (isinstance(x,str)):
            strings.append(x)
            if x % 2 != 0 :
                odds.append(x)
                if x % 2 == 0 :
                    evens.append(x)
                    return {'odds':odds,'evens':evens,'chars':strings}