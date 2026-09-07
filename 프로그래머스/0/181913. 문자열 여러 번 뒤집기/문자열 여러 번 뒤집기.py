def solution(my_string, queries):
    my_str = my_string
    for key in queries:
        start = key[0]
        end = key[1]
        str1 = my_str[:start]
        str2 = my_str[start:end + 1][::-1]  # start부터 end까지 추출 후 뒤집기
        str3 = my_str[end + 1:]            # end 다음부터 끝까지
        my_str = str1 + str2 + str3
    return my_str