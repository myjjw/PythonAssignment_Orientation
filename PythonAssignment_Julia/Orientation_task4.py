import pandas as pd
import numpy as np
import itertools

newUsers = pd.read_csv('NewUsers.csv')
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)


newUsers_list = newUsers.to_dict('list')


list_of_dict = {35: {5: ["Love Reinvented"],
                     4: ["Paula Abdul'S Get Up & Dance", "Clifford: Clifford Saves The Day! Clifford'S Fluffiest Friend Cleo",
                             "Never Die Alone"], 3: ["Full Frame: Documentary Shorts", "Rudolph The Red-Nosed Reindeer",
                                                       "Jade"],
                     2: ["Immortal Beloved"], 1: "Aqua Teen Hunger Force: Vol. 1"},
                13: {5: ["Chump Change"], 3: ["We'Re Not Married"],
                     2: ["Fighter", "Abc Primetime: Mel Gibson's The Passion Of The Christ"],
                     1: ["The Love Letter"]},
                15: {4: ["Sex And The Beauties"], 3: ["Dinosaur Planet", "Lady Chatterley"],
                     2: ["Neil Diamond: Greatest Hits Live", "A Yank In The Raf"]},
                19: {5: ["The Libertine"], 3: ["8 Man", "Boycott", "Searching For Paradise",
                             "Devo: The Complete Truth About De-Evolution", "Jonah: A Veggietales Movie: Bonus Material",
                             "Dragonheart"], 2: ["Nature: Antarctica"]},
                20: {5: ["Zatoichi'S Conspiracy"], 4: ["Seeta Aur Geeta", "Something'S Gotta Give",
                             "Silent Service", "The Weather Underground"], 3: ["Screamers", "My Bloody Valentine"],
                     2: ["Isle Of Man Tt 2004 Review", "What The Hell Do We Know!?"]},
                21: {5: ["The Rise And Fall Of Ecw", "Sesame Street: Elmo'S World: The Street We Live On"],
                     4: ["My Favorite Brunette", "The Bad And The Beautiful"],
                     3: ["By Dawn'S Early Light", "Pitcher And The Pin-Up"],
                     2: ["Ashtanga Yoga: Beginner'S Practice With Nicki Doane"], 1: ["Carandiru"]},
                25: {5: ["Daydream Obsession"], 4: ["7 Seconds"], 2: ["Inspector Morse 31: Death Is Now My Neighbour"],
                     1: ["Character"]},
                36: {5: ["Lord Of The Rings: The Return Of The King: Extended Edition: Bonus Material",
                            "Justice League"], 4: ["Sick"], 3: ["Lilo And Stitch", "Ferngully 2: The Magical Rescue"],
                     2: ["Horror Vision", "Richard Iii"]},
                40: {5: ["Classic Albums: Meat Loaf: Bat Out Of Hell", "The Bonesetter"], "4": ["Strange Relations"],
                     2: ["Spitfire Grill"], 1: ["Class Of Nuke 'Em High 2"]}
                }


userAge = newUsers_list['UserAge']
numOfMovie = newUsers_list['NoOfMoviesToRecommend']
movies = newUsers_list['Movies']


for i in range(7):
    if userAge[i] in list_of_dict.keys():
        recommended_movies = list_of_dict[userAge[i]]
        recommended_movies_list = list(recommended_movies.values())
        l1 = [flat for sublist in recommended_movies_list for flat in sublist]
        n_l1 = l1[:numOfMovie[i]]
        movies[i] = n_l1

    else:
        closest_value = min(list_of_dict.keys(), key=lambda x: abs(x-userAge[i]))
        closest_recommended_movies = list_of_dict[closest_value]
        closest_recommended_movies_list = list(closest_recommended_movies.values())
        l2 = [flat for sublist in closest_recommended_movies_list for flat in sublist]
        n_l2 = l2[:numOfMovie[i]]
        movies[i] = n_l2


newUsers_result = pd.DataFrame.from_dict(newUsers_list)
str_newUser_result = newUsers_result.to_string(index=False)
final_result = str_newUser_result.replace("[", "  ").replace("]", "")
print(final_result)





















