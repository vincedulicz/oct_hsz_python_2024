from o_25_alkalom_01_22.hf.TextComparer.TextComparerABC import TextComparer


class CharTextComparer(TextComparer):
    """ TODO: set1-2 névkonverzió """
    @staticmethod
    def compare_texts(text1: str, text2: str) -> float:
        """ Jaccard hasonlóság char szinten """
        set1 = set(text1)
        set2 = set(text2)
        intersection = len(set1 & set2)
        union = len(set1 | set2)

        return (intersection / union) * 100 if union != 0 else 0.0
