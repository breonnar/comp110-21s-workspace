"""Utility functions for wrangling data."""

__author__ = "730327440"


from csv import DictReader


def read_csv_rows(csv_file: str) -> list[dict[str, str]]:
    """Read a CSV file's contents into a list of rows."""
# TODO 0.1) Complete the implementation of this function here.
    data: list[dict[str, str]] = []
    file_handle = open(csv_file, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        data.append(row)
    file_handle.close()
    return data


# TODO: Define the other functions here.
def column_values(table: list[dict[str, str]], names: str) -> list[str]:
# column values names turning into a list
    col_val: list[str] = []
        for all_row in table:
        col_val.append(all_row[names])
    return col_val
        

def columnar(co: list[dict[str,str]]) -> dict[str,list[str]]:
# first_kv is all of the names in code at index 0, new dict[column name]: make it equal to the list of values of age 
    new_dict: dict[str, list[str]] = {}
    for first_kv in co[0]: 
        new_dict[first_kv] = column_values(co, first_kv)
    return new_dict
    

def head(cb_table:dict[str, list[str]], row_num: int) -> dict[str, list[str]]:
# making a new column based table with int
    head_dict: dict[str, list[str]] = {}
    for each_col in cb_table:
        list_str = []
        for i in range(0, row_num):
            if i < len(cb_table[each_col]):
                list_str.append(cb_table[each_col][i]) 
        head_dict[each_col] = list_str 
    return head_dict


def select(cb2_table: dict[str, list[str]], new_cols: list[str]) -> dict[str, list[str]]: 
# make a new column with certain cols from original cols
    new_dict = {}
    for cols in new_cols:
        new_dict[cols] = cb2_table[cols]
    return new_dict


def count(oki: list[str]) -> dict[str, int]:
#associating keys with the amount of time their values appeared 
    built = {}
    for elements in oki: 
        if elements in built: 
            built[elements] += 1
        else: 
            built[elements] = 1
    return built 


    






