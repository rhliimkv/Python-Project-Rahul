#!/usr/bin/env python
# coding: utf-8

# In[45]:


import pandas as pd

file_path = 'imdb_movies.csv'
df = pd.read_csv(file_path)


user_input = input("Enter your preferred movie criteria (e.g., year, rating, genre): ")

if not user_input:
    print("No criteria entered. Please provide at least one criterion.")
else:
    preferences = user_input.split()
    
    valid_criteria = ['year', 'rating', 'genre']
    
    user_preferences = {}
    
    invalid_input = [preference for preference in preferences if preference.lower() not in valid_criteria]
    
    if invalid_input:
        print(f"Invalid criteria: {',' .join(invalid_input)}.Please enter valid criteria.")
    else:
        
        for preference in preferences:
            user_value = input(f"Enter the value for {preference} (Press Enter to skip): ")
            if user_value:
                user_preferences[preference.lower()] = user_value

        if not user_preferences:
            print("No values entered. Please provide values for the selected criteria.")
        else:
            filtered_movies = df
            is_filtered = False
            
            try:

                for key, value in user_preferences.items():
                    if key == 'year':
                        filtered_movies = filtered_movies[filtered_movies['Year'] == value]
                        is_filtered = True
                    elif key == 'rating':
                        filtered_movies = filtered_movies[filtered_movies['Rating'] >= float(value)]
                        is_filtered = True
                    elif key == 'genre':
                        filtered_movies = filtered_movies[filtered_movies['Genre'].str.contains(value, case=False)]
                        is_filtered = True
                            
            except (KeyError, ValueError) as e:
                print("Error: Invalid input or data type. Please provide valid input")

            if is_filtered:
                
                if len(filtered_movies) > 0:
                    print("Here are your movie suggestions:")
                    print(filtered_movies[['Title', 'Year', 'Rating', 'Genre']])
                else:
                    print("No movies found based on your preferences.")
            
            else:
                print("No valid filtering criteria provided. Please enter valid criteria")

