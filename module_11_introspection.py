def introspection_info(obj):
    # тип объекта
    obj_type = type(obj)

    # атрибуты объекта
    attributes = dir(obj)

    # методы объекта
    methods = [attr for attr in attributes if callable(getattr(obj, attr))]

    # модуль, к которому объект принадлежит
    module = obj_type.__module__

    # другие интересные свойства
    properties = {}
    if hasattr(obj, '__dict__'):
        properties['__dict__'] = obj.__dict__
    if hasattr(obj, '__name__'):
        properties['__name__'] = obj.__name__
    if hasattr(obj, '__doc__'):
        properties['__doc__'] = obj.__doc__

    info = {'type': obj_type.__name__,'attributes': attributes,'methods': methods,'module': module, 'properties': properties}

    return info


number_info = introspection_info(42)
print(number_info)