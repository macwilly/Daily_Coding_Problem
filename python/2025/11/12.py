'''
Email Signature Generator

Given strings for a person's name, title, and company, return an email signature as a single string using the
following rules:
 * The name should appear first, preceded by a prefix that depends on the first letter of the name.
   For names starting with (case-insensitive):
     * A-I: Use >> as the prefix.
     * J-R: Use -- as the prefix.
     * S-Z: Use :: as the prefix.
 * A comma and space (, ) should follow the name.
 * The title and company should follow the comma and space, separated by " at " (with spaces around it).
For example, given "Quinn Waverly", "Founder and CEO", and "TechCo" return "--Quinn Waverly, Founder and CEO at TechCo".

Test Case
1. generate_signature("Quinn Waverly", "Founder and CEO", "TechCo") should return "--Quinn Waverly, Founder and CEO at TechCo".
2. generate_signature("Alice Reed", "Engineer", "TechCo") should return ">>Alice Reed, Engineer at TechCo".
3. generate_signature("Tina Vaughn", "Developer", "example.com") should return "::Tina Vaughn, Developer at example.com".
4. generate_signature("B. B.", "Product Tester", "AcmeCorp") should return ">>B. B., Product Tester at AcmeCorp".
5. generate_signature("windstorm", "Cloud Architect", "Atmospheronics") should return "::windstorm, Cloud Architect at Atmospheronics".
'''

def generate_signature(name, title, company):
    # Initialize the return
    signature = ""
    # Getting the first letter of the first name and setting to upper for case-insensitivity and to match upper directive
    first_letter = name[0].upper()

    if 'A' <= first_letter <= 'I':
        name = ">>" + name
    elif 'J' <= first_letter <= 'R':
        name = "--" + name
    else:
        name = "::" + name

    signature = f"{name}, {title} at {company}"
    return signature

test_arr = [
    ["Quinn Waverly", "Founder and CEO", "TechCo"],
    ["Alice Reed", "Engineer", "TechCo"],
    ["Tina Vaughn", "Developer", "example.com"],
    ["B. B.", "Product Tester", "AcmeCorp"],
    ["windstorm", "Cloud Architect", "Atmospheronics"]
]

for filename in test_arr:
        print(generate_signature(filename[0], filename[1], filename[2]))