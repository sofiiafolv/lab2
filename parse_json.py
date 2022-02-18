"""Module string"""
import os.path
import json
def greeting():
    return """Hello, this is a program to parse json file, \
there is some information in it, and this code will help you to navigate \
through this file."""

def input_path():
    print("Please type a path to a json file, which you want to parse: ")
    path = input(">>> ")
    if os.path.isfile(path):
        return path
    return "There is no such file"

def read_file(path_to_json):
    """
    Read json file and return an object from it
    """
    try:
        with open(path_to_json, mode="r",encoding="utf-8-sig") as f:
            data=json.load(f)
        return data
    except FileNotFoundError as err:
        return err

def parse_file(info_list):
    if type(info_list)==list:
        print(f"Write the number from 0 to {len(info_list)-1}: ")
        idx=int(input(">>> "))
        info_dict=info_list[idx]
    elif type(info_list)==dict:
        info_dict=info_list
    while True:
        print("List of choices:\n{}".format("\n".join(list(info_dict.keys()))))
        print()
        print("Pick an information you want to see: ")
        choice=input('>>> ')
        print()
        if choice not in list(info_dict.keys()):
            print("There is no such information")
            break
        elif type(info_dict.get(choice))==dict:
            new_dict=info_dict.get(choice)
            info_dict=new_dict
            continue
        else:
            print(choice,":",info_dict.get(choice))
            break
           
if __name__=="__main__":
    print(greeting())
    parse_file(read_file(input_path()))

