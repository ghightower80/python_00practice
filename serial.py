class SerialGenerator:
    def __init__(self, start):
        """
        Start the SerialGenerator with a starting number.

        """
        self.start = start
        self.next_number = start

    def generate(self):
        """
        Generate the next number.

        Returns:
            int: The next number.
        """
        number = self.next_number
        self.next_number += 1
        return number

    def reset(self):
        """
        Reset the number back to the original number.
        """
        self.next_number = self.start


serial = SerialGenerator(start=100)

print(serial.generate())
print(serial.generate())
print(serial.generate())


serial.reset()

print(serial.generate())
