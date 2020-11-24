init python:
    import os


    def mathFunction():
        return os.path.dirname(os.path.realpath(__file__))
# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define pov = Character("[povname]")
define e = Character("A Strange Voice")

init python:
    from pydblite import pydblite
    
    from Python import itemFactory
    from Python import inventory
    from Python import item
    from Python import character

    global Player
    Player=character.RPGCharacter()
        

    def DBTest():
        db = pydblite.Base('/Users/Sid/Documents/RenProject/Gates of Galloo/dummy.pdl')
        db.path=mathFunction()+"testDB.pdl"
        # create new base with field names
        db.create('name', 'age', 'size')
        # insert new record
        db.insert(name='homer', age=23, size=1.84)
        # records are dictionaries with a unique integer key __id__
        # simple selection by field value
        records = db(name="homer")
        # complex selection by list comprehension
        db.commit()

    # A list of section and tutorial objects.
    tutorials = [ ]

    class Section(object):
        """
        Represents a section of the tutorial menu.

        `title`
            The title of the section. This should be a translatable string.
        """

        def __init__(self, title):
            self.kind = "section"
            self.title = title

            tutorials.append(self)


    class Tutorial(object):
        """
        Represents a label that we can jump to.
        """

        def __init__(self, label, title, move=True):
            self.kind = "tutorial"
            self.label = label
            self.title = title

            if move and (move != "after"):
                self.move_before = True
            else:
                self.move_before = False

            if move and (move != "before"):
                self.move_after = True
            else:
                self.move_after = False

            tutorials.append(self)


    Section(_("What would you like to do?"))

    Tutorial("wander", _("Wander Around"))

    Tutorial("inventoryMenu", _("Open Inventory"))

    Tutorial("characterDetails", _("Character Information"))


screen tutorials(adj):

    frame:
        xsize 640
        xalign .5
        ysize 485
        ypos 30

        has side "c r b"

        viewport:
            yadjustment adj
            mousewheel True

            vbox:
                for i in tutorials:

                    if i.kind == "tutorial":

                        textbutton i.title:
                            action Return(i)
                            left_padding 20
                            xfill True

                    else:

                        null height 10
                        text i.title alt ""
                        null height 5




        bar adjustment adj style "vscrollbar"

        textbutton _("That's enough for now."):
            xfill True
            action Return(False)
            top_margin 10


# This is used to preserve the state of the scrollbar on the selection
# screen.
default tutorials_adjustment = ui.adjustment()

# True if this is the first time through the tutorials.
default tutorials_first_time = True


# The game starts here.
#begin start
label start:
#end start
    image bg cubg = LiveTile("cubg.jpeg")
    scene bg cubg
    show eileen vhappy
    with dissolve

    # Start the background music playing.
    #play music "sunflower-slow-drag.ogg"

    window show

    $jones=mathFunction()


    e "You find yourself in a strange unknown land."

    e "Who are you?"

    python:
        povname = renpy.input("What is your name?")
        povname = povname.strip()

        if not povname:
             povname = "Jeff Bridges"

    e "[povname]!"

    jump characterSetup


label tutorials:

    show eileen happy at left
    with move

    if tutorials_first_time:
        $ e(_("What would you like to do?"), interact=False)
    else:
        $ e(_("Is there anything else you'd like to do?"), interact=False)

    $ tutorials_first_time = False
    $ renpy.choice_for_skipping()

    call screen tutorials(adj=tutorials_adjustment)

    $ tutorial = _return

    if not tutorial:
        jump end

    if tutorial.move_before:
        show eileen happy at center
        with move

    #$ reset_example()

    call expression tutorial.label from _call_expression

    if tutorial.move_after:
        hide example
        show eileen happy at left
        with move

    jump tutorials

label end:

    show eileen happy at center
    with move

    show _finale behind eileen


    e "You choose to go back to sleep, with many questions unanswered."

    window hide

    # Returning from the top level quits the game.
return

# The game starts here.

