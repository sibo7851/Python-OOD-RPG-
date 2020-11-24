init python:
    from Python import character


define e = Character("A Strange Voice")

label characterSetup:
    e "tell me a little more about yourself"

    menu:
     "What do you identify as?"

     "She/Her/Hers":
         "Understood"
         $Player.gender="Her"

     "He/Him/His":
         "Got it"
         $Player.gender="Him"

     "They/Them/Theirs":
         "Wonderful"
         $Player.gender="Them"

    label post_menu:

        "Great, now select your major"
    menu:
        "What should I do?"

        "Athletic":
            $Player=character.Athletic()

        "Engineering":
            $Player=character.Engineer()

        "Art":
            $Player=character.Art()

        "History":
            $Player=character.History()

    $Player.name=povname

    "Now that we've gotten that out of the way..."
    e "You should probably add some classes, they will help you build your stats, but each one will cost you per credit."
    e "In order to graduate you're going to need to take 150 credits."
    e "You'll find that it's really easy to spend money here at Mountain Public University, so it's a good thing you have a credit card with no limit!"
    e "Your goal is to find a way to graduate with the least amount of debt possible!"


    jump tutorials

    return