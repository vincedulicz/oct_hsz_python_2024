from o_25_alkalom_01_22.hf.FileComparer.FileComparer import FileComparer
from o_25_alkalom_01_22.hf.ResultPrinter.ResultPrinter import ResultPrinter
from o_25_alkalom_01_22.hf.TextComparer.CharTextComparer import CharTextComparer
from o_25_alkalom_01_22.hf.TextComparer.SimpleTextComparer import SimpleTextComparer


def main():
    """ TODO: névkonverzió """
    file1 = "data/407.txt"
    file2 = "data/408.txt"

    word_comparer = FileComparer(SimpleTextComparer())
    word_result = word_comparer.compare_files(file1, file2)

    printer = ResultPrinter()
    printer.print_result(word_result, "word-level")

    char_comparer = FileComparer(CharTextComparer())
    char_result = char_comparer.compare_files(file1, file2)

    printer.print_result(char_result, "char-level")


if __name__ == "__main__":
    main()
