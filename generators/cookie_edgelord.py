# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 19:03:13 2020

@author: Ehlion
"""

from wordgenerator.Weight import WeightNode as weightmap
from wordgenerator.Sequence import SequenceNode
from wordgenerator.Print import PrintNode, PrintToBuffer

PrintNode._printer = PrintToBuffer()

antagonist = weightmap()
antagonist.extend([
    [3,"An evil wizard"],
    [3,"A dragon"],
    [3,"The drow"],
    [3,"Goblins"],
    [3,"Kobolds"],
    [3,"A mind flayer"],
    [3,"Evil cultists"],
    [3,"Orcs"],
    [3,"Trolls"],
    [3,"A banshee"],
    [3,"A demon lord"],
    [3,"An archdevil"],
    [3,"Giants"],
    [3,"Vampires"],
    [3,"Gnolls"],
    [3,"A werewolf"],
    [3,"A djinni"],
    [3,"A mimic"],
    [3,"A tarrasque"],
    [3,"A beholder"],
    [3,"A hag coven"],
    [3,"A lich"],
    [3,"Barbarians"],
    [3,"An aboleth"],
    [3,"A sucuubus"],
    [3,"A criminal organisation"],
    [3,"A gelatinous cube"],
    [3,"A necromancer"],
    [3,"Corrupt nobles"],
    [3,"A death knight"],
    [3,"The BBEG"],
    [3,"The bard"],
    [3,"Natural selection"],
    [1,"The DM"],
])

action = weightmap()
action.extend([
    [9,"killed"],
    [10,"murdered"],
    [10,"slautered"],
    [10,"massacred"],
    [10,"assassinated"],
    [3,"brainwashed"],
    [3,"captured"],
    [3,"banished"],
    [3,"enslaved"],
    [3,"betrayed"],
    [3,"sacrificed"],
    [3,"mauled"],
    [3,"stole"],
    [3,"blackmailed"],
    [3,"conned"],
    [3,"framed"],
    [3,"humiliated"],
    [3,"pillaged"],
    [3,"ruined"],
    [3,"ate"],
    [3,"cursed"],
    [2,"befriended"],
    [1,"seduced"],
])

victim = weightmap()
victim.extend([
    [4,"my family"],
    [4,"my hometown"],
    [4,"my parents"],
    [4,"my clan"],
    [4,"my siblings"],
    [4,"my mentors"],
    [4,"my significant other"],
    [4,"my master"],
    [4,"my side squeeze"],
    [4,"my apprentice"],
    [4,"my friends"],
    [4,"my previous adventuring party"],
    [4,"my everyone I knew"],
    [4,"my crew of sailors"],
    [4,"my crew of pirates"],
    [4,"my crew of noble outlaws"],
    [4,"my crew of thieves"],
    [4,"the tavern I basically lived in"],
    [4,"my start-up business"],
    [4,"my military unit"],
    [4,"my social status"],
    [4,"my treasure"],
	[4,"my aspirations"],
	[4,"my confidence"],
	[3,"my honor"],
	[1,"my imaginary friends"],
])

outcome = weightmap()
outcome.extend([
    [29,"And it will have no effect on how I roleplay my character"],
    [10,"And now I'm a murder hobo"],
    [10,"And now I'm a lawful good stick in the mud"],
    [ 4,"And now I seek vengeance"],
    [ 4,"And now I trust no one"],
    [ 4,"And now I have a bleak outlook of the world"],
    [ 4,"And now I strive to live by their ideals"],
    [ 4,"And now I must become stronger"],
    [ 5,"And now I seek to bring back what I have lost"],
    [ 4,"And now I vow to prevent that from happening to anyone else"],
    [ 4,"And now I am haunted by their memory"],
    [ 4,"And now I seek to uncover the truth about what happened"],
    [ 4,"And now I fear it will happen again"],
    [ 3,"And now I am stronger because of it"],
    [ 3,"And now I'm an alcoholic"],
    [ 3,"And now I have multiclassed into warlock"],
    [ 1,"And now I'm Batman"],
])

sequence = SequenceNode()
sequence.inbetween_action = PrintNode(" ")
sequence.extend([
    antagonist,
    action,
    victim,
    outcome
])
sequence.execute()

print(PrintNode._printer.get_text())
