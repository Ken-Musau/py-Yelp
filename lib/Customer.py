class Customer:

    all_customers = []

    def __init__(self, given_name, family_name) -> None:
        self.given_name = given_name
        self.family_name = family_name
        Customer.add_to_all(self)

    def given_name(self):
        return self._given_name

    def set_given_name(self, given_name):
        self._given_name = given_name

    given_name = property(given_name, set_given_name)

    def family_name(self):
        return self._family_name

    def set_family_name(self, family_name):
        self._family_name = family_name

    family_name = property(family_name, set_family_name)

    def full_name(self):
        return f"{self.given_name} {self.family_name}"

    @classmethod
    def add_to_all(cls, customer):
        cls.all_customers.append(customer)


ken = Customer("Kennedy", "Musau")
marge = Customer("Marge", "Lenana")
john = Customer("John", "doe")

# print(ken.given_name)
# ken.set_given_name("Steve")
print(Customer.all_customers)
