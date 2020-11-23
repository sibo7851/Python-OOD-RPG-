default player = 1

image playerImage = DynamicImage("character[player].jpg")


show playerImage


screen charactermenus(adj):

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

                textbutton "character1":
                    action Return(1)
                    left_padding 20
                    xfill True

                textbutton "character2":
                    action Return(2)
                    left_padding 20
                    xfill True



        bar adjustment adj style "vscrollbar"

        textbutton _("That's enough for now."):
            xfill True
            action Return(False)
            top_margin 10



label characterSelect:

    call screen charactermenus(adj=tutorials_adjustment)

    $ chara = _return
    $player = chara
    show playerImage at right
