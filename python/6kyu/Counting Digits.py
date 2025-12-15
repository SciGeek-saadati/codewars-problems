def count_digits(num, rounds):
    for i in range(rounds):
        result = []
        str_num = str(num)
        for ch in str_num:
            number = f"{str_num.count(ch)}{ch}"
            if number not in result:
                result.append(number)
        num = "".join(result)
    result = [int(x) for x in result]
    return result
