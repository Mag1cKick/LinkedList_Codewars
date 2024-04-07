def linked_list_from_string(s):
    if s == 'None': 
        return None
    if type(s) != list:
        s = s.split(' -> ')[:-1]
    if len(s)!=1:
        return Node(int(s[0]), linked_list_from_string(s[1:]))
    else:
        return Node(int(s[0]))
