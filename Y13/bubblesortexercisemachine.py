import random

def bubble_sort(arr):
    n = len(arr)
    sorted_arr = arr.copy()
    for i in range(n):
        for j in range(0, n-i-1):
            if sorted_arr[j] > sorted_arr[j+1]:
                sorted_arr[j], sorted_arr[j+1] = sorted_arr[j+1], sorted_arr[j]
    return sorted_arr

def generate_data():
    size = random.randint(5, 10)
    data = random.sample(range(1, 100), size)
    return data

def main():
    exercises = []
    solutions = []
    while True:
        print("1. Generate a new exercise")
        print("2. Solve an exercise")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3):")
        if choice == '1':
            data = generate_data()
            exercises.append(data)
            solutions.append(bubble_sort(data))
            print(f"New exercise generated: {data}")

        elif choice == '2':
            if not exercises:
                print("No exercises available. Please generate a new exercise first.")
                continue
            print("Available exercises:")
            for i, exercise in enumerate(exercises):
                print(f"{i+1}. {exercise}")
            exercise_number = int(input("Enter the number (not how many) of the exercise you want to solve: "))
            if exercise_number < 1 or exercise_number > len(exercises):
                print("Invalid exercise number. Please try again.")
                continue
            user_solution = input(f"Enter your sorted array for the exercise without any square brackets and separated with spaces cuz formatting :p {exercises[exercise_number-1]} \ninput here:")
            user_solution = [int(x) for x in user_solution.split()]
            if user_solution == solutions[exercise_number-1]:
                print("Correct! Well done.")
            else:
                print(f"Wrong! The correct sorted array is {solutions[exercise_number-1]}")

        elif choice == '3':
            print("Byeeeee...")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
