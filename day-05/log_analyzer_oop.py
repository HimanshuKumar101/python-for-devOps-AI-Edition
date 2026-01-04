class LogAnalyzer:
    """
    A simple log analyzer to count INFO, WARNING, and ERROR messages.
    """

    def __init__(self, log_file: str, output_file: str) -> None:
        self.log_file = log_file
        self.output_file = output_file
        self.log_lines = []
        self.log_counts = {
            "INFO": 0,
            "WARNING": 0,
            "ERROR": 0
        }

    def read_logs(self) -> bool:
        """
        Read log file contents.
        """
        try:
            with open(self.log_file, "r") as file:
                self.log_lines = file.readlines()

            if not self.log_lines:
                print("❌ Log file is empty.")
                return False

            return True

        except FileNotFoundError:
            print("❌ Log file not found.")
            return False

    def analyze_logs(self) -> None:
        """
        Analyze log lines and count log levels.
        """
        for line in self.log_lines:
            for level in self.log_counts:
                if level in line:
                    self.log_counts[level] += 1

    def write_summary(self) -> None:
        """
        Write analysis summary to output file.
        """
        with open(self.output_file, "w") as file:
            file.write("Log Summary\n")
            file.write("-" * 20 + "\n")
            for level, count in self.log_counts.items():
                file.write(f"{level}: {count}\n")

    def display_summary(self) -> None:
        """
        Print summary to terminal.
        """
        print("\nLog Summary")
        print("-" * 20)
        for level, count in self.log_counts.items():
            print(f"{level}: {count}")

    def run(self) -> None:
        """
        Execute full log analysis process.
        """
        if self.read_logs():
            self.analyze_logs()
            self.display_summary()
            self.write_summary()
            print("\n✅ Summary written to", self.output_file)


def main() -> None:
    analyzer = LogAnalyzer(
        log_file="app.log",
        output_file="log_summary.txt"
    )
    analyzer.run()


if __name__ == "__main__":
    main()
