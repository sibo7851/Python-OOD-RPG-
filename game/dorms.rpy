init python:
    from Python import character
    from Python import ledger
    from random import randint

label dorms:
    image bg cudorms = LiveTile("cudorms.jpg")
    scene bg cudorms
    $rando=randint(0,100)
    e "You paid $1000 to sleep in the dorms!"
    $Player.ledger.addBill(ledger.bill("Dorm Bill",1000))
    $Player.stats.money=Player.stats.money-1000.0

    $Player.stats.maxHealth=Player.stats.maxHealth+20.0
    $Player.stats.currentHealth=Player.stats.maxHealth
    e "You woke up feeling refreshed!"

    jump tutorials
    return