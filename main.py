def create_text_file(file_name):
    try:
        with open(file_name, 'w') as file:
            lines = [
                "Hello world!",
                "This is a sample text file.",
                "Words with vowels will be extracted.",
                "Some words will have special characters!",
                "Develop a program."
            ]
            file.write("\n".join(lines))
        print(f"Text file '{file_name}' created successfully.")
    except IOError as e:
        print(f"Error creating file '{file_name}': {e}")

def extract_vowel_words(input_file, output_file):
    try:
        with open(input_file, 'r') as in_file, open(output_file, 'w') as out_file:
            for line in in_file:
                words = line.split()
                vowel_words = [word for word in words if word[0].lower() in 'aeiou']
                out_file.write("\n".join(vowel_words) + "\n")
        print(f"Vowel words extracted to '{output_file}' successfully.")
    except IOError as e:
        print(f"Error processing files: {e}")

def print_file_content(file_name):
    try:
        with open(file_name, 'r') as file:
            print(f"Content of file '{file_name}':")
            for line in file:
                print(line.strip())
    except IOError as e:
        print(f"Error reading file '{file_name}': {e}")

# Задаємо імена файлів
input_file_name = 'TF16_1.txt'
output_file_name = 'TF16_2.txt'

# a) Створення текстового файлу
create_text_file(input_file_name)

# б) Виділення слов, які починаються з голосної літери
extract_vowel_words(input_file_name, output_file_name)

# в) Виведення вмісту другого файлу по рядках
print_file_content(output_file_name)