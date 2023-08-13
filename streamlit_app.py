# import streamlit
# import pandas
# import requests
# import snowflake.connector
# from urllib.error import URLError

# streamlit.title( 'My  Parents New Healthy Diner' ) 
# streamlit.header( 'Breakfast Menu' )
# streamlit.text( 'Omega 3 & Blueberry Oatmill' )
# streamlit.text( 'Kale Spinach & Rocket Smoothie' )
# streamlit.text( 'Hard-Boiled Free Range Egg' )
# streamlit.header( ' 🥣Breakfast Favorites' )
# streamlit.text( '   🥗Omega 3 & Blueberry Oatmill' )
# streamlit.text( '   🐔Kale Spinach & Rocket Smoothie' )
# streamlit.text( '   🥑🍞Hard-Boiled Free Range Egg' )
# streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# # import pandas

# my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# my_fruit_list = my_fruit_list.set_index( 'Fruit' )
# streamlit.dataframe(my_fruit_list)


# # Let's put a pick list here so they can pick the fruit they want to include 
# streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# # Display the table on the page
# streamlit.dataframe( my_fruit_list )

# # Let's put a pick list here so they can pick the fruit they want to include 


# # Let's put a pick list here so they can pick the fruit they want to include
# fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
# fruits_to_show = my_fruit_list.loc[fruits_selected]
# # Display the table on the page
# # streamlit.dataframe( fruits_to_show )

# # streamlit.header("Fruityvice Fruit Advice!")
# # fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
# # streamlit.write('The user entered ', fruit_choice)
# # streamlit.header("Fruityvice Fruit Advice!")
# # try:
# #     fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
# #     if not fruit_choice:
# #         streamlit.error("Please select a fruit to get information.")
# #     else:
# #         fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
# #         fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# #         streamlit.dataframe(fruityvice_normalized)
# # except URLError as e:
# #     streamlit.error()
# # create a repeatable code block (called a function)
# def get_fruityvice_data(this_fruit_choice):
#     fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
#     fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#     return fruityvice_normalized
# # New section to display fruitvicw API Responce
# streamlit.header("Fruityvice Fruit Advice!")
# try:
#     fruit_choice = streamlit.text_input('What fruit would you like information about?')
#     if not fruit_choice:
#         streamlit.error("Please select a fruit to get information.")
#     else:
#         back_from_function = get_fruityvice_data(fruit_choice)
#         streamlit.dataframe(back_from_function)
# except URLError as e:
#     streamlit.error()
    

# # streamlit.write('The user entered ', fruit_choice)

# # import requests
# # fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
# fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
# # streamlit.text(fruityvice_response)
# # streamlit.text(fruityvice_response.json())
# # take the json version of the response and normalize it
# fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# # streamlit.dataframe(fruityvice_normalized)
# # import snowflake.connector
# my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# # my_cur = my_cnx.cursor()
# # my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
# # my_cur.execute("SELECT *from fruit_load_list")
# # my_data_row = my_cur.fetchone()
# # my_data_rows = my_cur.fetchall()
# # streamlit.text("Hello from Snowflake:")
# # streamlit.text(" The Fruit Load List Contais:")
# # streamlit.header(" The Fruit Load List Contais:")
# # streamlit.text(my_data_row)
# # streamlit.dataframe(my_data_row)

# #===========================
# streamlit.header(" The Fruit Load List Contais:")
# # snowflake related functions
# # def get_fruit_load_list():
# #     with my_cnx.cursor() as my_cur:
# #         my_cur.execute("select * from fruit_load_list")
# #         return my_cur.fetchall()
# # #add a button to load the fruit
# # if streamlit.button('Get Fruit Load List'):
# #     my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#     # my_data_rows = get_fruit_load_list()
# #     streamlit.dataframe(my_data_rows)
# #===========================

# # add_my_fruit = streamlit.text_input("Enter the name of the new fruit:")
# # # fruit_choice = streamlit.text_input('What fruit would you like to add?',)
# # my_cur.execute(f"INSERT INTO fruit_load_list VALUES ('{add_my_fruit}')")
# # # fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
# # fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + add_my_fruit)

# # streamlit.write('Thanks for adding ', add_my_fruit)
# # my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values ('from streamlit')")
# #=============================

# # function and button (2)
# # def insert_row_snowflake(new_fruit):
# #     with my_cnx.cursor() as my_cur:
# #         my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values ('from streamlit')")
# #         return "Thanks for adding" + new_fruit
# # add_my_fruit = streamlit.text_input("What fruit would you like to add?")
# # if streamlit.button ('Add a fruit to list'):
# #     my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# #     back_from_function = insert_row_snowflake(add_my_fruit)
# #     streamlit.dataframe (back_from_function)
# #===========challenge
# # def insert_row_snowflake(new_fruit):
# #     with my_cnx.cursor() as my_cur:
# #         my_cur.execute("insert into fruit_load_list values (%s),(new_fruit,)")
# #         my_cnx.commit()  
# #         return "Thanks for adding" + new_fruit

    
                    
        
# def insert_row_snowflake(new_fruit):
#     with my_cnx.cursor() as my_cur:
#         query = "INSERT INTO fruit_load_list VALUES (%s)"
#         my_cur.execute(query, (new_fruit,))
#         my_cnx.commit()  # Commit the transaction to save changes
#         return "Thanks for adding " + new_fruit

# def add_fruits_to_list():
#     # List of fruits to add
#     fruits_to_add = ["jackfruit", "papaya", "guava", "kiwi"]

#     # Adding fruits to the list in the database
#     for fruit in fruits_to_add:
#         response = insert_row_snowflake(fruit)
#         # print(response)  # Optional: Print the response for each fruit

# # Call the function to add the fruits to the list
# add_fruits_to_list()
# #======================================
# # add a button to load the fruits
# if streamlit.button('get fruit list'):
#     my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#     my_data_rows = get_fruit_load_list()
#     my_cnx.close()
#     streamlit.dataframe(my_data_rows)

# # streamlit.stop()

import streamlit
import snowflake.connector
import pandas
streamlit.title('Zena\'s Amazing Athleisure Catalog')
# connect to snowflake
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
# run a snowflake query and put it all in a var called my_catalog
my_cur.execute("select color_or_style from catalog_for_website")
my_catalog = my_cur.fetchall()
# put the dafta into a dataframe
df = pandas.DataFrame(my_catalog)
# temp write the dataframe to the page so I Can see what I am working with
# streamlit.write(df)
# put the first column into a list
color_list = df[0].values.tolist()
# print(color_list)
# Let's put a pick list here so they can pick the color
option = streamlit.selectbox('Pick a sweatsuit color or style:', list(color_list))
# We'll build the image caption now, since we can
product_caption = 'Our warm, comfortable, ' + option + ' sweatsuit!'
# use the option selected to go back and get all the info from the database

my_cur.execute("select direct_url, price, size_list, upsell_product_desc from catalog_for_website where
color_or_style = '" + option + "';")
df2 = my_cur.fetchone()
streamlit.image(
df2[0],
width=400,
caption= product_caption
)
streamlit.write('Price: ', df2[1])
streamlit.write('Sizes Available: ',df2[2])
streamlit.write(df2[3])







