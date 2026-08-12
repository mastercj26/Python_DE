
from my_processor.core import (
process_raw_members,
filter_members_by_domain,
get_all_names,
)

raw_members = [
{"name": "Chetan", "email": "chetan.jain@example.com", "phone": "555-0101"},
{"name": "Aman", "email": "jane.bddx@example.com", "phone": "555-0102"},
{"name": "aryan", "email": "vsrae.rdrch@...com", "phone": "555-0103"},
{"name": "Bob Lee", "email": "laks.@example.com", "phone": "not-a-number"},
{"name": "", "email": "qam.alal@example.com", "phone": "555-0104"},
]

def main():

    members, error_count = process_raw_members(raw_members)
    print("\n--- Functional Programming Demo ---")
    example_members = filter_members_by_domain(members, "example.com")
    print(f"Members with @example.com email: {get_all_names(example_members)}")

    for m in members:
      print(m)
if __name__ == "__main__":
   main()