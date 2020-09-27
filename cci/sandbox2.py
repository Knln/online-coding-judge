def rank(st, we, n):
    if not st:
        return "No participants"

    name_sum = list()
    st_list = st.split(",")

    if n > len(st_list):
        return "Not enough participants"

    # Calculate sum
    for i, name in enumerate(st_list):
        if not name:
            continue
        sum = 0
        for letter in name:
            lower_letter = letter.lower()
            sum = sum + ord(lower_letter) - 96
        sum = sum + len(name)
        sum = sum * we[i]
        name_sum.append(sum)

    sort_name = sorted(name_sum, reverse=True)
    index = name_sum.index(sort_name[n - 1])
    name_sum_dup = name_sum.copy()
    name_sum_dup.remove(sort_name[n - 1])
    if sort_name[n - 1] not in name_sum_dup:
        return st_list[index]
    else:
        list_of_dup_index = list()
        list_of_dup_rank = list()
        for i in range(index, len(name_sum)):
            if sort_name[n - 1] != name_sum[i]:
                break
            else:
                list_of_dup_index.append(i)
        som = sort_name[n - 1]
        print(som)
        for i in range(1, len(sort_name)):
            if sort_name[i-1] == som:
                list_of_dup_rank.append(i)
        print(list_of_dup_rank)
        short_list = st_list[list_of_dup_index[0]:list_of_dup_index[-1] + 1]
        final_list = sorted(short_list)
        answer = final_list[list_of_dup_rank.index(n)]
        print(answer)
        return answer

rank("Elijah,Chloe,Elizabeth,Matthew,Natalie,Jayden", [1, 3, 5, 5, 3, 6], 2)
rank("Addison,Jayden,Sofia,Michael,Andrew,Benjamni,Benjamin", [4, 2, 1, 4, 3, 2, 2], 4)
