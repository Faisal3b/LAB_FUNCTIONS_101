def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def main():
    while True:
        user_input = input('Enter a temperature and its unit (e.g., "25 C" or "77 F"): ')

        try:
            temp_str, unit = user_input.split()
            temp_value = float(temp_str)  
            unit = unit.upper()

            if unit == "C":
                converted = celsius_to_fahrenheit(temp_value)
                print(f"Temperature in Fahrenheit: {round(converted, 2)} F")
            elif unit == "F":
                converted = fahrenheit_to_celsius(temp_value)
                print(f"Temperature in Celsius: {round(converted, 2)} C")
            else:
                raise TypeError("Invalid unit")

        except ValueError:
            print("Invalid temperature value. Please enter a valid number.")
        except TypeError:
            print("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")

        print()  # blank line between prompts, matching the example output


main()