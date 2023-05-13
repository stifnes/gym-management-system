class Customers:
    def __init__(self, id, name, email, password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Email: {self.email}"
    
class Trainers:
    def __init__(self, id, name, email, password, specialty):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.specialty = specialty

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Email: {self.email}, Specialty: {self.specialty}"


class Equipment:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}"


class ExercisePlan:
    def __init__(self, id, trainer_id, equipment_id, duration):
        self.id = id
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration

    def __str__(self):
        return f"ID: {self.id}, Trainer ID: {self.trainer_id}, Equipment ID: {self.equipment_id}, Duration: {self.duration} minutes"


class Subscriptions:
    def __init__(self, id, customer_id, trainer_id, exercise_plan_id, start_date, end_date):
        self.id = id
        self.customer_id = customer_id
        self.trainer_id = trainer_id
        self.exercise_plan_id = exercise_plan_id
        self.start_date = start_date
        self.end_date = end_date

    def __str__(self):
        return f"ID: {self.id}, Customer ID: {self.customer_id}, Trainer ID: {self.trainer_id}, Exercise Plan ID: {self.exercise_plan_id}, Start Date: {self.start_date}, End Date: {self.end_date}"

def read_customers():
    customers = []
    with open("customers.txt", "r") as file:
        for line in file:
            data = line.strip().split(", ")
            customer = Customers(int(data[0]), data[1], data[2], data[3])
            customers.append(customer)
    return customers


def read_trainers():
    trainers = []
    with open("trainers.txt", "r") as file:
        for line in file:
            data = line.strip().split(", ")
            trainer = Trainers(int(data[0]), data[1], data[2], data[3], data[4])
            trainers.append(trainer)
    return trainers


def read_equipments():
    equipments = []
    with open("equipments.txt", "r") as file:
        for line in file:
            data = line.strip().split(", ")
            equipment = Equipment(int(data[0]), data[1])
            equipments.append(equipment)
    return equipments


def read_exercise_plans():
    exercise_plans = []
    with open("exercisePlans.txt", "r") as file:
        for line in file:
            data = line.strip().split(", ")
            exercise_plan = ExercisePlan(int(data[0]), int(data[1]), int(data[2]), int(data[3]))
            exercise_plans.append(exercise_plan)
    return exercise_plans


def read_subscriptions():
    subscriptions = []
    with open("subscriptions.txt", "r") as file:
        for line in file:
            data = line.strip().split(", ")
            subscription = Subscriptions(int(data[0]), int(data[1]), int(data[2]), int(data[3]), data[4], data[5])
            subscriptions.append(subscription)
    return subscriptions


def create_customer():
    id = input("Enter customer ID: ")
    name = input("Enter customer name: ")
    email = input("Enter customer email: ")
    password = input("Enter customer password: ")
    customer = Customers(int(id), name, email, password)
    customers.append(customer)
    with open("customers.txt", "a") as file:
        file.write(f"\n{id}, {name}, {email}, {password}")
    print("Customer account created successfully.")


def create_trainer():
    id = input("Enter trainer ID: ")
    name = input("Enter trainer name: ")
    email = input("Enter trainer email: ")
    password = input("Enter trainer password: ")
    specialty = input("Enter trainer specialty: ")
    trainer = Trainers
    (int(id), name, email, password, specialty)
    trainers.append(trainer)
    with open("trainers.txt", "a") as file:
        file.write(f"\n{id}, {name}, {email}, {password}, {specialty}")
    print("Trainer account created successfully.")


def create_equipment():
    id = input("Enter equipment ID: ")
    name = input("Enter equipment name: ")
    equipment = Equipment(int(id), name)
    equipments.append(equipment)
    with open("equipments.txt", "a") as file:
        file.write(f"\n{id}, {name}")
    print("Equipment added successfully.")


def create_exercise_plan():
    id = input("Enter exercise plan ID: ")
    trainer_id = input("Enter trainer ID: ")
    equipment_id = input("Enter equipment ID: ")
    duration = input("Enter exercise duration (in minutes): ")
    exercise_plan = ExercisePlan(int(id), int(trainer_id), int(equipment_id), int(duration))
    exercise_plans.append(exercise_plan)
    with open("exercisePlans.txt", "a") as file:
        file.write(f"\n{id}, {trainer_id}, {equipment_id}, {duration}")
    print("Exercise plan created successfully.")


def create_subscription():
    id = input("Enter subscription ID: ")
    customer_id = input("Enter customer ID: ")
    trainer_id = input("Enter trainer ID: ")
    exercise_plan_id = input("Enter exercise plan ID: ")
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    subscription = Subscriptions(int(id), int(customer_id), int(trainer_id), int(exercise_plan_id), start_date, end_date)
    subscriptions.append(subscription)
    with open("subscriptions.txt", "a") as file:
        file.write(f"\n{id}, {customer_id}, {trainer_id}, {exercise_plan_id}, {start_date}, {end_date}")
    print("Subscription created successfully.")


def display_customers():
    for customer in customers:
        print(customer)


def display_trainers():
    for trainer in trainers:
        print(trainer)


def display_equipments():
    for equipment in equipments:
        print(equipment)


def display_exercise_plans():
    for exercise_plan in exercise_plans:
        print(exercise_plan)
def display_subscriptions():
    for subscription in subscriptions:
        print(subscription)


def main():
    global customers, trainers, equipments, exercise_plans, subscriptions
    customers = read_customers()
    trainers = read_trainers()
    equipments = read_equipments()
    exercise_plans = read_exercise_plans()
    subscriptions = read_subscriptions()

    while True:
        print("\nWelcome to the GYM management system!")
        print("1. Create customer account")
        print("2. Create trainer account")
        print("3. Add equipment")
        print("4. Create exercise plan")
        print("5. Create subscription")
        print("6. Display customers")
        print("7. Display trainers")
        print("8. Display equipments")
        print("9. Display exercise plans")
        print("10. Display subscriptions")
        print("11. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_customer()
        elif choice == "2":
            create_trainer()
        elif choice == "3":
            create_equipment()
        elif choice == "4":
            create_exercise_plan()
        elif choice == "5":
            create_subscription()
        elif choice == "6":
            display_customers()
        elif choice == "7":
            display_trainers()
        elif choice == "8":
            display_equipments()
        elif choice == "9":
            display_exercise_plans()
        elif choice == "10":
            display_subscriptions()
        elif choice == "11":
            print("Thank you for using the GYM management system!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

        
