import file_reader

file_path = 'c:/Users/lekya/OneDrive/Desktop/CNM Assignment 1/example.txt'
num_words = file_reader.count_words(file_path)

print(f'The file "{file_path}" contains {num_words} words.')
