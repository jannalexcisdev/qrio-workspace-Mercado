import time

def main():
    hello_world_string = "Hello, World!"
    print(hello_world_string)

    # print the first character of the string
    print(hello_world_string[0])

    # print the last character of the string
    print(hello_world_string[-1])

    # print the first 5 characters of the string
    print(hello_world_string[:5])

    # print the last 5 characters of the string
    print(hello_world_string[-5:])

    # print the string in reverse
    print(hello_world_string[::-1])

    # replace the word "World" with the word "Universe"
    print(hello_world_string.replace("World", "Universe"))

    # split the string into a list
    print(hello_world_string.split(","))

    list_of_words = hello_world_string.split(",")
    print(list_of_words)
    print(list_of_words[0])
    print(list_of_words[1])

    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    days_of_week.append("New day")

    print(days_of_week)

    person = {
        "name": "John",
        "age": 20,
        "city": "New York"
    }

    print(person.get('names'))
    print(person['ages'])
    print(person['city'])
    
    
def order_item(item_id:int):
    return {
        "id": item_id,
        "name": "Item " + str(item_id),
        "price": 10
    }

def checkout(item):
    return item["price"]

def pay(total):
    print(total)

    
if __name__ == "__main__":
    item = order_item(1)
    total = checkout(item)
    pay(total)

