# Read and convert the student details
Student_name = input()           # Reads a string
Student_age = input()            # Reads a string
Student_age = int(Student_age)   # Converts to integer
Course_rating = input()          # Reads a string
Course_rating = float(Course_rating)  # Converts to float

# Display the values
print(f"Student: {Student_name}")
print(f"Age: {Student_age}")
print(f"Rating: {Course_rating}")

# Display the data types
print(type(Student_name))
print(type(Student_age))
print(type(Course_rating))
