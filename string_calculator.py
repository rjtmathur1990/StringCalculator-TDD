import re

class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0

        if numbers.startswith("//"):
            delimiter, numbers = re.match(r"//(.+)\n(.+)", numbers).groups()
            numbers = numbers.replace(delimiter, ",")

        numbers = numbers.replace("\n", ",")
        num_list = list(map(int, numbers.split(",")))

        negative_numbers = [num for num in num_list if num < 0]
        if negative_numbers:
            raise ValueError(f"negative numbers not allowed: {', '.join(map(str, negative_numbers))}")

        return sum(num_list)

