init python:
    from random import randint
    from Python import character
    from Python import ledger
    from Python import command


define p = Character("Professor")
define n = Character("")

label takeClass:
    image prof = "professor.png"
    image bg cuclass = LiveTile("cuclass.jpg")
    scene bg cuclass
    show prof

    p "You payed $1k to take a class"
    p "The professor attacks with a Final Exam!"

    $Prof=character.Professor()
    $AICommand=command.ComplexCommand(Prof,True)
    $AIController.cmdOne=AICommand

    while True:
        $QAsked=0
        $QRight=0
        menu:
            "What should I do?"

            "Learn":
                $Choice=1

            "Give Up":
                $Choice=2

        $BattleController.cmdOne=AIController.cmdOne
        $BattleController.cmdTwo=PlayerController.cmdOne
        $temp=BattleController.cmdOne.execute()
        n "[temp]"
        $QAsked=QAsked+1
        $temp=BattleController.cmdTwo.execute()
        n "[temp]"
        $temp=(Prof.stats.attack/Player.stats.defense)
        $Player.stats.currentHealth=Player.stats.currentHealth-temp
        $Prof.stats.currentHealth=Prof.stats.currentHealth-(Player.stats.attack/Prof.stats.defense)
        n "You lost [temp] health"
        $rando=randint(0,100)
        $temp=(Player.stats.accuracy/Prof.stats.evasion)*100
        n "You have a [temp] chance of getting the question right"
        if rando<temp:
            n "You answered the question correctly"
            $QRight=QRight+1
        else:
            n "Your answer was incorrect"

        if Player.stats.currentHealth<=0.0:
            "You were too exhausted to make it through the class"
            jump failedClass
        if Prof.stats.currentHealth<=0.0:
            $temp=(QRight/QAsked)*100
            n "You got a [temp] in the class"
            if temp>70.0:
                jump finishClass
            else:
                jump failedClass



label finishClass:



    $randCred=randint(3,5)
    n "You payed $1k for [randCred] credits"
    n "Today you learned"

    $Player.stats.money=Player.stats.money-1000.0
    $Player.ledger.addBill(ledger.bill("Class",1000))
    $Player.stats.credits=Player.stats.credits+randCred



    jump tutorials

label failedClass:
    p "Sorry, I see you didn't study at all."
    n "You failed the class."

    jump tutorials

return