import re

print("📧 Email Extractor Program\n")

# Step 1: Open input file
try:
    with open("input.txt", "r") as file:
        data = file.read()
except FileNotFoundError:
    print("❌ input.txt file not found!")
    exit()

# Step 2: Extract emails using regex
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", data)

# Step 3: Remove duplicates
emails = list(set(emails))

# Step 4: Check if emails found
if emails:
    print("✅ Emails found:\n")
    
    # Step 5: Save to output file
    with open("emails.txt", "w") as file:
        for email in emails:
            print(email)
            file.write(email + "\n")

    print("\n📁 Emails saved to emails.txt")
else:
    print("❌ No emails found in file")