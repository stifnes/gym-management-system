from datetime import date
customers = []
trainers = []
equipments = []
exercise_plans = []
subscriptions = []



class Subscription:
    def __init__(self, customer, trainer, exercise_plan, start_date, end_date):
        self.customer = customer
        self.trainer = trainer
        self.exercise_plan = exercise_plan
        self.start_date = start_date
        self.end_date = end_date

    def __str__(self):
        return f"Subscription from {self.start_date} to {self.end_date} for {self.customer.name} with trainer {self.trainer.name}"


class Customer:
    def __init__(self, name, password, age, email, phone, address):
        self.name = name
        self.password = password
        self.age = age
        self.email = email
        self.phone = phone
        self.address = address

    @staticmethod
    def create_customer():
        name = input("Enter customer name: ")
        password = input("Enter password: ")
        age = input("Enter age: ")
        email = input("Enter email: ")
        phone = input("Enter phone number: ")
        address = input("Enter address: ")
        with open('customers.txt', 'a') as f:
            f.write(f"{name},{password},{age},{email},{phone},{address}\n")
        print(f"Customer {name} created successfully.")

    @staticmethod
    def remove_customer(name):
        with open('customers.txt', 'r') as f:
            lines = f.readlines()
        with open('customers.txt', 'w') as f:
            found = False
            for line in lines:
                if line.startswith(name + ','):
                    found = True
                else:
                    f.write(line)
            if found:
                print(f"Customer {name} removed successfully.")
            else:
                print(f"Customer {name} not found.")

    def create_subscription(self, trainer, exercise_plan, start_date, end_date):
        if not isinstance(trainer, Trainer):
            raise ValueError("trainer must be a Trainer object")
        if not isinstance(exercise_plan, ExercisePlan):
            raise ValueError("exercise_plan must be an ExercisePlan object")
        if not isinstance(start_date, str) or not isinstance(end_date, str):
            raise ValueError("start_date and end_date must be strings")

        try:
            subscription = Subscription(self, trainer, exercise_plan, start_date, end_date)
            subscriptions.append(subscription)
            self.update_subscription_file()
            print('Subscription created successfully')
        except Exception as e:
            print(f"Error creating subscription: {e}")

    def read_subscriptions(self):
        if not subscriptions:
            print("No subscriptions found.")
        else:
            for subscription in subscriptions:
                print(subscription)

    def update_subscription(self, subscription_index, trainer=None, exercise_plan=None, start_date=None, end_date=None):
        if not isinstance(subscription_index, int):
            raise ValueError("subscription_index must be an integer")
        if subscription_index < 0 or subscription_index >= len(subscriptions):
            raise ValueError(f"subscription_index out of range (0-{len(subscriptions) - 1})")

        subscription = subscriptions[subscription_index]
        if trainer and not isinstance(trainer, Trainer):
            raise ValueError("trainer must be a Trainer object")
        if exercise_plan and not isinstance(exercise_plan, ExercisePlan):
            raise ValueError("exercise_plan must be an ExercisePlan object")
        if start_date and not isinstance(start_date, str):
            raise ValueError("start_date must be a string")
        if end_date and not isinstance(end_date, str):
            raise ValueError("end_date must be a string")

        try:
            if trainer:
                subscription.trainer = trainer
            if exercise_plan:
                subscription.exercise_plan = exercise_plan
            if start_date:
                subscription.start_date = start_date
            if end_date:
                subscription.end_date = end_date
            self.update_subscription_file()
        except Exception as e:
            print(f"Error updating subscription: {e}")

    def delete_subscription(self, subscription_index):
        if not isinstance(subscription_index, int):
            raise ValueError("subscription_index must be an integer")
        if subscription_index < 0 or subscription_index >= len(subscriptions):
            raise ValueError(f"subscription_index out of range (0-{len(subscriptions) - 1})")

        try:
            del subscriptions[subscription_index]
            self.update_subscription_file()
            print("Subscription Deleted Successfully")
        except Exception as e:
            print(f"Error deleting subscription: {e}")

    def update_subscription_file(self):
        try:
            with open('subscriptions.txt', "w") as f:
                for subscription in subscriptions:
                    f.write(
                        f"{subscription.customer.name},{subscription.trainer.name},{subscription.exercise_plan},{subscription.start_date},{subscription.end_date}\n")
        except Exception as e:
            print(f"Error updating subscription file: {e}")

def customer_login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    with open('customers.txt', 'r') as f:
        for line in f:
            name, pwd, age, email, phone, address = line.strip().split(',')
            if name == username and pwd == password:
                print("Login successful as " + name)
                customer = Customer(name, pwd, age, email, phone, address)
                # do something with the customer object
                customer_menu(customer)
                return
            else:
                print("Incorrect username or password.")
        else:
            print("Account does not exist. Create an account first")
            main()


def trainer_login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    for trainer in trainers:
        if trainer.name == username and trainer.password == password:
            print("Login successful as " + trainer.name)
            # trainer = Trainer(name, pwd, age, specialization)
            # do something with the trainer object
            trainer_menu(trainer)
            return trainer
        else:
            print("Incorrect username or password.")
    # with open('trainers.txt', 'r') as f:
    #     for line in f:
    #         name, pwd, age, specialization = line.strip().split(',')
    #         if name == username and pwd == password:
    #             print("Login successful as a trainer.")
    #             trainer = Trainer(name, pwd, age, specialization)
    #             # do something with the trainer object
    #             return
    # print("Incorrect username or password.")


def customer_menu(customer):
    print("Customer Menu:")
    print("1. View subscriptions")
    print("2. Create new subscription")
    print("3. Update subscription")
    print("4. Delete subscription")
    print("5. Delete account")
    print("6. Logout")
    choice = input("Enter choice (1-7): ")
    if choice == "1":
        # print out the customer's subscriptions
        customer.read_subscriptions()
    elif choice == "2":
        # create a new subscription for the customer
        trainer_name = input('Please enter the name of the trainer')

        # check if trainer exists
        def checkTrainer():
            for trainer in trainers:
                if trainer.name == trainer_name:
                    print("Trainer" + trainer.name + " exists")
                    # trainer = Trainer(name, pwd, age, specialization)
                    # do something with the trainer object
                    return trainer
                else:
                    print("Trainer does not exists. Create a new trainer")
                    main()
                    return

        trainer1 = checkTrainer()
        equipment1 = Equipment('bench', 'working')
        exercise_plan1 = ExercisePlan(trainer1, equipment1, 30)
        customer.create_subscription(trainer1, exercise_plan1, "2023-05-14", "2023-06-14")
    elif choice == "3":
        # update the first subscription's trainer and duration
        trainer2 = Trainer("Bob Johnson", "Certified Personal Trainer")
        equipment2 = Equipment('bench', 'working')
        exercise_plan2 = ExercisePlan("Cardio", trainer2, equipment2, 30)
        customer.update_subscription(0, trainer=trainer2, exercise_plan=exercise_plan2)
    elif choice == "4":
        # delete the second subscription
        subscription_index = int(
            input('Please enter the number of the subscription to be deleted.e.g Enter 1 for first subscription'))
        customer.delete_subscription(subscription_index - 1)
    elif choice == "5":
        customer.remove_customer(customer.name)
    elif choice == "6":
        customer.update_subscription_file()
        return
    else:
        print("Invalid choice. Please try again.")

class Trainer:
    def __init__(self, name, password, age, specialization):
        self.name = name
        self.password = password
        self.age = age
        self.specialization = specialization
        self.exercise_plans = []

    @staticmethod
    def create_trainer():
        name = input("Enter trainer name: ")
        password = input("Enter password: ")
        age = input("Enter age: ")
        specialization = input("Enter specialization: ")
        with open('trainers.txt', 'a') as f:
            f.write(f"{name},{password},{age},{specialization}\n")
        print(f"Trainer {name} created successfully.")


    def create_exercise_plan(self, plan_name, equipment, duration):
        exercise_plan = ExercisePlan(self, plan_name, equipment, duration)
        with open('exercisePlans.txt', 'a') as f:
            f.write(f"{self.name},{plan_name},{equipment},{duration}\n")
        return exercise_plan

    def read_exercise_plans(self):
        with open('exercisePlans.txt', 'r') as f:
            for line in f:
                fields = line.strip().split(', ')
                if fields[0] == self.name:
                    plan_name = fields[1]
                    # equipment = Equipment(fields[2], fields[3])
                    # duration = int(fields[4])
                    # exercise_plan = ExercisePlan(self.name, plan_name, equipment, duration)
                    # exercise_plans.append(exercise_plan)
            return plan_name

    def update_exercise_plan(self, old_plan, new_equipment, new_duration):
        exercise_plans = self.read_exercise_plans()
        if old_plan not in exercise_plans:
            raise ValueError(f"{self.name} does not have an exercise plan with the given details.")
        for exercise_plan in exercise_plans:
            if exercise_plan == old_plan:
                exercise_plan.equipment = new_equipment
                exercise_plan.duration = new_duration
        with open('exercisePlans.txt', 'w') as f:
            for exercise_plan in exercise_plans:
                f.write(f"{self.name}, {exercise_plan.equipment.name}, {exercise_plan.duration}\n")

    def delete_exercise_plan(self, exercise_plan_name):
        # exercise_plans = self.read_exercise_plans()
        for plan in exercise_plans:
            print(plan.plan_name)
            print(plan.trainer)
        if exercise_plan_name not in exercise_plans:
            raise ValueError(f"{self.name} does not have an exercise plan with the given details.")
        exercise_plans.remove(exercise_plan_name)
        with open('exercisePlans.txt', 'w') as f:
            for exercise_plan in exercise_plans:
                f.write(f"{self.name},{exercise_plan_name}, {exercise_plan.equipment.name}, {exercise_plan.duration}\n")

    def write_exercise_plans_to_file(self):
        with open('exercisePlans.txt', 'w') as f:
            for plan in self.exercise_plans:
                f.write(f"{self.name},{plan.equipment.name},{plan.duration}\n")

class Equipment:
    def __init__(self, name, status):
        self.name = name
        self.status = status

    @staticmethod
    def add_equipment():
        name = input("Enter equipment name: ")
        status = input("Enter equipment status (working/not-working): ")
        with open('equipment.txt', 'a') as f:
            f.write(f"{name},{status}\n")
        print(f"Equipment {name} added successfully.")

    @staticmethod
    def remove_equipment(name):
        with open('equipment.txt', 'r') as f:
            lines = f.readlines()
        with open('equipment.txt', 'w') as f:
            found = False
            for line in lines:
                if line.startswith(name + ','):
                    found = True
                else:
                    f.write(line)
            if found:
                print(f"Equipment {name} removed successfully.")
            else:
                print(f"Equipment {name} not found.")

class ExercisePlan:
    def __init__(self,trainer, plan_name, equipment, duration):
        self.trainer = trainer
        self.plan_name = plan_name
        self.equipment = equipment
        self.duration = duration

    def get_trainer(self):
        return self.trainer

    def get_equipment(self):
        return self.equipment

    def get_duration(self):
        return self.duration

    def write_to_file(self):
        with open('exercisePlans.txt', 'a') as f:
            f.write(f"{self.trainer.name},{self.plan_name},{self.equipment.name},{self.duration}\n")

def trainer_menu(trainer):
    print("Trainer Menu:")
    print("1. View exercise plans")
    print("2. Create new exercise plans")
    print("3. Update exercise plans")
    print("4. Delete exercise plans")
    print("5. Delete account")
    print("6. Logout")
    choice = input("Enter choice (1-7): ")
    if choice == "1":
        # print out the customer's subscriptions
        print(trainer.read_exercise_plans())
        # for plan in allplans:
        #     print("Plan name: " + plan[1])
    elif choice == "2":
        # create a new exercise plan for the trainer
        plan_name = input("please enter the name of the plan: ")
        duration = int(input('please enter the duration of the plan: '))
        equipment1 = Equipment('bench', 'working')
        print(trainer.name, plan_name, equipment1.name, duration)
        trainer.create_exercise_plan(plan_name, equipment1.name, duration)
    elif choice == "3":
        # update the first subscription's trainer and duration
        trainer2 = Trainer("Bob Johnson", "Certified Personal Trainer")
        equipment2 = Equipment('bench', 'working')
        exercise_plan2 = ExercisePlan("Cardio", trainer2, equipment2, 30)
        trainer.update_subscription(0, trainer=trainer2, exercise_plan=exercise_plan2)
    elif choice == "4":
        # delete an exercise plan
        plan_name = input('Please enter the name of the plan to be deleted: ')
        trainer.delete_exercise_plan(plan_name)
    elif choice == "5":
        trainer.remove_trainer(trainer.name)
    elif choice == "6":
        trainer.update_subscription_file()
        return
    else:
        print("Invalid choice. Please try again.")


with open("trainers.txt", "r") as file:
    for line in file:
        data = line.strip().split(",")
        trainer = Trainer(data[0], data[1], data[2], data[3])
        trainers.append(trainer)

with open("subscriptions.txt", "r") as file:
    for line in file:
        data = line.strip().split(",")
        subscription = Subscription(data[0], data[1], data[2], data[3],data[3])
        subscriptions.append(subscription)

with open("exercisePlans.txt", "r") as file:
    for line in file:
        data = line.strip().split(",")
        exercise_plan = ExercisePlan(data[0], data[1], data[2], data[3])
        exercise_plans.append(exercise_plan)


# main program
def main():

    while True:
        print("1. Customer Login")
        print("2. Trainer Login")
        print("3. Create Customer Account")
        print("4. Create Trainer Account")
        print("5. Delete Customer Account")
        print("6. Add Equipment")
        print("7. Delete Equipment")
        choice = int(input("Enter your choice (1-4): "))
        if choice == 1:
            customer_login()
            break
        elif choice == 2:
            trainer_login()
            break
        elif choice == 3:
            Customer.create_customer()
        elif choice == 4:
            Trainer.create_trainer()
        elif choice == 5:
            name = input("Enter the name of the customer to delete")
            Customer.remove_customer(name)
        elif choice == 6:
            Equipment.add_equipment()
        elif choice == 7:
            name = input("Enter the name of the equipment to delete")
            Equipment.remove_equipment(name)
        else:
            print("Invalid choice. Please try again.")


main()
