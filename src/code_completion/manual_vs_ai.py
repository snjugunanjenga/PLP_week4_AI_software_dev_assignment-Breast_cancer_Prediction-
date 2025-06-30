# File: src/code_completion/manual_vs_ai.py
"""
Task 1: AI-Powered Code Completion
- Manual implementation vs. AI-suggested implementation
- Sorting a list of dictionaries by a specified key
"""

def sort_dicts_by_key_manual(dicts_list, sort_key):
    """
    Manually sort a list of dictionaries by the specified key.
    Falls back to None for missing keys and handles mixed types.
    """
    try:
        return sorted(dicts_list, key=lambda d: d.get(sort_key, None))
    except TypeError:
        return sorted(dicts_list, key=lambda d: str(d.get(sort_key, '')))


def sort_dicts_by_key_ai(dicts_list, sort_key):
    """
    AI-suggested version: Sort dictionaries by given key,
    placing items without the key at the end.
    """
    
    default = float('inf')
    return sorted(
        dicts_list,
        key=lambda d: convert_to_sortable(d.get(sort_key, default))
    )

def convert_to_sortable(value):
    """
    Ensures all values are comparable by converting to float if possible, else to string.
    """
    try:
        return float(value)
    except (TypeError, ValueError):
        return str(value)

# Test data
data = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob'},
    {'name': 'Charlie', 'age': 25},
    {'name': 'Diana', 'age': '27'}
]

if __name__ == "__main__":
    print("Manual sort by 'age':")
    print(sort_dicts_by_key_manual(data, 'age'))
    print("\nAI sort by 'age':")
    print(sort_dicts_by_key_ai(data, 'age'))
