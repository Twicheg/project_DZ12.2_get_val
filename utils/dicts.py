def get_val(collection,key,default='git'):
    if not collection:
        return default


    return collection[key]