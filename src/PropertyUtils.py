def loadConfigproperties(filepath, sep='=', comment_char='#'):
    """
    Read the file passed as parameter as a properties file.
    """
    props = {}
    print("filepath==>",filepath)
    with open(filepath, "rt") as f:
        for line in f:
            l = line.strip()
            if l and not l.startswith(comment_char):
                key_value = l.split(sep)
                key = key_value[0].strip()
                value = sep.join(key_value[1:]).strip().strip('"')
                props[key] = value
    return props


# print(type(loadConfigproperties("E:/creds/python_reference/db.properties")));
# print(loadConfigproperties("E:/creds/python_reference/db.properties", "_"));
# myProps = loadConfigproperties("E:/creds/python_reference/db.properties");
# # print(type(myProps.get("DB_USER")))
# print(myProps.get("DB_USERNAME"))
