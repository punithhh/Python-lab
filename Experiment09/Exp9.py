import pandas as pd

data = pd.DataFrame({
    "names": ["Aman", "Riya", "Karan", "Sneha", "Arjun", "Neha", "Rohit", "Pooja", "Vikram", "Anjali"],
    "age": [20, 21, 22, 20, 23, 21, 22, 20, 24, 23],
    "marks": [85, 90, 78, 88, 92, 76, 81, 89, 95, 87],
    "grades": ["A", "A+", "B", "A", "A+", "B", "B+", "A", "A+", "A"],
    "cities": ["Delhi", "Mumbai", "Chennai", "Kolkata", "Pune", "Hyderabad", "Jaipur", "Goa", "Kochi", "Lucknow"],
    "subjects": ["Math", "Science", "English", "History", "Physics", "Chemistry", "Biology", "Geo", "CS", "Economics"],
    "hobbies": ["Reading", "Gaming", "Music", "Dance", "Sports", "Drawing", "Singing", "Travel", "Coding", "Photography"],
    "devices": ["Phone", "Laptop", "Tablet", "PC", "Phone", "Laptop", "Tablet", "PC", "Phone", "Laptop"],
    "food": ["Pizza", "Burger", "Pasta", "Rice", "Noodles", "Biryani", "Fries", "Sandwich", "Cake", "Ice Cream"],
    "status": ["Pass", "Pass", "Pass", "Pass", "Pass", "Pass", "Pass", "Pass", "Pass", "Pass"]
})
print(data)
