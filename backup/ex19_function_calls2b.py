__author__ = 'Slezak Attila'
# -- coding: utf-8 --

def index_counter(result, deep):
    i = 0
    j = 1
    max_index_in_deep = 0
    where_is_index = []
    for one_result in result:
        for one_backet in one_result[0]:
            print("Mi: ", one_backet)
            if one_backet == "[":
                if j == deep:
                    where_is_index.append(i+1)
                else:
                    j += 1
            elif one_backet == "]" and where_is_index != []:
                where_is_index.append(i)
            i += 1
        print("Where is index: ", where_is_index)
        if where_is_index != []:
            if max_index_in_deep == 0:
                max_index_in_deep = int(one_result[0][where_is_index[0]:where_is_index[1]])
            elif max_index_in_deep < int(one_result[0][where_is_index[0]:where_is_index[1]]):
                max_index_in_deep = int(one_result[0][where_is_index[0]:where_is_index[1]])
    print("Max index:", max_index_in_deep)
    return max_index_in_deep

def callable_function(it_can_be_anything):
        result = []
        result_builder = ""
        result_builder_type = ""
        coordinate = ""
        deep = 0
        index = 0
        coordinate_changer = []
        i = 0
        j = 1
        data_in_string = str(it_can_be_anything)
        print(data_in_string)
        for one_char in data_in_string:
            if one_char == "," and result_builder_type != "str/o":
                index += 1
            elif one_char == "[":
                deep += 1
                index = index_counter(result, deep)
                result_builder_type = "["
                for one_backet in coordinate:
                    if one_backet == "[":
                        coordinate_changer.append(i)
                    i += 1
                if deep > len(coordinate_changer) and len(coordinate_changer) != 0:
                    coordinate = coordinate[:coordinate_changer[len(coordinate_changer)-1]] + "[" + str(index) + "]" + "[0]"
                elif len(coordinate_changer) == 0:
                    coordinate = "[" + str(index) + "]"
                i = 0
                #  actual_coordinate = actual_coordinate[:i] + "[" + str(index) + "]"
                #  actual_coordinate = actual_coordinate[:coordinate_changer+1] + "[" + str(index) + "]" + actual_coordinate[i:]
            elif one_char == "]":
                deep -= 1
                index = index_counter(result, deep)
            elif one_char == "\"" or one_char == "'":
                if result_builder_type == "" or result_builder_type == "[" or result_builder_type == "(":
                    result_builder_type = "str/o"
                    continue
                elif result_builder_type == "str/o":
                    result_builder_type = ""
                    result.append([coordinate, result_builder, "str"])
                    result_builder = ""
            elif result_builder_type == "str/o":
                result_builder += one_char
            print(result_builder_type)
        print(result_builder)
        print(result)
        print(it_can_be_anything[0])
        print(it_can_be_anything[0][1])
        print(it_can_be_anything[1][0])


print(callable_function(["Valami", [25, 33, "Még nincs"], "Hihi!"]))