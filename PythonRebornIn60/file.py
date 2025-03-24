# Exercise 4: Polymorphism with File Readers
# Objective: Read content from different file types using polymorphism.

# Instructions:
# Create a base class FileReader with a method read(self) that raises a NotImplementedError.

# Create two derived classes:
# TextFileReader that overrides read(self) to return "Reading from a text file."
# CSVFileReader that overrides read(self) to return "Reading from a CSV file."
# Write a function read_file(reader) that takes a FileReader object and prints its read() output.
# In main(), create a list of readers (one text and one CSV), and use a loop to call read_file() on each.


class FileReader:
    def read(self):
        raise NotImplementedError


class TextFileReader(FileReader):
    def read(self):
        return "Reading from a text file."


class CSVFileReader(FileReader):
    def read(self):
        return "Reading from a CSV file."


def read_file(reader):
    print(f"{type(reader).__name__}:", reader.read())


def main():
    readers = [TextFileReader(), CSVFileReader()]

    for reader in readers:
        read_file(reader)


if __name__ == "__main__":
    main()
