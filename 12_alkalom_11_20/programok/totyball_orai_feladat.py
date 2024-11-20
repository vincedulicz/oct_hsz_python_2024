import json
from typing import List, Dict, Union


def load_json(filename: str) -> Union[Dict, List]:
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from '{filename}'.")
        return {}


def save_json(data: Union[Dict, List], filename: str) -> None:
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Data saved to {filename}")
    except IOError as e:
        print(f"Error: Unable to save file '{filename}'. {e}")


def filter_invalid_matches(matches: List[Dict]) -> List[Dict]:
    valid_matches = []
    invalid_matches = []

    for match in matches:
        try:
            if "ht" not in match["score"]:
                raise KeyError(f"Missing 'ht' in match: {match}")
            valid_matches.append(match)
        except KeyError:
            invalid_matches.append(match)

    if invalid_matches:
        save_json({"invalid_matches": invalid_matches}, "hibas.json")
        print(f"{len(invalid_matches)} invalid matches saved to 'hibas.json'.")
    return valid_matches


def home_losing_at_halftime_but_wins(matches: List[Dict]) -> List[Dict]:
    results = []
    for match in matches:
        try:
            ht_home, ht_away = match["score"]["ht"]
            ft_home, ft_away = match["score"]["ft"]
            if ht_home < ht_away and ft_home > ft_away:
                results.append(match)
        except KeyError as e:
            print(f"Error processing match: {match}. Missing key: {e}")
    return results


def home_losing_at_halftime_but_draws(matches: List[Dict]) -> List[Dict]:
    results = []
    for match in matches:
        try:
            ht_home, ht_away = match["score"]["ht"]
            ft_home, ft_away = match["score"]["ft"]
            if ht_home < ht_away and ft_home == ft_away:
                results.append(match)
        except KeyError as e:
            print(f"Error processing match: {match}. Missing key: {e}")
    return results


def home_concedes_more_than_three_goals(matches: List[Dict]) -> List[Dict]:
    results = []
    for match in matches:
        try:
            _, ft_away = match["score"]["ft"]
            if ft_away > 3:
                results.append(match)
        except KeyError as e:
            print(f"Error processing match: {match}. Missing key: {e}")
    return results


def home_scores_more_than_three_goals(matches: List[Dict]) -> List[Dict]:
    results = []
    for match in matches:
        try:
            ft_home, _ = match["score"]["ft"]
            if ft_home > 3:
                results.append(match)
        except KeyError as e:
            print(f"Error processing match: {match}. Missing key: {e}")
    return results


def filter_by_matchday(matches: List[Dict], matchday: str) -> List[Dict]:
    try:
        results = [
            match for match in matches if match["round"].lower() == f"matchday {matchday}".lower()
        ]
        return results
    except KeyError as e:
        print(f"Error filtering by matchday: {e}")
        return []


def filter_by_date(matches: List[Dict], date: str) -> List[Dict]:
    try:
        results = [match for match in matches if match["date"] == date]
        return results
    except KeyError as e:
        print(f"Error filtering by date: {e}")
        return []


def print_results(title: str, matches: List[Dict]) -> None:
    print(title)
    for match in matches:
        print(f"{match['round']}: {match['team1']} vs {match['team2']}, "
              f"Date: {match['date']}, HT: {match['score'].get('ht', 'N/A')}, FT: {match['score'].get('ft', 'N/A')}")
    print("-" * 50)


def main() -> None:
    filename = "adatok/data.json"
    data = load_json(filename)
    matches = data.get("matches", [])

    matches = filter_invalid_matches(matches)

    while True:
        options = [
            "1. Search by Matchday",
            "2. Search by Date",
            "3. Analyze all matches",
            "Kilépés: q/end/quit"
        ]

        print(f"Options: {[option for option in options]}")

        choice = input("Choose an option (1/2/3/q): ")

        if choice == "1":
            matchday = input("Enter Matchday (1-9): ")
            filtered_matches = filter_by_matchday(matches, matchday)
        elif choice == "2":
            date = input("Enter Date (YYYY-MM-DD): ")
            filtered_matches = filter_by_date(matches, date)
        elif choice.lower() in ["end", "q", "quit"]:
            break
        else:
            filtered_matches = matches

        halftime_loss_to_win = home_losing_at_halftime_but_wins(filtered_matches)
        halftime_loss_to_draw = home_losing_at_halftime_but_draws(filtered_matches)
        home_concedes_3_or_more = home_concedes_more_than_three_goals(filtered_matches)
        home_scores_3_or_more = home_scores_more_than_three_goals(filtered_matches)

        print_results("1) Hazai félidőben vereségre áll, de fordít", halftime_loss_to_win)
        print_results("2) Hazai félidőben vereségre áll, de döntetlen lesz", halftime_loss_to_draw)
        print_results("3) Hazai 3 gólnál többet kap", home_concedes_3_or_more)
        print_results("4) Hazai 3 gólnál többet rúg", home_scores_3_or_more)


main()
