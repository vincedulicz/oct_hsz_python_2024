from o_25_alkalom_01_22.hf.TextComparer.TextComparerABC import TextComparer
from o_25_alkalom_01_22.hf.TextProcessor.TextProcessor import TextProcessor


class FileComparer:
    """ TODO: property """
    def __init__(self, comparer: TextComparer):
        self.procesor = TextProcessor()
        self.comparer = comparer

    def compare_files(self, file1: str, file2: str) -> float:
        """ compare the content of the 2 files """
        try:
            text1 = self.procesor.prepare_text(self.procesor.load_file(file1))
            text2 = self.procesor.prepare_text(self.procesor.load_file(file2))

            return self.comparer.compare_texts(text1, text2)
        except RuntimeError as e:
            print(e)
            return 0.0
