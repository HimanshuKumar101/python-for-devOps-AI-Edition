def read_log_file(file_path: str) -> list:
    """
    Reads the log file and returns log lines.
    """
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()

            if not lines:
                raise ValueError("Log file is empty.")

            return lines

    except FileNotFoundError:
        print("❌ Error: Log file not found.")
        return []
    except ValueError as error:
        print("❌ Error:", error)
        return []


def analyze_logs(log_lines: list) -> dict:
    """
    Analyze log lines and count log levels.
    """
    log_counts = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0
    }

    for line in log_lines:
        for level in log_counts:
            if level in line:
                log_counts[level] += 1

    return log_counts


def write_summary(summary: dict, output_file: str) -> None:
    """
    Write log summary to an output file.
    """
    with open(output_file, "w") as file:
        file.write("Log Summary\n")
        file.write("-" * 20 + "\n")
        for level, count in summary.items():
            file.write(f"{level}: {count}\n")


def main() -> None:
    log_file = "app.log"
    output_file = "log_summary.txt"

    log_lines = read_log_file(log_file)

    if not log_lines:
        return

    summary = analyze_logs(log_lines)

    print("\nLog Summary")
    print("-" * 20)
    for level, count in summary.items():
        print(f"{level}: {count}")

    write_summary(summary, output_file)
    print("\n✅ Summary written to log_summary.txt")


if __name__ == "__main__":
    main()
