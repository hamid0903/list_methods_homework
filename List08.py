def main(fruits):
    """
    A list called "fruits" is given and is five in length and contains at least one "apple". Remove the apples from the list and return the list.
    Args:
        fruits(list): parameter
    Returns:
        list: return answer
    """
    
    i=fruits.index('apple')
    print(i)
    fruits.pop(i)
    i=fruits.index('apple')
    print(i)
    fruits.pop(i)
    i=fruits.index('apple')
    print(i)
    return fruits
print(main(['apple', 'apple', 'apple', 'peach', 'apple']))