from o_20_alkalom_12_18.backend.fogalmak_meghatarozasok.questionhandler.QuestionHandler import QuestionHandler


class Game:
    """ A játék logikája (business logic) """

    def __init__(self, question_handler: QuestionHandler):
        self._question_handler = question_handler
        self._correct_answears = 0
        self._total_question = 0

    def play(self):
        for _ in range(len(self._question_handler.definiton_provider.fogalmak)):
            valasz, correct_fogalom = self._question_handler.ask_question()

            if valasz.lower() in ['end', 'q', 'quit']:
                break

            self._total_question += 1

            if self._question_handler.definiton_provider.check_answear(valasz, correct_fogalom):
                print("Helyes válasz!")
                self._correct_answears += 1
            else:
                print(f'Rossz válasz. Helyesen: {correct_fogalom}')

    def display_result(self):
        print(f'Helyes válaszok száma: {self._correct_answears} / {self._total_question}')
        if self._total_question > 0:
            print(f'Sikerességi arány: {self._correct_answears / self._total_question * 100:.2f}%')

    def ask_for_new_game(self):
        response = input("Szeretnél-e új játékot?(igen/nem)").strip().lower()
        return response == 'igen'
