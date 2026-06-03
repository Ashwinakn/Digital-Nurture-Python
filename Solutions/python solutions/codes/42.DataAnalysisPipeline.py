import statistics

def main():
    # Create the sales.txt file with sample numeric data
    with open('sales.txt', 'w') as f:
        f.write("150.50\n200.75\n350.00\n100.25\n250.00\n")

    try:
        with open('sales.txt', 'r') as f:
            data = [float(line.strip()) for line in f if line.strip()]
        
        if not data:
            print("No data found.")
            return

        mean_val = statistics.mean(data)
        median_val = statistics.median(data)

        print("Statistics Summary:")
        print(f"Mean: {mean_val:.2f}")
        print(f"Median: {median_val:.2f}")
    except FileNotFoundError:
        print("Error: sales.txt not found. Please create it with numeric data.")
    except ValueError:
        print("Error: Invalid numeric data in sales.txt.")

if __name__ == "__main__":
    main()
