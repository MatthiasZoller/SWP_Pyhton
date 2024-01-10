from enum import Enum


class Gender(Enum):
    Male = 'male'
    Female = 'female'


class Firma:
    def __init__(self):
        self.abteilungen = []

    def add_abteilung(self, abteilung):
        self.abteilungen.append(abteilung)

    def get_mitarbeiter(self):
        count = 0
        for abt in self.abteilungen:
            count += abt.get_members_count()
        return count

    def get_abteilungsleiter(self):
        count = 0
        for abt in self.abteilungen:
            if abt.get_abteilungsleiter_count() > 0:
                count += 1
        return count

        return count

    def get_abteilungen(self):
        return len(self.abteilungen)

    def get_largest_abteilung(self):
        return max(self.abteilungen, key=lambda x: len(x.members)).name

    def get_gender_perc(self):
        total = self.get_mitarbeiter()
        male_count = sum(member.gender == Gender.Male for abt in self.abteilungen for member in abt.members)
        female_count = total - male_count
        per_male = (male_count / total) * 100
        per_female = (female_count / total) * 100

        return "female:", per_female, "male:", per_male


class Person:
    def __init__(self, firstname, lastname, gender):
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender


class Mitarbeiter(Person):
    def __init__(self, firstname, lastname, gender, department):
        super().__init__(firstname, lastname, gender)
        self.department = department


class Abteilungsleiter(Mitarbeiter):
    def __init__(self, firstname, lastname, gender, department):
        super().__init__(firstname, lastname, gender, department)


class Abteilung():
    def __init__(self, name):
        self.name = name
        self.members = []
        self.head = None

    def add_members(self, members):
        self.members.append(members)

    def set_head(self, head):
        self.head = head

    def get_members_count(self):
        return len(self.members)

    def get_abteilungsleiter_count(self):
        return 1 if self.head is not None else 0


if __name__ == '__main__':
    firma = Firma()

    abt1 = Abteilung("Vertrieb")
    abt2 = Abteilung("Marketing")

    mitarbeiter1 = Mitarbeiter("Josef", "Steiner", Gender.Male, abt2)
    mitarbeiter2 = Mitarbeiter("Andrea", "Vogel", Gender.Female, abt1)
    mitarbeiter3 = Mitarbeiter("Nico", "Lag", Gender.Male, abt2)
    abteilungsleiter1 = Abteilungsleiter("Jochn", "Baum", Gender.Male, abt1)
    abteilungsleiter2 = Abteilungsleiter("Hans", "Kraft", Gender.Male, abt2)

    abt1.add_members(mitarbeiter2)
    abt1.add_members(mitarbeiter3)
    abt1.set_head(abteilungsleiter1)

    abt2.add_members(mitarbeiter1)
    abt2.set_head(abteilungsleiter2)

    firma.add_abteilung(abt1)
    firma.add_abteilung(abt2)

    print("Name:", mitarbeiter2.firstname, mitarbeiter2.lastname)
    print("Gender:", mitarbeiter2.gender)
    print("Department:", mitarbeiter2.department.name)
