def create_an_empty_list():
    empty = []
    print(empty)
    return empty

create_an_empty_list()

def create_a_list():
    a_list = ["Tom", "Dick", "Harry", "Moby"]
    print(a_list)
    return (a_list)

create_a_list()

def add_element_to_end_of_list(list, element):
  list= [1, 2, 3, 4] 
  element = 5
  list.append(element)
  print(list)
  return(list)

add_element_to_end_of_list([1, 2, 3, 4], 5)

def add_element_to_start_of_list(list, element):
    list = [1, 2, 3, 4]
    element = 0
    list.insert(0,element)
    print(list)
    return(list)
add_element_to_start_of_list([1, 2, 3, 4], 0)

def remove_element_from_end_of_list(list):
    list = [1, 2, 3, 4]
    list.pop(3)
    print(list)
    return(list)
remove_element_from_end_of_list([1, 2, 3, 4])

def remove_element_from_start_of_list(list):
    list = [1, 2, 3, 4]
    list.pop(0)
    print(list)
    return(list)

remove_element_from_end_of_list(  list = [1, 2, 3, 4])

def retrieve_first_element_from_list(list):
    list = [1, 2, 3, 4]
    element =list[0]
    print(element)
    return(element)

retrieve_first_element_from_list([1, 2, 3, 4])

def retrieve_element_from_index(l, index):
    return None

def retrieve_last_element_from_list(l):
    return None
