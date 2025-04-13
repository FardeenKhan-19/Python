import re

def get_words_by_length(filename, lengths):
    try:
        with open(filename, 'r', encoding="utf-8") as file:
            text = file.read()

        words = re.findall(r'\b\w+\b', text)

        # Dictionary to store words by their length
        length_dict = {length: set() for length in lengths}

        for word in words:
            if len(word) in length_dict:
                length_dict[len(word)].add(word)

        for length in sorted(length_dict.keys()):
            if length_dict[length]:
                print(f'{length}-letter words: {length_dict[length]}')
            else:
                print(f'No {length}-letter words found.')

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except ValueError:
        print("Error: Please enter valid numbers for word lengths.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

filename = input("Enter the name of the file: ")

# User input for word lengths
length_input = input("Enter the lengths of words to find (separated by spaces): ")
if length_input.strip():
    lengths = [int(x) for x in length_input.split() if x.isdigit()]
    get_words_by_length(filename, lengths)
else:
    print("Error: No word lengths provided.")
