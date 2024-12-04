def introspection_info(obj):
    obj_type = type(obj).__name__
    all_attributes = dir(obj)
    all_methods = [method for method in all_attributes if
                   callable(getattr(obj, method)) and not method.startswith('__')]
    attributes = [attr for attr in all_attributes if not attr.startswith('__') and attr not in all_methods]
    obj_module = getattr(obj, '__module__', '__main__')
    info = {
        'type': obj_type,
        'attributes': attributes,
        'methods': all_methods,
        'module': obj_module
    }
    return info


number_info = introspection_info(42)
print(number_info)
