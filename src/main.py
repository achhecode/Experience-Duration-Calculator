from calculator import ExperienceCalculator

def main():
    calculator = ExperienceCalculator("../data/experience.json")
    years, months = calculator.calculate_total_experience()

    print(f"Total Experience: {years} years and {months} months")

if __name__ == "__main__":
    main()
