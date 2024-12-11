from pprint import pprint
import inspect


def  introspection_info(obj):
    type_object = str(type(obj))
    atributtes = dir(obj)
    methods = dir(type_object)
    module = introspection_info.__module__
    my_dictionary = {'type_object': type_object,
                     'atributtes': atributtes,
                     'methods': methods,
                     'modules': module
                     }

    return  my_dictionary
number_info = introspection_info(42)
pprint(number_info)
