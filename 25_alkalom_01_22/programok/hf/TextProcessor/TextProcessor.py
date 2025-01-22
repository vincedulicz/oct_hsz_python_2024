class TextProcessor:
    """ TODO: hol a readfile? """
    @staticmethod
    def load_file(file_path: str) -> str:
        """ Load file return content """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError as e:
            return f'Hiba: {e}'
        except IOError as e:
            return f'Hiba: {e}'
        except Exception as e:
            return f'Hiba: {e}'

    @staticmethod
    def prepare_text(text: str) -> str:
        """ normalizálás a szövegre """
        return ' '.join(text.lower().split())
