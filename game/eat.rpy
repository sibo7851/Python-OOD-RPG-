init python:
    from Python import character
    from Python import ledger
    from random import randint

label eat:
    image bg cufood = LiveTile("cufood.jpg")
    scene bg cufood
    $rando=randint(0,100)
    e "You ate some fairly unhealthy fast food for $50"
    $Player.ledger.addBill(ledger.bill("Food",50))
    $Player.stats.money=Player.stats.money-50.0
    if Player.stats.currentHealth+3<=Player.stats.maxHealth:
        $Player.stats.currentHealth=Player.stats.currentHealth+3.0
    else:
        $Player.stats.currentHealth=Player.stats.maxHealth
    e "You got more energy!"

    jump tutorials
    return