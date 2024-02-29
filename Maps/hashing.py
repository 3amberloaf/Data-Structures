# Design a hashing scheme for storing and retrieving NJIT students records 
# Assume 12,000 students and use an address space of 15,000. 

# Constants
num_students = 12000
address_space = 15000 # total number of slots available for storing hashed values

# Stores student information
class StudentRecord:
    def __init__(self, student_id, admissions_credentials, transcripts, degree_works, bursar_bills, payments):
        self.student_id = student_id
        self.admissions_credentials = admissions_credentials
        self.transcripts = transcripts
        self.degree_works = degree_works
        self.bursar_bills = bursar_bills
        self.payments = payments

# Hash function
def hash_function(student_id):
    return student_id % address_space

# Inserts student record into hash table using seperate chaining 
def insert_student_record(hash_table, student_record, collision_counter):
    hash_address = hash_function(student_record.student_id) # finds hash address of student ID
    if hash_table[hash_address] is None:   
        hash_table[hash_address] = [student_record] # if no hash address, then add the student record
    else:
        collision_counter['count'] += 1
        hash_table[hash_address].append(student_record)  # Adds student record to corresponding hash table list
    
# Finds and returns student record 
def find_student_record(hash_table, student_id):
    hash_address = hash_function(student_id) # Finds hash adddress of student ID
    chain = hash_table[hash_address] # Returns the list of records for student ID
    if chain is not None: # If there is list of records for student ID
        for record in chain:
            if record.student_id == student_id:
                return record # Finds and returns student ID
    return None

student_ids = list(range(1, num_students + 1))

# Initialize the hash table
hash_table = [None] * address_space
collision_counter = {'count': 0}

for student_id in student_ids:
    # Create a mock StudentRecord for each student ID
    student_record = StudentRecord(
        student_id=student_id, 
        admissions_credentials=f"Credentials {student_id}", 
        transcripts=f"Transcripts {student_id}", 
        degree_works=f"Degree Works {student_id}", 
        bursar_bills=f"Bursar Bills {student_id}", 
        payments=f"Payments {student_id}"
    )
    insert_student_record(hash_table, student_record, collision_counter)

# Example: Retrieve a student record
retrieved_record = find_student_record(hash_table, 10301)
if retrieved_record:
    print(f"Student Record Found: {retrieved_record.student_id}, {retrieved_record.admissions_credentials}")
else:
    print("Student Record Not Found")

# Print the total number of collisions
print(f"Total collisions: {collision_counter['count']}")


