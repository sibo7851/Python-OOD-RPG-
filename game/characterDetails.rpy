init python:
    from Python import itemFactory
    from Python import inventory
    from Python import item
    from Python import character


define e = Character("A Strange Voice")

label characterDetails:
    $temp=Player.characterType
    e "[temp] [povname] has..."
    $temp=Player.stats.money
    e "[temp] money..."
    $temp=Player.stats.attack
    
    e "[temp] attack points..."
    $temp=Player.stats.defense
    e "[temp] defense points..."
    $temp=Player.stats.speed
    e "[temp] speed points..."
    $temp=Player.stats.currentHealth
    $temp2=Player.stats.maxHealth
    e "[temp]/[temp2] health..."
    $temp=Player.stats.currentMagic
    $temp2=Player.stats.maxMagic
    e "[temp]/[temp2] magic..."

    jump tutorials
return