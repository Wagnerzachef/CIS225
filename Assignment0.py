import json

def add_values(user_dict, key, values) :   #made to make adding values easy
    if key not in user_dict :
        user_dict[key] = list()
    user_dict[key].extend(values)
    return user_dict

with open('user_dict.txt', 'r') as t:
    new_dict = json.load(t)

#print(new_dict)
user_dict = {}
i = 1
username = input('Enter your first and last name: ')

if username in new_dict:
    print(username, new_dict[username])

else:
    print('You are making a new account. Please follow the following directions')
    while i < 6:
        movie = input('Input title of your favorite movie: ')
        director = input('Input title of the director: ')
        year = input('Input the year it was released: ')
        IMDB = input('Input the IMDB star rating: ')
        rotten = input('Input the Rotten Tomatoes rating: ')
        MPAA = input('Input the MPAA rating: ')
        favorite = 'This is your', i, 'favorite movie: '
        add_values(user_dict, username, [favorite, movie, director, year, IMDB, rotten, MPAA])
        i = i + 1

with open('user_dict.txt', 'a') as f:
    f.write(json.dumps([new_dict, user_dict]))
    
