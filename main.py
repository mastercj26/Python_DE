
from my_processor.core import (
process_raw_members,
filter_members_by_domain,
get_all_names,
)
# Hardcoded "Raw Member Data" as specified in the assignment.
# Includes valid entries and a couple of intentionally malformed
# ones to demonstrate exception handling.
raw_members = [
{"name": "John Doe", "email": "john.doe@example.com", "phone": "555-0101"},
{"name": "Jane Smith", "email": "jane.smith@example.com", "phone": "555-0102"},
{"name": "InvalidData", "email": "jane.smith@...com", "phone": "555-0103"},
{"name": "Bob Lee", "email": "bob.lee@example.com", "phone": "not-a-number"},
{"name": "", "email": "missing.name@example.com", "phone": "555-0104"},
]

def main():
    print("--- Starting Member Data Processing ---\n")
    members, error_count = process_raw_members(raw_members)
    print("\n--- Functional Programming Demo ---")
    example_members = filter_members_by_domain(members, "example.com")
    print(f"Members with @example.com email: {get_all_names(example_members)}")
    print("\n--- Final Member Objects ---")
    for m in members:
      print(m)
if __name__ == "__main__":
   main()