import argparse


class LogAnalyzer:
    """
    CLI-based log analyzer to count INFO, WARNING, and ERROR messages.
    """

    def __init__(self, log_file: str, output_file: str, level: str = None):
        self.log_file = log_file
        self.output_file = output_file
        self.level = level
        self.log_lines = []
        self.log_counts = {
            "INFO": 0,
            "WARNING": 0,
            "ERROR": 0
        }

    def read_logs(self) -> bool:
        """
        Read log file safely.
        """
        try:
            with open(self.log_file, "r") as file:
                self.log_lines = file.readlines()

            if not self.log_lines:
                print("❌ Log file is empty.")
                return False

            return True

        except FileNotFoundError:
            print(f"❌ Log file not found: {self.log_file}")
            return False

    def analyze_logs(self) -> None:
        """
        Analyze log lines and count levels.
        """
        for line in self.log_lines:
            for level in self.log_counts:
                if level in line:
                    self.log_counts[level] += 1

        if self.level:
            self.log_counts = {
                self.level: self.log_counts.get(self.level, 0)
            }

    def display_summary(self) -> None:
        """
        Print summary to terminal.
        """
        print("\nLog Summary")
        print("-" * 20)
        for level, count in self.log_counts.items():
            print(f"{level}: {count}")

    def write_summary(self) -> None:
        """
        Write summary to output file.
        """
        with open(self.output_file, "w") as file:
            file.write("Log Summary\n")
            file.write("-" * 20 + "\n")
            for level, count in self.log_counts.items():
                file.write(f"{level}: {count}\n")

    def run(self) -> None:
        """
        Execute the full CLI log analysis.
        """
        if self.read_logs():
            self.analyze_logs()
            self.display_summary()
            self.write_summary()
            print(f"\n✅ Summary written to {self.output_file}")


def parse_arguments():
    """
    Parse command-line arguments.
    """
    parser = argparse.ArgumentParser(
        description="Simple CLI Log Analyzer for DevOps"
    )

    parser.add_argument(
        "--file",
        required=True,
        help="Path to log file"
    )

    parser.add_argument(
        "--out",
        default="log_summary.txt",
        help="Output file path"
    )

    parser.add_argument(
        "--level",
        choices=["INFO", "WARNING", "ERROR"],
        help="Filter log level"
    )

    return parser.parse_args()


def main() -> None:
    args = parse_arguments()

    analyzer = LogAnalyzer(
        log_file=args.file,
        output_file=args.out,
        level=args.level
    )

    analyzer.run()


if __name__ == "__main__":
    main()
