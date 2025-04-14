    #find first non_repeating character in string


    def non_character(str):
        dict={}
        for i in str:
            dict[i]=dict.get(i,0)+1
        print(dict)


        for i in str:
            if dict[i]==1:
                return i

        return None
    str="ppuurrsm"

    result=non_character(str)
    if result:
        print(result)
    else:
        print("repeated")