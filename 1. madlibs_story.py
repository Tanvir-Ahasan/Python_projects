def madlibs_story():
    inputs = []
    inputs.append(input("Enter a name: "))
    inputs.append(input("Enter two adjectives: "))
    inputs.append(input("Enter two nouns: "))
    inputs.append(input("Enter an animal: "))
    inputs.append(input("Enter two more adjectives: "))
    inputs.append(input("Enter the last noun: "))

    for i in inputs:
        if not i:
            print("Input cannot be blank")
            return

    person_name, adj1, adj2, noun1, noun2, animal_type, adj3, adj4, noun3 = inputs[0], inputs[1].split()[0], \
                                                                            inputs[1].split()[1], inputs[2].split()[0], \
                                                                            inputs[2].split()[1], inputs[3], \
                                                                            inputs[4].split()[0], inputs[4].split()[1], \
                                                                            inputs[5]

    story = f"Once there was a man named {person_name} who lived in a {adj1} village. He sought the {adj2} {noun1} to grant his wishes. He encountered a witch who offered to help in exchange for a {adj3} {noun2}. They found the {noun1} but it turned {person_name} into a {adj4} {animal_type}. To break the spell, {person_name} had to do a {adj3} dance and sing a {adj4} song in front of the {adj1} {noun3}. {person_name} succeeded and returned to the village a hero, living happily ever after."

    print(story)


madlibs_story()
