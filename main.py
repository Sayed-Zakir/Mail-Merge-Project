PLACEHOLDER="[name]"

with open("C:/Users/zakir/Downloads/Python for days/Mail Merge Project/Mail Merge Project Start/Input/Names/invited_names.txt") as name_file:
    names=name_file.readlines()

with open("C:/Users/zakir/Downloads/Python for days/Mail Merge Project/Mail Merge Project Start/Input/Letters/starting_letter.txt") as starting_letter:
    letter_content= starting_letter.read() 
    for name in names:
        stripped_name= name.strip()
        new_letter=letter_content.replace(PLACEHOLDER,stripped_name)
        with open(f"C:/Users/zakir/Downloads/Python for days/Mail Merge Project/Mail Merge Project Start/Output/ReadyToSend/letter_to_{stripped_name}", mode="w") as completed_letter:
            completed_letter.write(new_letter)
