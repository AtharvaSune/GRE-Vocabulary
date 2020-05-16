from termcolor import colored
def parse_list(tabspace, inkey, var):

    print(f"{' '*tabspace}{colored(inkey.upper(), 'blue')}")

    tabspace += len(inkey)
    for i in var:
        print(f"{' '*tabspace}: {i}")


def parse_dict(tabspace, inkey, var):
    if inkey is not None:
        print(f"{' '*tabspace}{colored(inkey.upper(), 'blue')}:")
        tabspace += len(inkey)
    for key in var.keys():
        if isinstance(var[key], list):
            parse_list(tabspace, key, var[key])
        
        elif isinstance(var[key], dict):
            parse_dict(tabspace, key, var[key])
        
        elif var[key] is None:
            print(f"{' '*tabspace}{colored(key.upper(), 'blue')}: None")