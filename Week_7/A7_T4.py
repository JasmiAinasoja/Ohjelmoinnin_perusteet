from dataclasses import dataclass

DELIMITER = ";"

@dataclass
class Timestamp:
    weekday: str
    hour: str
    consumption: float
    price: float

def read_timestamps(filename: str) -> list[Timestamp]:
    timestamps = []
    with open(filename, "r", encoding="utf-8") as f:
        next(f)
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
    return timestamps

def print_usage(timestamps: list[Timestamp]):
    print("Electricity usage:")
    total_consumption = 0.0
    total_cost = 0.0
    for ts in timestamps:
        cost = ts.consumption * ts.price
        total_consumption += ts.consumption
        total_cost += cost
        print(f" - {ts.weekday} {ts.hour}:00, price {ts.price:.2f}, consumption {ts.consumption:.2f} kWh, total {cost:.2f} €")


def main():
    print("Program starting.")
    filename = input("Insert filename: ")
    print(f'Reading file "{filename}".')
    timestamps = read_timestamps(filename)
    if timestamps:
        print_usage(timestamps)
    print("Program ending.")

if __name__ == "__main__":
    main()