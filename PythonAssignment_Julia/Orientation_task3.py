import pandas as pd
import numpy as np

ratingsInput = pd.read_csv('RatingsInput.csv')
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

ratingsInput["MovieID"] = ratingsInput["MovieName"].str.split(',').str.get(0)
ratingsInput["MovieName"] = ratingsInput["MovieName"].str.split(',').str.get(1)
ratingsInput["MovieName"] = ratingsInput["MovieName"].str.title()
ratingsInput_with_age_and_rating = ratingsInput.sort_values(["UserAge", "Rating"], ascending=[True, False])
ratingsInput_create_dict = ratingsInput_with_age_and_rating[["UserAge", "Rating", "MovieName"]]

print(ratingsInput_create_dict)


list_of_dict = {13: {5: ["Chump Change"], "3": ["We'Re Not Married"],
                       "2": ["Fighter", "Abc Primetime: Mel Gibson's The Passion Of The Christ"],
                       "1": ["The Love Letter"]},
                "15": {"4": ["Sex And The Beauties"], "3": ["Dinosaur Planet", "Lady Chatterley"],
                       "2": ["Neil Diamond: Greatest Hits Live", "A Yank In The Raf"]},
                "19": {"5": ["The Libertine"], "3": ["8 Man", "Boycott", "Searching For Paradise",
                             "Devo: The Complete Truth About De-Evolution", "Jonah: A Veggietales Movie: Bonus Material",
                             "Dragonheart"], "2": ["Nature: Antarctica"]},
                "20": {"5": ["Zatoichi'S Conspiracy"], "4": ["Seeta Aur Geeta", "Something'S Gotta Give",
                             "Silent Service", "The Weather Underground"], "3": ["Screamers", "My Bloody Valentine"],
                        "2": ["Isle Of Man Tt 2004 Review", "What The Hell Do We Know!?"]},
                "21": {"5": ["The Rise And Fall Of Ecw", "Sesame Street: Elmo'S World: The Street We Live On"],
                       "4": ["My Favorite Brunette", "The Bad And The Beautiful"],
                       "3": ["By Dawn'S Early Light", "Pitcher And The Pin-Up"],
                       "2": ["Ashtanga Yoga: Beginner'S Practice With Nicki Doane"], "1": ["Carandiru"]},
                "25": {"5": ["Daydream Obsession"], "4":["7 Seconds"], "2": [" Inspector Morse 31: Death Is Now My Neighbour"],
                       "1": ["Character"]},
                "35": {"5": ["Love Reinvented"],
                       "4": ["Paula Abdul'S Get Up & Dance", "Clifford: Clifford Saves The Day! Clifford'S Fluffiest Friend Cleo",
                             "Never Die Alone"], "3": ["Full Frame: Documentary Shorts", "Rudolph The Red-Nosed Reindeer",
                                                       "Jade"],
                       "2": ["Immortal Beloved"], "1": ["Aqua Teen Hunger Force: Vol. 1"]},
                "36": {"5": ["Lord Of The Rings: The Return Of The King: Extended Edition: Bonus Material",
                            "Justice League"], "4": ["Sick"], "3": ["Lilo And Stitch", "Ferngully 2: The Magical Rescue"],
                       "2": ["Horror Vision", "Richard Iii"]},
                "40": {"5": ["Classic Albums: Meat Loaf: Bat Out Of Hell","The Bonesetter"], "4": ["Strange Relations"],
                       "2": ["Spitfire Grill"], "1": ["Class Of Nuke 'Em High 2"]}
}

print(list_of_dict)









