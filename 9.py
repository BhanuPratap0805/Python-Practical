# Program to perform operations on a file

def analyze_file(filename):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()

        # a. Count characters, words, lines
        total_lines = len(lines)
        total_chars = sum(len(line) for line in lines)
        total_words = sum(len(line.split()) for line in lines)

        print(f"Total Characters: {total_chars}")
        print(f"Total Words: {total_words}")
        print(f"Total Lines: {total_lines}")

        # b. Frequency of each character
        char_freq = {}
        for line in lines:
            for ch in line:
                char_freq[ch] = char_freq.get(ch, 0) + 1
        print("\nCharacter Frequencies:")
        for ch, freq in char_freq.items():
            # printing \n as \\n for better readability
            printable_char = ch if ch != "\n" else "\\n"
            print(f"'{printable_char}': {freq}")

        # c. Print words in reverse order
        all_words = " ".join(lines).split()
        reversed_words = all_words[::-1]
        print("\nWords in Reverse Order:")
        print(" ".join(reversed_words))

        # d. Copy even and odd lines to separate files
        with open("File1.txt", 'w') as even_file, open("File2.txt", 'w') as odd_file:
            for i, line in enumerate(lines, start=1):
                if i % 2 == 0:
                    even_file.write(line)
                else:
                    odd_file.write(line)

        print("\nEven lines copied to File1.txt")
        print("Odd lines copied to File2.txt")

    except FileNotFoundError:
        print("Error: File not found. Please check the filename.")

# Main program
filename = input("Enter the filename to read: ")
analyze_file(filename)
