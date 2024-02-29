# Design a hashing scheme for storing and retrieving NJIT students records 
# Assume 12,000 students and use an address space of 15,000. 

# Constants
num_students = 12000
address_space = 15000 # total number of slots available for storing hashed values

# Hash function
def hash_function(student_id):
    return student_id % address_space

# Simulate hashing and collision detection
def simulate_hashing_and_collision(num_students, address_space):
    
    # Generate unique mock student IDs
    student_ids = list(range(1, num_students + 1))
    
    # Initialize empty hash table
    hash_table = [None] * address_space
    collisions = 0  # Initialize collision counter

    # Hash each student ID and check for collisions
    for student_id in student_ids:
        hash_address = hash_function(student_id)
        
        # If the slot is already filled, it's a collision
        if hash_table[hash_address] is not None:
            collisions += 1
        else:
            hash_table[hash_address] = student_id  # Assign student ID to the hash address

    return collisions

# Run the simulation
collisions = simulate_hashing_and_collision(num_students, address_space)

print(f"Number of collisions: {collisions}")
