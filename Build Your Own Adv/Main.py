def play_again():
    deaths = 0
    deaths += 1
    again = input("Would you like to play again? (y/n) ")
    if again.lower() == 'y':
        tutorial()
    else:
        print(f"Thanks for playing! You have died {deaths} times")
        exit()


def phase_one():
    pass


def tutorial():
    print("""
        The first rays of dawn kissed the snowy peaks of the Aethelstone Mountains, painting them a brilliant rose gold.
         Below, nestled against their base, the city of Spearpoint basked in the newfound warmth.
         Banners bearing the sigil of a crimson griffin fluttered proudly in the crisp morning air, 
         a vibrant counterpoint to the stoic mountains that guarded its back. 
         From the training grounds below, the rhythmic clang of steel on steel echoed 
         – a symphony of unwavering vigilance in this corner of the kingdom.""")

    print("""
        Sunlight glared off the polished breastplate as you paced the battlements. Every day was the 
        same: guard duty, the clang of the forge, shouts of trainees. Today, though, a prickle of unease crawled up 
        their spine. The mist below seemed different, a swirling grey that choked the valley. Then, a flicker. Smoke. 
        Not the wispy tendrils from a cook fire, but thick, black plumes rising from multiple points. The warrior's 
        heart hammered.  Another flicker, this time movement – a glint of metal catching the weak morning light. An 
        army. An army unlike any they'd ever seen, stretching out across the valley floor like a steel serpent. Your 
        dream was about to become a waking nightmare.""")

    choice = input("\nThe warrior's breath caught – alert the captain, or race to warn the King's own guard? "
                   "(captain/king)\nChoice: ")

    if choice == "captain":
        print("""
        Panic clawed at the warrior's throat.  Ignoring protocol, they sprinted towards Captain Varis, 
        his normally stoic face pale under his helm. "Captain! We're under attack! A massive army…" The words tumbled 
        out, breathless. Varis' lips stretched into a smile that never reached his eyes. 'Excellent work, 
        soldier! Raise the alarm! Ring the bell and rouse the men. I'll gather them at the courtyard.' 
        
        """)
        choice = input("Would you like to ring the bell and discern the intentions of the captain?"
                       "(ring/intentions)\nChoice: ")
        if choice == "ring":
            print("""
            The warrior, thrown by Varis' urgency, obeyed. They yanked the heavy rope, the bell's toll shattering the 
            morning calm.""")
        else:
            print("""The smile vanished from Varis' face as his eyes darted to the warrior. The truth hung heavy in 
            the air, a betrayal his apprentice had somehow sniffed out. "See those approaching?" Varis forced a 
            steady tone. "Allies. Just a misunderstanding. No alarm needed."

            The warrior's gaze held Varis', suspicion tightening like a fist around their heart. Varis' hand 
            instinctively reached for his sword. "Trust me," he hissed, his voice a cold rasp. "This will be 
            easier... now.""")
            print("You perished by your own choices. Good luck on your next try.")
            play_again()
    else:
        print(
            """
            Ignoring the pounding in your chest and the pre-established chain of command, you bolted. The 
            sight of that monstrous army slithering towards Spearpoint demanded a response beyond the walls. Your
            gut churned with a primal certainty – the King. Only the King's command could marshal the entire city's 
            defenses, only his voice could unite Spearpoint against this unthinkable threat.  Dust billowed in your 
            wake as you sprinted through the city, every fiber of your being focused on reaching the King before it 
            was too late. The rhythmic clang of the blacksmith's hammer, once a comforting background hum, 
            now sounded a frantic counterpoint to the pounding of your own heartbeat. You had to reach the King, 
            for Spearpoint, for the kingdom, for the very future they now desperately fought to preserve."""
        )

        print("""
        The warrior's lungs burned as they rounded the final corner, the imposing silhouette of the King's 
        palace rising before them. Relief warred with a fresh wave of trepidation. There, in a courtyard bathed in 
        morning sunlight, sat the King himself. Unarmored, unguarded, reading a parchment while taking a solitary 
        breakfast.

        Two paths unfurled before the warrior. One, the path of honesty – to blurt out the impending doom, to shatter 
        the King's peace with the grim truth. The other, a gamble – a desperate, unorthodox plan that gnawed at their 
        conscience.

        To tell the King outright meant panic, scrambling defenses, and a bloody battle. But to bring him to witness 
        the sheer terror of the approaching army firsthand... that might be the only way to avoid a fight altogether. 
        It would mean sacrificing their honor, appearing cowardly, but maybe, just maybe, it could save countless lives.

        The warrior swallowed a lump in their throat. This wasn't about glory; it was about survival. Taking a deep 
        breath, they approached the King, a silent prayer forming on their lips. Perhaps, in this unconventional act, 
        there might be a sliver of a chance to avert the coming storm.""")

        choice = input("Would you like to tell the king about the incoming army or attempt to kill the king? (talk/ "
                       "kill)\nChoice: ")
        if choice == "talk":
            print("""The King deserved the truth, and Spearpoint the chance to prepare. As the warrior drew closer, 
            their voice rose, a desperate plea shattering the peaceful morning. "Your Majesty! We are under attack! A 
            massive army approaches!""")

            print(
                """The King, a man with eyes like steel and a weathered face that held the weight of countless 
                battles, listened intently. When the warrior finished, a grim smile played on his lips. He gestured 
                towards a nearby stone altar, its surface etched with arcane symbols.

                "This threat deserves a response the whole kingdom can hear," he declared.

                The warrior watched as the King placed his hand on the altar, muttering words that crackled with 
                power. A faint blue light emanated from the runes, then surged upwards, engulfing the King in its 
                glow. His voice, normally deep and steady, boomed outwards, amplified by a hundredfold.
                
                "People of Spearpoint!" the King's voice echoed, rolling across the city and beyond, shaking the very 
                foundations of the palace. "An enemy approaches, a force unlike any we have faced before! But fear 
                not! Your King stands with you. Mages, sharpen your spells! Knights, polish your blades! Merchants, 
                gather your supplies! Every man, woman, and child – prepare for war! Defend your homes, defend your 
                families, defend Spearpoint!"
                
                The King's voice resonated through every alley, every marketplace, every home. A palpable energy 
                crackled in the air, replaced by the steely resolve of a united kingdom preparing to face the coming 
                storm.
            """)

            print("Now, young warrior. Will you be able to defend Spearpoint?")
            phase_one()
        else:
            print("""Shame battled with desperation. This wasn't about honor anymore. It was about saving Spearpoint. 
            Hand on sword, the warrior lunged. The King, eyes widening in shock, barely fended off the attack with a 
            breakfast knife. Steel screamed against steel in a desperate fight. The warrior pressed on, but the King, 
            surprisingly nimble, countered every move. The clang of metal finally shattered the King's breakfast, 
            but before the warrior could win, a searing pain erupted in their chest. The King, his face contorted 
            with rage, had plunged the knife deep. As darkness closed in, the warrior clung to a single, 
            desperate hope: their failed gamble might somehow warn the city in time.""")
            print("\nYour dishonour brought you defeat. Good luck on your next try.")
            play_again()


def main():
    print("Welcome to Project 'Noira', a game that will test your wits and your abilities to wield your sword to "
          "protect the King of Spearpoint.")
    name = input("What is your name, player?: ")
    print(f"\nHello, {name}.\n Are you ready for the adventure of your life? ")
    tutorial()


main()
