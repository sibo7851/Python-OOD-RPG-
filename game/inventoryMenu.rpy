init python:
    import os

    from Python import itemFactory
    from Python import inventory
    from Python import item
    
    bag=inventory.createTestInventory()

    gItem=item.Item();

    def mathFunction():
        return os.path.dirname(os.path.realpath(__file__))
# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("[povname]")

init python:

    # A list of section and tutorial objects.
    itemmenus = [ ]

    class TitleSection(object):
        """
        Represents a section of the tutorial menu.

        `title`
            The title of the section. This should be a translatable string.
        """

        def __init__(self, title):
            self.kind = "section"
            self.title = title

            itemmenus.append(self)


    class itemmenu(object):
        """
        Represents a label that we can jump to.
        """

        def __init__(self, label, title, item,move=True):
            self.kind = "itemText"
            self.label = label
            self.title = title
            self.move_before=False
            self.item=item

            if move and (move != "after"):
                self.move_before = True
            else:
                self.move_before = False

            if move and (move != "before"):
                self.move_after = True
            else:
                self.move_after = False

            itemmenus.append(self)

    TitleSection(_("Items"))

    def rebuildItemMenu():
        for i in set(bag.getItems()):
            itemmenu("itemText", _(i.itemName+" ("+str(bag.countItem(i))+")"),i)

    rebuildItemMenu()



screen itemmenus(adj):

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
                for i in itemmenus:

                    if i.kind == "itemText":

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




# The game starts here.
#begin start

label inventoryMenu:
    $bag=Player.inventory
    $itemmenus=[]
    $rebuildItemMenu()

    call screen itemmenus(adj=tutorials_adjustment)

    $ itemm = _return

    if not itemm:
        jump tutorials

    $gItem=itemm.item
    $renpy.jump(itemm.label)



label itemText:
    $iName = gItem.itemName
    menu:
     "What should I do?"
     
     "Use [iName].":
         "you used [iName]."
         $Player.inventory.removeItem(gItem)
         $itemmenus=[]
         $rebuildItemMenu()
         $Player.stats=Player.stats+gItem.itemStats

     "Dont Use":
         "Don't need to use that right now"

label after_menu:

     "What should I do next?"

    # Returning from the top level quits the game.
return

# The game starts here.

