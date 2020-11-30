init python:
    from Python import character
    from Python import ledger
    from random import randint

label workout:
    image bg curec = LiveTile("curec.jpg")
    scene bg curec
    $rando=randint(0,100)
    if rando>80:
        e "You forgot your student ID, you owe $50"
        $Player.ledger.addBill(ledger.bill("Gym Charge",50))
        $Player.stats.money=Player.stats.money-50.0
    $Player.stats.attack=Player.stats.attack+3.0
    e "You got stronger!"

    jump tutorials
    return