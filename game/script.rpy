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
    from Python import millify

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

    Tutorial("takeClass", _("Take A Class"))

    Tutorial("wander", _("Wander Around"))

    Tutorial("inventoryMenu", _("Open Inventory"))

    Tutorial("characterDetails", _("Character Information"))


transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
    # This is to fade the bar in and out, and is only required once in your script

screen countdown:
    timer 1 repeat True action If(time<=100.0, true=SetVariable('time', Player.stats.money + interest), false=[Hide('countdown'), Jump(timer_jump)])
    $Player.stats.money=Player.stats.money+interest
    if time <= 0:
        text "$"+millify.millify(time, precision=2)+" debt accrued" xpos .01 ypos .01 color "#FF0000" at alpha_dissolve
    else:
        text "$"+millify.millify(time, precision=2)+" debt accrued" xpos .01 ypos .01 at alpha_dissolve

screen creditCount:
    timer 1 repeat True action If(True,true=SetVariable('credits', Player.stats.credits),false=SetVariable('time', time + interest))
    text str(credits)+" credits" xpos .9 ypos .01 color "#FFFFFF" at alpha_dissolve


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
    image chip = "chip.png"
    image bg cubg = LiveTile("cubg.jpeg")
    scene bg cubg
    show chip
    with dissolve
    $credits=Player.stats.credits
    $time = 0.0
    $timer_range = 0.0
    $timer_jump = tutorials

    # Start the background music playing.
    #play music "sunflower-slow-drag.ogg"

    window show

    $jones=mathFunction()


    e "Welcome to Mountain Public University!"

    e "Aren't you excited to be here?"

    python:
        povname = renpy.input("Would you please tell me your name?")
        povname = povname.strip()

        if not povname:
             povname = "Jeff Bridges"

    e "[povname]!"

    jump characterSetup


label tutorials:
    scene bg cubg
    show chip at left
    $time = Player.stats.money
    $interest=Player.stats.money*.01
    show screen countdown
    show screen creditCount

    show chip at left
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
        show chip at center
        with move

    #$ reset_example()

    call expression tutorial.label from _call_expression

    if tutorial.move_after:
        hide example
        show chip at left
        with move

    jump tutorials

label end:

    show chip at center
    with move

    show _finale behind chip


    e "You choose to go back to sleep, with many questions unanswered."

    window hide

    # Returning from the top level quits the game.
return

# The game starts here.

