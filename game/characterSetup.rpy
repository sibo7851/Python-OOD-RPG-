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

        "Great, now select your job"
    menu:
        "What should I do?"

        "Biker":
            $Player=character.Biker()

        "Scientist":
            $Player=character.Scientist()

        "Yuppie":
            $Player=character.Yuppie()

        "Priest":
            $Player=character.Priest()

    $Player.name=povname

    "Now that we've gotten that out of the way..."

    jump tutorials

    return