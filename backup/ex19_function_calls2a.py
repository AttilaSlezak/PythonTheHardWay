__author__ = 'Slezak Attila'
# -- coding: utf-8 --

def callable_function(it_can_be_anything):
        result = []
        result_builder = ""
        result_builder_type = ""
        coordinate = ""
        deep = 0
        index = 0
        coordinate_changer = 0
        i = 0
        j = 1
        data_in_string = str(it_can_be_anything)
        print(data_in_string)
        for one_char in data_in_string:
            if one_char == "[":
                deep += 1
                result_builder_type = "["
                for one_backet in coordinate:
                    if one_backet == "[":
                        if j == deep:
                            coordinate_changer = i
                        else:
                            j += 1
                    elif one_backet == "]" and deep == j:
                        if coordinate_changer == 0:
                            coordinate = coordinate[:i] + "[" + str(index) + "]"
                        else:
                            coordinate = coordinate[:coordinate_changer+1] + "[" + str(index) + "]" + coordinate[i:]
                    i += 1
                if coordinate == "":
                    coordinate = "[0]"
                index = 0
                i = 0
                j = 1
            elif one_char == "]":
                deep -= 1
            elif one_char == "\"" or one_char == "'":
                if result_builder_type == "" or result_builder_type == "[" or result_builder_type == "(":
                    result_builder_type = "str/o"
                    continue
                elif result_builder_type == "str/o":
                    result_builder_type = ""
                    result.append([coordinate, result_builder, "str"])
                    result_builder = ""
                    index += 1
            elif result_builder_type == "str/o":
                result_builder += one_char
            print(result_builder_type)
        print(result_builder)
        print(result)
        print(it_can_be_anything[0])
        print(it_can_be_anything[0][1])
        print(it_can_be_anything[1][0])


print(callable_function(["Valami", [25, 33, "Még nincs"]]))