label graduation:

    image prof = "professor.png"
    image bg cuclass = LiveTile("cuclass.jpg")

    scene bg cuclass
    show prof

    e "You think you're ready to graduate? We'll have to see about that"

    $creditReq = 3

    if Player.stats.credits >= creditReq:

        e "Since you have [Player.stats.credits] credits you can graduate!"

        e "Congratulations! But jokes on you! You racked up $ [Player.stats.money] in debt!"

    else:
        e "Sorry, you dont have enough credits to graduate"

        $creditMissing = creditReq - Player.stats.credits

        e "You need [creditMissing] more credits in order to graduate"

    return
