class Cat:
    def __init__(self, name, affection_level=0):
        self.name = name
        self.affection_level = affection_level

    def pet(self):
        self.affection_level += 10
        if self.affection_level > 100:
            self.affection_level = 100
        print(f"You pet {self.name}. Affection level is now {self.affection_level}!")

    def is_happy(self):
        return self.affection_level > 75

class Player:
    def __init__(self, name):
        self.name = name
        self.cats = []

    def adopt_cat(self, cat):
        self.cats.append(cat)
        print(f"{self.name} adopted {cat.name}!")

    def pet_cat(self, cat_name):
        for cat in self.cats:
            if cat.name == cat_name:
                cat.pet()
                break
        else:
            print(f"{self.name} doesn't have a cat named {cat_name}.")

    def show_cats(self):
        for cat in self.cats:
            print(f"{cat.name} - Affection level: {cat.affection_level}")

def main():
    player = Player(input("Enter your name: "))

    while True:
        print("\nOptions:")
        print("1. Adopt a cat")
        print("2. Pet a cat")
        print("3. See all my cats")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            cat_name = input("Enter the name of the cat you want to adopt: ")
            player.adopt_cat(Cat(cat_name))
        elif choice == '2':
            cat_name = input("Enter the name of the cat you want to pet: ")
            player.pet_cat(cat_name)
        elif choice == '3':
            player.show_cats()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
