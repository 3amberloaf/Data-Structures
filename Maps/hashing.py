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
def insert_student_record(hash_table, student_record):
    hash_address = hash_function(student_record.student_id)
    if hash_table[hash_address] is None:
        hash_table[hash_address] = [] # If a hash address is empty, it initializes an empty list
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

# Initialize the hash table
hash_table = [None] * address_space

# Example student
student_record = StudentRecord(10001, "Admissions Info", "Transcript Info", "Degree Works Info", "Bursar Bill Info", "Payment Info")
insert_student_record(hash_table, student_record)

retrieved_record = find_student_record(hash_table, 10001)
if retrieved_record:
    print("Student Record Found:", retrieved_record.student_id, retrieved_record.admissions_credentials)
else:
    print("Student Record Not Found")