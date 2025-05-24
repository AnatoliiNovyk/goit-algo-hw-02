from collections import deque

def is_palindrome(input_string: str) -> bool:
    """
    Перевіряє, чи є рядок паліндромом.
    Нечутлива до регістру та пробілів.
    """
    # Нормалізація рядка: нижній регістр та видалення пробілів
    normalized_string = ''.join(input_string.lower().split())
    
    if not normalized_string: # Порожній рядок або рядок з одних пробілів вважається паліндромом
        return True
        
    char_deque = deque(normalized_string)
    
    while len(char_deque) > 1:
        first_char = char_deque.popleft()
        last_char = char_deque.pop()
        if first_char != last_char:
            return False
            
    return True

# Приклади використання:
if __name__ == "__main__":
    print(f"'А роза упала на лапу Азора' є паліндромом: {is_palindrome('А роза упала на лапу Азора')}")
    print(f"'Race car' є паліндромом: {is_palindrome('Race car')}")
    print(f"'hello' є паліндромом: {is_palindrome('hello')}")
    print(f"'madam' є паліндромом: {is_palindrome('madam')}")
    print(f"' ' є паліндромом: {is_palindrome(' ')}") # Порожній після нормалізації
    print(f"'' є паліндромом: {is_palindrome('')}")   # Порожній рядок
    print(f"'A' є паліндромом: {is_palindrome('A')}")     # Рядок з одного символу
