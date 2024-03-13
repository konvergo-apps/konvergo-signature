import json
from unidecode import unidecode

# Load data from the JSON file
with open("data.json") as json_file:
    data = json.load(json_file)

# Read the HTML template
with open("template.html") as template_file:
    template = template_file.read()

# Define the output directory
output_dir = "output/"

# For each user, replace data and create a new signature
for user in data["users"]:
    personalized_signature = template.replace("{{name}}", user["name"])
    personalized_signature = personalized_signature.replace("{{photo}}", user["photo"])

    # Create a file name that is all lowercase and without accents
    filename = f"{output_dir}signature_{unidecode(user['name']).replace(' ', '_').lower()}.html"

    # Save the personalized signature to an HTML file in the output directory
    with open(filename, "w") as output_file:
        output_file.write(personalized_signature)

    # Print a confirmation message
    print(f"Signature file created: {filename}")
