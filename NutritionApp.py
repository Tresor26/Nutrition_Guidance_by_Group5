import mysql.connector
from mysql.connector import Error

class BabyNutritionAdvisor:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Tresor@26",
                database="nutrition_app",
                port=3307
            )
            self.cursor = self.conn.cursor()
            print("Database connection established.")
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
            self.conn = None
            self.cursor = None

        # Recommended weight ranges for babies (in kg) based on age in months
        self.weight_guide = {
            1: (3.2, 4.2),
            2: (4.2, 5.4),
            3: (5.0, 6.5),
            4: (5.6, 7.3),
            5: (6.0, 7.8),
            6: (6.4, 8.2),
            7: (6.7, 8.5),
            8: (6.9, 8.8),
            9: (7.1, 9.0),
            10: (7.4, 9.2),
            11: (7.6, 9.4),
            12: (7.8, 9.5),
            13: (8.0, 9.7),
            14: (8.2, 9.9),
            15: (8.4, 10.2),
            16: (8.6, 10.4),
            17: (8.8, 10.6),
            18: (9.0, 10.8),
            19: (9.2, 11.0),
            20: (9.4, 11.2),
            21: (9.6, 11.4),
            22: (9.8, 11.6),
            23: (10.0, 11.8),
            24: (10.2, 12.0),
            25: (10.4, 12.2),
            26: (10.6, 12.4),
            27: (10.8, 12.6),
            28: (11.0, 12.8),
            29: (11.2, 13.0),
            30: (11.4, 13.2),
            31: (11.6, 13.4),
            32: (11.8, 13.6),
            33: (12.0, 13.8),
            34: (12.2, 14.0),
            35: (12.4, 14.2),
            36: (12.6, 14.4),
            37: (12.8, 14.6),
            38: (13.0, 14.8),
            39: (13.2, 15.0),
            40: (13.4, 15.2),
            41: (13.6, 15.4),
            42: (13.8, 15.6),
            43: (14.0, 15.8),
            44: (14.2, 16.0),
            45: (14.4, 16.2),
            46: (14.6, 16.4),
            47: (14.8, 16.6),
            48: (15.0, 16.8)
        }

        # Recommended sleep hours for babies (in hours per day)
        self.sleep_guide = {
            "0-3 months": 15,
            "4-11 months": 14,
            "12-24 months": 12,
            "25-48 months": 10
        }

        # Vaccine schedule by age (in months)
        self.vaccine_guide = {
            1: ["BCG", "Hepatitis B"],
            2: ["Polio", "Tetanus", "Rotavirus(Dose 1 of 3)"],
            4: ["Polio(IPV)", "H. influenzae type b (Hib)", "Pneumococcal", "Rotavirus(Dose 2 of 3)"],
            6: ["Influenza (flu)", "Coronavirus disease 2019 (COVID-19)", "Rotavirus(Dose 3 of 3)"],
            9: ["Chicken Pox(Varicela) Dose 1"],
            12: ["Measles, mumps, rubella (MMR)"],
            18: ["Vitamin A", "Deworming", "Hepatitis A (HepA)"],
        }

    def get_sleep_recommendation(self, age_months):
        if 0 <= age_months <= 3:
            return self.sleep_guide["0-3 months"]
        elif 4 <= age_months <= 11:
            return self.sleep_guide["4-11 months"]
        elif 12 <= age_months <= 24:
            return self.sleep_guide["12-24 months"]
        elif 25 <= age_months <= 48:
            return self.sleep_guide["25-48 months"]
        else:
            return "Age out of range for recommendation."

    def get_weight_range(self, age_months):
        return self.weight_guide.get(age_months, "No data for this age.")

    def get_vaccine_recommendation(self, age_months):
        applicable_vaccines = [vaccine for age, vaccine in self.vaccine_guide.items() if age <= age_months]
        return applicable_vaccines[-1] if applicable_vaccines else "No vaccines available for this age."

    def give_advice(self, name, age_months, weight, sleep_hours):
        advice_list = []
        # Weight advice
        weight_range = self.get_weight_range(age_months)
        if weight_range == "No data for this age.":
            advice_list.append("We don't have weight data for this age group.")
        elif weight < weight_range[0]:
            advice_list.append(
                f"Weight Alert: {name}'s weight ({weight}kg) is below the recommended range ({weight_range[0]}kg - {weight_range[1]}kg). "
                "\nAdd more protein and high-calorie meals, such as mashed sweet potatoes, avocados, and banana porridge."
            )
        elif weight > weight_range[1]:
            advice_list.append(
                f"Weight Alert: {name}'s weight ({weight}kg) is above the recommended range ({weight_range[0]}kg - {weight_range[1]}kg). ""\nConsult a pediatrician for a detailed assessment."
            )
        else:
            advice_list.append(f"Weight: {name}'s weight ({weight}kg) is within the healthy range.")

        # Sleep advice
        recommended_sleep = self.get_sleep_recommendation(age_months)
        if isinstance(recommended_sleep, int):
            if sleep_hours < recommended_sleep:
                advice_list.append(
                    f"Sleep Alert: {name} is sleeping {sleep_hours} hours, below the recommended {recommended_sleep} hours. "
                    "\nCreate a consistent bedtime routine, limit distractions, and ensure the baby has a comfortable sleeping environment."
                )
            else:
                advice_list.append(f"Sleep: {name} is getting enough sleep ({sleep_hours} hours).")
        else:
            advice_list.append(recommended_sleep)

        # Vaccine advice
        vaccines_due = self.get_vaccine_recommendation(age_months)
        advice_list.append(
            f"Vaccines: By {age_months} months, {name} should have received: {', '.join(vaccines_due)}.")

        # General advice
        advice_list.append(f"\n=== Meal Plan Advice for {name} ===\n")
        advice_list.append("Ensure the baby is hydrated throughout the day.")
        advice_list.append("Introduce a variety of fruits and vegetables gradually.")
        advice_list.append("Avoid processed foods or foods with added sugar or salt.")
        advice_list.append("Engage in play and tummy time to promote development.")
        advice_list.append("Keep Up with medical check-Ups,vaccinations")

        advice_text = "\n".join(advice_list)
        print(f"\n=== Advice for {name} ===\n{advice_text}")
        return advice_text

    def save_to_database(self, name, age_months, weight, sleep_hours, advice):
        query = """
        INSERT INTO baby_profiles (name, age_months, weight, sleep_hours, advice)
        VALUES (%s, %s, %s, %s, %s)
        """
        self.cursor.execute(query, (name, age_months, weight, sleep_hours, advice))
        self.conn.commit()
        print(f"Profile for {name} saved to the database.")

    def close_connection(self):
        if self.conn:
            self.cursor.close()
            self.conn.close()
            print("Database connection closed.")


def main():
    advisor = BabyNutritionAdvisor()

    while True:
        print ("  ----  VIDA BITE   ----  ")
        print("\n=== Baby Nutrition Tracker ===")
        name = input("please, Enter Baby's Name: ")
        age_months = int(input("please, Enter Baby's Age (in Months): "))
        weight = float(input("please, Enter Baby's Weight (in kg): "))
        sleep_hours = float(input("please, Enter Baby's Daily Sleep Hours: "))

        # Generate advice
        advice = advisor.give_advice(name, age_months, weight, sleep_hours)

        # Save to database
        advisor.save_to_database(name, age_months, weight, sleep_hours, advice)

        # Continue or exit
        cont = input("\nWould you like to add another baby? (yes/no): ").strip().lower()
        if cont != "yes":
            print("Thank you for using the Baby Nutrition Tracker!")
            break

    advisor.close_connection()


if __name__ == "__main__":
    main()





