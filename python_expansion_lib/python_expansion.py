import numpy as np


class Pexpansion:
    """Manipulations of basic data structure int, float, str, list ,set ,dict"""

    @staticmethod
    def if_x_not_ls_make_x_ls(x):
        if type(x) == list:
            return x
        else:
            return [x]

    @staticmethod
    def flatten_ls(ls):
        if len(ls) == 0:
            return ls
        if isinstance(ls[0], list):
            return Pexpansion.flatten_ls(ls[0]) + Pexpansion.flatten_ls(ls[1:])
        elif isinstance(ls[0], (set, tuple)):
            return Pexpansion.flatten_ls(list(ls[0])) + Pexpansion.flatten_ls(ls[1:])
        return ls[:1] + Pexpansion.flatten_ls(ls[1:])

    @staticmethod
    def get_key_from_dict_by_value(dictionary, value):
        for key in dictionary:
            if value in dictionary[key]:
                return key

    # test
    @staticmethod
    def del_duplicate_values_in_key_of_dict(dictionary):
        for key in dictionary.keys():
            array = np.array(dictionary[key])
            array = array.flatten()
            dictionary[key] = list(set(array))
        return dictionary

    # test
    @staticmethod
    def merge_dicts(dict1, dict2):
        ''' keep values of common keys in list'''
        dict3 = {**dict1, **dict2}
        for key, value in dict3.items():
            if key in dict1 and key in dict2:
                dict3[key] = [dict1[key], dict3[key]]

        for key in dict3:
            dict3[key] = Pexpansion.flatten_ls(list(dict3[key]))
        return dict3
    
    @staticmethod
    def upside_down_dictionary(dictionary):
        new_dictionary = dict()
        for k in dictionary.keys():
            v = Pexpansion.if_x_not_ls_make_x_ls(dictionary[k])
            for i in v:
                if i in new_dictionary.keys():
                    new_dictionary[i].append(k)
                else:
                    new_dictionary[i] = [k]
        return new_dictionary

    @staticmethod
    def replace_str_by_comparison(string, replacement_dict):
        """
        dict_compare:dict,{replacement_value: [ list of compare value], ..}
        """
        for k in replacement_dict:
            for i in replacement_dict[k]:
                string = string.replace(i, k)
        return string

    # TODO: test
    @staticmethod
    def strip_element_in_ls(ls):
        for i in range(len(ls)):
            if type(ls[i]) == str:
                ls[i] = ls[i].strip()
        return ls

    @staticmethod
    def remove_from_flat_ls(ls, ls_of_remove):
        ls_of_remove = Pexpansion.if_x_not_ls_make_x_ls(ls_of_remove)
        ls = Pexpansion.strip_element_in_ls(ls)
        for i in ls_of_remove:
            ls = list(filter(lambda x: x != i, ls))
        return ls

    # TODO: test
    @staticmethod
    def from_ls_to_str_tag_separated(ls, tag=","):
        """ deletes the duplicates and  NONE from ls """
        if None in ls:
            ls.remove(None)
        string = tag.join([str(i) for i in ls])
        return string

    # TODO: test
    @staticmethod
    def select_category_by_importance(x, dictionary_importance):
        """importance: Determined by a dictionary
        the smaller the number is the more important it is
        and will choose over others"""
        ls = x.split(", ")
        ls = [i.strip() for i in ls]
        ls_degree_importance = []
        for i in ls:
            ls_degree_importance.append(dictionary_importance[i])
        max_importance_index = ls_degree_importance.index(min(ls_degree_importance))
        return ls[max_importance_index]

    # TODO: test
    @staticmethod
    def filter_value_counts_dict_by_amount_value(dictionary, min_amount_num):
        new_dict = {}
        for k, v in dictionary.items():
            if v > min_amount_num:
                new_dict[k] = v
        return new_dict

    @staticmethod
    def del_duplicate_categories_in_multicategories_str(x):
        if type(x) == str:
            return ",".join(sorted(list(set(x.split(",")))))

    @staticmethod
    def str_of_dicts_keys(ls_dicts): #str_of_keys_from_dicts
        """
        Gets a list of dictionaries and returns a string of names of
        all keys. the keys separated by ","

        input:
        ls_dicts: list
            list of dicts [dict, dict]

        return:
        keys:str
            "key, key, key"
        """
        keys = []
        for dic in ls_dicts:
            keys.append(list(dic.keys()))
        keys = Pexpansion.from_ls_to_str_comma_separated(keys)
        return keys

    # TODO: test
    @staticmethod
    def decade_of_range(ls_range):
        # standart ["89","9"] -> ["89","09"]
        for i in range(len(ls_range)):
            if len(ls_range[i]) == 1:
                ls_range[i] = "0" + ls_range[i]

        return ls_range

    # TODO: test
    @staticmethod
    def from_word_ls_to_roots_str(x, ps):
        """make ls of words to str of roots separated by ' ' """
        ls = [ps.stem(i) for i in x]
        return ' '.join(ls)

    # TODO: test
    @staticmethod
    def make_dict_with_empty_ls_as_value(ls_keys):
        return dict(zip(ls_keys, [[] for i in range(len(ls_keys))]))

    @staticmethod
    def make_dict_with_empty_str_as_value(ls_keys):
        return dict(zip(ls_keys, ["" for i in range(len(ls_keys))]))

    ## TODO: test
    @staticmethod
    def set_up_class_var(dict_var, instance):
        for k, v in dict_var.items():
            setattr(instance, k, v)

    # TODO: test
    @staticmethod
    def return_npnan_instead_empty_space(x):
        if type(x) == str:
            if x.strip() == "":
                return None
            else:
                return x
        else:
            return x

    @staticmethod
    def v():
        print(14)
