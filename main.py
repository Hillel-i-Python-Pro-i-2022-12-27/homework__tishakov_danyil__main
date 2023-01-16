def create_users():
    from faker import Faker

    faker = Faker()

    print(f"name: {faker.name()}")
    print(f"text: {faker.email()}")
    print(f"address: {faker.address()}")


if __name__ == "__main__":
    create_users()
