def initialize():
    print("Initialize resources...")

def process_data(data):
    return data.upper()

def save_results(results):
    print(f"Saving results: {results}")

def main():
    initialize()
    data = "sample data"
    processed_data = process_data(data)
    save_results(processed_data)

main()

