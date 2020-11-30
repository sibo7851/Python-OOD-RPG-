init python:
    from Python import character
    from Python import ledger

label study:
    image bg culib = LiveTile("norlin.jpg")
    scene bg culib
    e "You paid for books, you owe $500"
    $Player.ledger.addBill(ledger.bill("Books",500))
    $Player.stats.money=Player.stats.money-500.0
    e "You got smarter!"
    $Player.stats.accuracy=Player.stats.accuracy+1

    jump tutorials
    return