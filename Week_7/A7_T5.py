from dataclasses import dataclass

DELIMITER = ";"
WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday"]

@dataclass
class Timestamp:
    weekday: str
    hour: str
    consumption: float
    price: float

@dataclass
class DayUsage:
    weekday: str
    total_consumption: float = 0.0
    total_cost: float = 0.0

def read_timestamps(filename: str) -> list[Timestamp]:
    timestamps = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            next(f)  # Ohitetaan otsikkorivi
            for line in f:
                line = line.strip()
                if not line:
                    continue
                columns = line.split(DELIMITER)
                ts = Timestamp(
                    weekday=columns[0],
                    hour=columns[1],
                    consumption=float(columns[2]),
                    price=float(columns[3])
                )
                timestamps.append(ts)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    return timestamps

def analyse_daily_usage(timestamps: list[Timestamp]) -> list[DayUsage]:
    # Alustetaan viikonpäivät
    day_usage_list = [DayUsage(weekday=day) for day in WEEKDAYS]

    # Käydään läpi aikaleimat ja lisätään arvot oikealle päivälle
    for ts in timestamps:
        for day_usage in day_usage_list:
            if day_usage.weekday == ts.weekday:
                day_usage.total_consumption += ts.consumption
                day_usage.total_cost += ts.consumption * ts.price
                break
    return day_usage_list

def print_summary(day_usage_list: list[DayUsage]):
    print("### Electricity consumption summary ###")
    for day_usage in day_usage_list:
        print(f" - {day_usage.weekday} usage {day_usage.total_consumption:.2f} kWh, "
              f"cost {day_usage.total_cost:.2f} €")
    print("### Electricity consumption summary ###")

def main():
    print("Program starting.")
    filename = input("Insert filename: ")
    print(f'Reading file "{filename}".')
    timestamps = read_timestamps(filename)
    if timestamps:
        print("Analysing timestamps.")
        day_usage_list = analyse_daily_usage(timestamps)
        print("Displaying results.")
        print_summary(day_usage_list)
    print("Program ending.")

if __name__ == "__main__":
    main()