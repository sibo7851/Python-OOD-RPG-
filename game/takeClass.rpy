init python:
    from random import randint
    from Python import character
    from Python import ledger


define p = Character("Professor")

label takeClass:
    image prof = "professor.png"
    image bg cuclass = LiveTile("cuclass.jpg")
    scene bg cuclass
    show prof
    $randCred=randint(3,5)
    p "You payed $1k for [randCred] credits"
    p "Today you learned"

    $Player.stats.money=Player.stats.money-1000.0
    $Player.ledger.addBill(ledger.bill("Class",1000))
    $Player.stats.credits=Player.stats.credits+randCred



    jump tutorials

    return