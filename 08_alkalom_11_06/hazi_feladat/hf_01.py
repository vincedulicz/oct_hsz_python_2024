# Fogalmak és meghatározások listái

import random

fogalmak = [
    'majorság', 'hűbéres', 'jobbágy', 'nemes', 'tized',
    'kilenced', 'robot', 'szügyhám', 'vetésforgó', 'ugar', 'lovag'
]

meghatarozasok = [
    'Egy-egy nagybirtok vagy valamely részének igazgatási központja.',
    'Aki örökletes használatra megkapja a földet.',
    'Telkes paraszt, aki a földesúrtól kapott földön gazdálkodik.',
    'Kiváltságos réteg.',
    'Egyházi adó.',
    'Földesúrnak beszolgáltatott adó.',
    'Ötvenkét igás, vagy 104 kézimunka nap kötelezettség.',
    'Igavonási találmány, melynek köszönhetően nem az állat nyakában van a húzó eszköz.',
    'A termőföld használata évszakonként más és más.',
    'Művelés alá nem vont terület.',
    'Vagyonos katonai szolgálattevő lóval, páncéllal.'
]


def create_dictionary(fogalmak, meghatarozasok):
    """ Létrehozza a fogalmak és megh. dict.-ét """

    return {meghatarozas: fogalom
            for fogalom, meghatarozas in zip(fogalmak, meghatarozasok)
            }


def get_random_definition(fogalom_meghatarozas_dict):
    """ Véletlenszerűen választ egy meghatározást """

    meghatarozas = random.choice(list(fogalom_meghatarozas_dict.keys()))

    return meghatarozas, fogalom_meghatarozas_dict[meghatarozas]


def check_answear(user_answear, correct_answear):
    """ Ellenőrízzük az eredményt """

    return user_answear.lower().strip() == correct_answear.lower()


def ask_question(meghatarozas, correct_fogalom):
    """ Feltettt kérdés kezelése """

    print(f'\n(END/Q/QUIT) Meghatározás: {meghatarozas}')
    valasz = input("Melyik fogalom társul ehhez? : ").strip()

    return valasz, correct_fogalom


def play_game(fogalom_meghatarozas_dict):
    """ Játék főprogram """

    correct_answears = 0
    total_questions = 0 # len(fogalom_meghatarozas_dict)

    fogalom_meghatarozas_keys_in_list = list(fogalom_meghatarozas_dict.keys())
    random.shuffle(fogalom_meghatarozas_keys_in_list)

    for meghatarozas in fogalom_meghatarozas_keys_in_list:
        correct_fogalom = fogalom_meghatarozas_dict[meghatarozas]
        valasz, correct_fogalom = ask_question(meghatarozas, correct_fogalom)

        if valasz.lower() in ["end", "q", "quit"]:
            break

        total_questions += 1

        if check_answear(valasz, correct_fogalom):
            print("Helyes válasz!")
            correct_answears += 1
        else:
            print(f'Rossz válasz. Helyesen: {correct_fogalom}')

    return correct_answears, total_questions


def display_result(correct_answears, total_questions):
    """ Kiírja az eredményt """

    print(f'Helyes válaszok száma: {correct_answears} / {total_questions}')

    if total_questions > 0:
        print(f'Sikerességi arány: {correct_answears / total_questions * 100:.2f}%')


def main():
    """ Főprogram """

    fogalom_meghatarozasa_dict = create_dictionary(fogalmak, meghatarozasok)

    correct_answears, total_questions = play_game(fogalom_meghatarozasa_dict)

    display_result(correct_answears, total_questions)


main()