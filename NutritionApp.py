class Baby:
    def __init__(self, name, age_months, weight_kg):
        self.name = name
        self.age_months = age_months
        self.weight_kg = weight_kg
    def display_info(self):
        print(f"\n{'Baby Name:':<15}{self.name}")
        print(f"{'Age:':<15}{self.age_months} months")
        print(f"{'Weight:':<15}{self.weight_kg} kg")

    def is_underweight(self):
        # Simple threshold values for illustration; these could be based on actual guidelines
        age_weight_thresholds = {3: 5.5, 6: 7.5, 9: 8.5, 12: 9.0, 18: 10.5, 24: 11.5}
        threshold = age_weight_thresholds.get(self.age_months, 8.0)  # Default if age not listed
        return self.weight_kg < threshold


class NutritionAdvice:
    def __init__(self, baby):
        self.baby = baby

    def generate_meal_plan(self):
        if self.baby.age_months < 6:
            return "Exclusive breastfeeding is recommended up to 6 months."
        elif 6 <= self.baby.age_months < 12:
            return "Start introducing mashed fruits and vegetables, rice porridge, and lentils."
        elif 12 <= self.baby.age_months < 24:
            return "Include soft foods like rice, beans, yogurt, eggs, and small pieces of soft vegetables."
        else:
            return "Balanced diet including grains, vegetables, fruits, proteins, and dairy."

    def generate_underweight_advice(self):
        return ("Since your baby is underweight, consider adding high-calorie, nutrient-dense foods:\n"
                "1. Mashed avocado for healthy fats.\n"
                "2. Peanut butter (in small amounts) for protein and healthy fats.\n"
                "3. Full-fat yogurt or dairy products.\n"
                "4. Sweet potatoes and oats for additional carbohydrates.\n"
                "5. Consult a pediatrician for specialized advice if possible.")

    def generate_advice(self):
        print("\nNutrition Advice:")
        meal_plan = self.generate_meal_plan()
        print(meal_plan)

        if self.baby.is_underweight():
            print("\nAdditional Advice for Low Weight:")
            print(self.generate_underweight_advice())

        print("\nGeneral Feeding Tips:")
        print("1. Wash hands before preparing food.")
        print("2. Feed the baby small portions several times a day.")
        print("3. Avoid sugary or salty foods.")


# Main execution function
def main():
    print("Welcome to the Nutrition Advice App for New Mothers!")
    name = input("Enter your baby's name: ")
    age_months = int(input("Enter your baby's age in months: "))
    weight_kg = float(input("Enter your baby's weight in kg: "))

    # Create Baby instance
    baby = Baby(name, age_months, weight_kg)
    baby.display_info()

    # Generate and display nutrition advice
    advice = NutritionAdvice(baby)
    advice.generate_advice()


# Run the app
if __name__ == "__main__":
    main()
# bullshit