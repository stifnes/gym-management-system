import json

class Customer:
    last_customer_id = 0
    def __init__(self, name, password, age, gender, email, address):
        self.customer_id = Customer.last_customer_id + 1
        Customer.last_customer_id += 1
        self.name = name
        self.password = password
        self.age = age
        self.gender = gender
        self.email = email
        self.address = address
        self.subscriptions = []

    def create(self):
        with open('customers.json', 'r') as f:
            data = json.load(f)

        data.append({
            'customer_id': self.customer_id,
            'name': self.name,
            'password': self.password,
            'age': self.age,
            'gender': self.gender,
            'email': self.email,
            'address': self.address,
            'subscriptions': self.subscriptions
        })
        with open('customers.json', 'w') as f:
            json.dump(data, f)
            print('Customer Created Successfully')

    @staticmethod
    def read(name):
        with open('customers.json', 'r') as f:
            data = json.load(f)

        for customer in data:
            if customer['name'] == name:
                return customer

    @staticmethod
    def delete(name):
        with open('customers.json', 'r') as f:
            data = json.load(f)

        for index, customer in enumerate(data):
            if customer['name'] == name:
                del data[index]
                print('Customer ' + name + ' deleted successfully')

        with open('customers.json', 'w') as f:
            json.dump(data, f)
        main()

    @staticmethod
    def login(name, password):
        with open('customers.json', 'r') as f:
            data = json.load(f)
        if len(data) == 0:
            print('No records found')
        else:
            for customer in data:
                if customer['name'] == name and customer['password'] == password:
                    customer_menu(customer)
                else:
                    print("Incorrect Username or Password")

    def create_subscription(self):
        trainer_name = input("Enter Trainer Name")
        plan_name = input("Enter Plan Name")
        start_date = input("Enter start date as YYYY-MM-DD")
        end_date = input("Enter end date as YYYY-MM-DD")

        subscription = Subscription(self['name'], trainer_name, plan_name, start_date, end_date)
        subscription.create()

        with open('customers.json', 'r') as f:
            data = json.load(f)

        for customer in data:
            if customer['name'] == self['name']:
                subscription = {
                    'trainer_name': trainer_name,
                    'plan_name': plan_name,
                    'start_date': start_date,
                    'end_date': end_date
                }
                customer['subscriptions'].append(subscription)
        with open('customers.json', 'w') as f:
            json.dump(data, f)
            print('Subscription Added to customer successfully')

    def read_subscription(self, trainer_name):
        with open('customers.json', 'r') as f:
            data = json.load(f)

        for customer in data:
            if customer['name'] == self['name']:
                for subscription in customer['subscriptions']:
                    if subscription.get('trainer_name') == trainer_name:
                        return subscription
        else:
            print('Subscription not found')

    def update_subscription(self, trainer_name, start_date=None, end_date=None):
        with open('subscriptions.json', 'r') as f:
            subscription_data = json.load(f)

        for subscription in subscription_data:
            if subscription['customer_name'] == self['name'] and subscription['trainer_name'] == trainer_name:
                if start_date:
                    subscription['start_date'] = start_date
                if end_date:
                    subscription['end_date'] = end_date
                break

        with open('subscriptions.json', 'w') as f:
            json.dump(subscription_data, f)
            print('Subscription Update Successfully')

        with open('customers.json', 'r') as f:
            customers_data = json.load(f)

        for customer in customers_data:
            subscriptions = customer['subscriptions']
            for subscription in subscriptions:
                if subscription['trainer_name'] == trainer_name:
                    if start_date:
                        subscription['start_date'] = start_date
                    if end_date:
                        subscription['end_date'] = end_date
                    break

        with open('customers.json', 'w') as f:
            json.dump(customers_data, f)
            print('Customers Subscription Update Successfully')

    def delete_subscription(self, trainer_name):
        with open('subscriptions.json', 'r') as f:
            subscription_data = json.load(f)

        for index, subscription in enumerate(subscription_data):
            if subscription['customer_name'] == self['name'] and subscription['trainer_name'] == trainer_name:
                del subscription_data[index]
                print('Your Subscription with' + trainer_name + ' is deleted successfully')
                break

        with open('subscriptions.json', 'w') as f:
            json.dump(subscription_data, f)

        with open('customers.json', 'r') as f:
            customers_data = json.load(f)

        for customer in customers_data:
            subscriptions = customer['subscriptions']
            for index, subscription in enumerate(subscriptions):
                if subscription['trainer_name'] == trainer_name:
                    subscriptions.pop(index)
                    break

        with open('customers.json', 'w') as f:
            json.dump(customers_data, f)
            print('Subscription deleted from customer successfully')

class Subscription:
    subscription_id = 1

    def __init__(self, customer_name, trainer_name, exercise_plan_name, start_date, end_date):
        self.subscription_id = str(Subscription.subscription_id)
        self.customer_name = customer_name
        self.trainer_name = trainer_name
        self.exercise_plan_name = exercise_plan_name
        self.start_date = start_date
        self.end_date = end_date
        Subscription.subscription_id += 1

    def create(self):
        with open('subscriptions.json', 'r') as f:
            data = json.load(f)

        data.append({
            'subscription_id': self.subscription_id,
            'customer_name': self.customer_name,
            'trainer_name': self.trainer_name,
            'exercise_plan_name': self.exercise_plan_name,
            'start_date': self.start_date,
            'end_date': self.end_date,
        })

        with open('subscriptions.json', 'w') as f:
            json.dump(data, f)
            print('Subscription Created Successfully')

    @staticmethod
    def read(customer_name):
        with open('subscriptions.json', 'r') as f:
            data = json.load(f)

        subscriptions = []
        for subscription in data:
            if subscription['customer_name'] == customer_name:
                subscriptions.append(subscription)

        return subscriptions

    def update(self):
        with open('subscriptions.json', 'r') as f:
            data = json.load(f)

        for subscription in data:
            if subscription['subscription_id'] == self.subscription_id:
                subscription.update({
                    'customer_name': self.customer_name,
                    'trainer_name': self.trainer_name,
                    'exercise_plan_name': self.exercise_plan_name,
                    'start_date': self.start_date,
                    'end_date': self.end_date,
                })
                break

        with open('subscriptions.json', 'w') as f:
            json.dump(data, f)

    @staticmethod
    def delete(subscription_id):
        with open('subscriptions.json', 'r') as f:
            data = json.load(f)

        for index, subscription in enumerate(data):
            if subscription['subscription_id'] == subscription_id:
                del data[index]
                print('Subscription ' + subscription_id + ' deleted successfully')
                break

        with open('subscriptions.json', 'w') as f:
            json.dump(data, f)

class Equipment:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    @staticmethod
    def read_all():
        with open('equipments.json', 'r') as f:
            data = json.load(f)
            equipments = []
            if len(data) == 0:
                print('No Equipments available')
            else:
                for equipment in data:
                    equipments.append(Equipment(equipment['name'], equipment['description']))
                return equipments

    @staticmethod
    def read(name):
        with open('equipments.json', 'r') as f:
            data = json.load(f)
            for equipment in data:
                if equipment['name'] == name:
                    return Equipment(equipment['name'], equipment['description'])
        return None

    @staticmethod
    def create():
        name = input('Enter equipment name: ')
        description = input('Enter equipment description: ')
        with open('equipments.json', 'r+') as f:
            data = json.load(f)
            equipments = data
            equipments.append({
                'name': name,
                'description': description
            })
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
        print('Equipment added successfully.')

    @staticmethod
    def delete(name):
        with open('equipments.json', 'r+') as f:
            data = json.load(f)
            equipments = data
            for equipment in equipments:
                if equipment['name'] == name:
                    equipments.remove(equipment)
                    break
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
        print('Equipment deleted successfully.')


class Trainer:
    trainer_id = 1

    def __init__(self, name, password, email, speciality):
        self.trainer_id = str(Trainer.trainer_id)
        Trainer.trainer_id += 1
        self.name = name
        self.password = password
        self.email = email
        self.speciality = speciality
        self.exercise_plans = []

    def create(self):
        with open('trainers.json', 'r') as f:
            data = json.load(f)

        data.append({
            'trainer_id': self.trainer_id,
            'name': self.name,
            'password': self.password,
            'email': self.email,
            'speciality': self.speciality,
            'exercise_plans': self.exercise_plans
        })

        with open('trainers.json', 'w') as f:
            json.dump(data, f)
            print('Trainer Created Successfully')

    @staticmethod
    def read(name):
        with open('trainers.json', 'r') as f:
            data = json.load(f)

        for trainer in data:
            if trainer['name'] == name:
                return trainer

        return None

    def update(self):
        with open('trainers.json', 'r') as f:
            data = json.load(f)

        for index, trainer in enumerate(data):
            if trainer['email'] == self.email:
                data[index] = {
                    'name': self.name,
                    'age': self.age,
                    'email': self.email,
                }
                break

        with open('trainers.json', 'w') as f:
            json.dump(data, f)

    @staticmethod
    def delete(name):
        with open('trainers.json', 'r') as f:
            data = json.load(f)

        for index, trainer in enumerate(data):
            if trainer['name'] == name:
                del data[index]
                print('Trainer ' + name + ' deleted successfully')
                break

        with open('trainers.json', 'w') as f:
            json.dump(data, f)

    @staticmethod
    def login(name, password):
        with open('trainers.json', 'r') as f:
            data = json.load(f)
        if len(data) == 0:
            print('No records found')
        else:
            for trainer in data:
                if trainer['name'] == name and trainer['password'] == password:
                    trainer_menu(trainer)

    def read_all_plans(self):
        plans = ExercisePlan.read_all()
        trainer_plans = []
        for plan in plans:
            if plan.trainer == self['name']:
                trainer_plans.append(plan)
        return trainer_plans

    def read_plan(self):
        return ExercisePlan.read(self['name'])

    def create_plan(self):
        plan_name = input('Enter plan name: ')
        equipment = input('Enter equipment name: ')
        duration = input('Enter duration: ')
        exercise_plan = ExercisePlan(self['name'],plan_name, equipment, duration)
        exercise_plan.create()

        with open('trainers.json', 'r') as f:
            trainers_data = json.load(f)

        for trainer in trainers_data:
            if trainer['name'] == self['name']:
                exercise_plan = {
                    'plan_name': plan_name,
                    'equipment': equipment,
                    'duration': duration,
                }
                trainer['exercise_plans'].append(exercise_plan)
        with open('trainers.json', 'w') as f:
            json.dump(trainers_data, f)
            print('Exercise Plan added to trainer successfully')

    def update_plan(self):
        exercise_plan = ExercisePlan.read(self['name'])
        if exercise_plan:
            exercise_plan.name = input('Enter new plan name: ')
            exercise_plan.equipment = input('Enter new equipment name: ')
            exercise_plan.duration = input('Enter new duration: ')
            exercise_plan.update()

            with open('trainers.json', 'r') as f:
                trainers_data = json.load(f)

            for trainer in trainers_data:
                exercise_plans = trainer['exercise_plans']
                for plan in exercise_plans:
                    if exercise_plan.name:
                        plan['plan_name'] = exercise_plan.name
                    if exercise_plan.equipment:
                        plan['equipment'] = exercise_plan.equipment
                    if exercise_plan.duration:
                        plan['duration'] = exercise_plan.duration
                    break

            with open('trainers.json', 'w') as f:
                json.dump(trainers_data, f)
                print('Exercise Plan updated to trainer successfully')
        else:
            print('Plan not updated, try again')

    def delete_plan(self, plan_name):
        ExercisePlan.delete(self['name'], plan_name)

        with open('trainers.json', 'r') as f:
            trainers_data = json.load(f)

        for trainer in trainers_data:
            exercise_plans = trainer['exercise_plans']
            for index, plan in enumerate(exercise_plans):
                if plan['plan_name'] == plan_name:
                    exercise_plans.pop(index)
                    break

        with open('trainers.json', 'w') as f:
            json.dump(trainers_data, f)
            print('Subscription deleted from customer successfully')


class ExercisePlan:

    def __init__(self, trainer, name, equipment, duration):
        self.trainer = trainer
        self.name = name
        self.equipment = equipment
        self.duration = duration

    @staticmethod
    def read_all():
        with open('exercise_plans.json', 'r') as f:
            data = json.load(f)
            plans = []
            for plan in data:
                plans.append(ExercisePlan(plan['trainer'],plan['name'], plan['equipment'], plan['duration']))
            return plans

    @staticmethod
    def read(trainer):
        with open('exercise_plans.json', 'r') as f:
            data = json.load(f)
            for plan in data:
                if plan['trainer'] == trainer:
                    return ExercisePlan(plan['trainer'], plan['name'], plan['equipment'], plan['duration'])
        return None

    def create(self):
        with open('exercise_plans.json', 'r+') as f:
            data = json.load(f)
            plans = data
            plans.append({
                'trainer': self.trainer,
                'name': self.name,
                'equipment': self.equipment,
                'duration': self.duration
            })
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
        print('Exercise plan added successfully.')

    def update(self):
        with open('exercise_plans.json', 'r+') as f:
            data = json.load(f)
            plans = data
            for plan in plans:
                if plan['trainer'] == self.trainer:
                    plan['name'] = self.name
                    plan['equipment'] = self.equipment
                    plan['duration'] = self.duration
                    break
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
        print('Exercise plan updated successfully.')

    @staticmethod
    def delete(trainer, plan_name):
        with open('exercise_plans.json', 'r+') as f:
            data = json.load(f)
            plans = data
            for plan in plans:
                if plan['trainer'] == trainer and plan['name'] == plan_name:
                    plans.remove(plan)
                    break
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
        print('Exercise plan deleted successfully.')



def customer_menu(customer):
    """This is the main program of tha application"""

    while True:
        print("WELCOME " + customer['name'], '\n')
        print("1. Delete Customer Account")
        print("2. View account details")
        print("3. Create Subscription")
        print("4. Read Subscription")
        print("5. Delete Subscription")
        print("6. Update Subscription")
        print("7. Logout")
        choice = int(input("Enter your choice (1-8): "))
        if choice == 1:
            confirmDelete = input("Are you sure you want to delete your account? (Enter yes/no)")
            if confirmDelete == 'yes':
                Customer.delete(customer['name'])
            elif confirmDelete == 'no':
                customer_menu(customer)
                break
        elif choice == 2:
            print(customer['name'], customer['password'], customer['gender'], customer['age'], customer['email'])
        elif choice == 3:
            Customer.create_subscription(customer)
        elif choice == 4:
            trainer_name = input("Enter your trainer name to see your subscription")
            print(Customer.read_subscription(customer, trainer_name))
        elif choice == 5:
            trainer_name = input('Enter your trainer name to delete your subscription')
            Customer.delete_subscription(customer, trainer_name)
        elif choice == 6:
            # update the start date of a subscription
            trainer_name = input('Enter your trainer name to update your subscription')
            Customer.update_subscription(customer, trainer_name, start_date='2023-05-15')
        elif choice == 7:
            print("You have logged out of the system", '\n')
            main()
            break
        else:
            print("Invalid choice. Please try again.")


def trainer_menu(trainer):
    """This is the main program of tha application"""

    while True:
        print("WELCOME " + trainer['name'], '\n')
        print("1. Delete Trainer Account")
        print("2. View trainer details")
        print("3. Read Exercise Plan")
        print("4. Create Exercise Plan")
        print("5. Delete Exercise Plan")
        print("6. Update Exercise Plan")
        print("7. Logout")
        choice = int(input("Enter your choice (1-8): "))
        if choice == 1:
            confirmDelete = input("Are you sure you want to delete your account? (Enter yes/no)")
            if confirmDelete == 'yes':
                Trainer.delete(trainer['name'])
            elif confirmDelete == 'no':
                trainer_menu(trainer)
                break
        elif choice == 2:
            print(trainer['name'], trainer['password'], trainer['email'], trainer['speciality'])
        elif choice == 3:
            plans = Trainer.read_all_plans(trainer)
            for plan in plans:
                print(plan.trainer, plan.equipment, plan.duration)
        elif choice == 4:
            Trainer.create_plan(trainer)
        elif choice == 5:
            plan_name = input("Enter the name of the plan you want to delete")
            Trainer.delete_plan(trainer, plan_name)
        elif choice == 6:
            Trainer.update_plan(trainer)
        elif choice == 7:
            print("You have logged out of the system", '\n')
            main()
            break
        else:
            print("Invalid choice. Please try again.")


def main():
    print("**WELCOME TO TU DUBLIN PYTHON GYM**", '\n')

    print("1. Login as Customer")
    print("2. Login as trainer")
    print("3. Create Customer Account")
    print("4. Create Trainer Account")
    print("5. See All Equipment")
    print("6. Add Equipment")
    print("7. Delete Equipment")
    print("8. Exit")
    choice = int(input("Enter your choice (1-3): "))
    if choice == 1:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        Customer.login(username, password)
    elif choice == 2:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        Trainer.login(username, password)
    elif choice == 3:
        name = input("Enter customer name: ")
        password = input("Enter customer password: ")
        age = int(input("Enter customer age: "))
        gender = input("Enter customer gender: ")
        email = input("Enter customer email: ")
        address = input("Enter customer address: ")
        customer = Customer(name, password, age, gender, email, address)
        customer.create()
        # Return to main menu
        main()
    elif choice == 4:
        name = input("Enter trainer name: ")
        password = input("Enter trainer password: ")
        email = input("Enter trainer email: ")
        speciality = input("Enter trainer speciality: ")
        trainer = Trainer(name, password, email, speciality)
        trainer.create()
    elif choice == 5:
        equipments = Equipment.read_all()
        for e in equipments:
            print(e.name)
    elif choice == 6:
        Equipment.create()
    elif choice == 7:
        name = input("please enter the name of the equipment you want to delete: ")
        Equipment.delete(name)
    elif choice == 8:
        print("It is sad to see you go, come back soon!!!")
    else:
        print("Invalid choice. Please try again.")


main()
