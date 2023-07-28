import streamlit
streamlit.title( 'My  Parents New Healthy Diner' ) 
streamlit.header( 'Breakfast Menu' )
streamlit.text( 'Omega 3 & Blueberry Oatmill' )
streamlit.text( 'Kale Spinach & Rocket Smoothie' )
streamlit.text( 'Hard-Boiled Free Range Egg' )
streamlit.header( ' 🥣Breakfast Favorites' )
streamlit.text( '   🥗Omega 3 & Blueberry Oatmill' )
streamlit.text( '   🐔Kale Spinach & Rocket Smoothie' )
streamlit.text( '   🥑🍞Hard-Boiled Free Range Egg' )
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)


# Display the table on the page.
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)

# # Let's put a pick list here so they can pick the fruit they want to include
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
# Display the table on the page
streamlit.dataframe( fruits_to_show )

# display fruityvice API responce
streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/Watermelon")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
streamlit.text(fruityvice_response)

#streamlit.text(fruityvice_response.json())

# # write your own comment -what does the next line do? 
# fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# # write your own comment - what does this do?
# streamlit.dataframe(fruityvice_normalized)
import snowflake.connector
# my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# my_cur = my_cnx.cursor()
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
# my_data_row = my_cur.fetchone()
# streamlit.text("Hello from Snowflake:")
# streamlit.text(my_data_row)

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
# my_data_row = my_cur.fetchone()
# # streamlit.text("The fruit load list contain")
# # streamlit.text(my_data_row)
# streamlit.header("The fruit load list contain")
# streamlit.dataframe(my_data_row)
my_data_rows = my_cur.fetchall()
# streamlit.text("The fruit load list contain")
# streamlit.text(my_data_row)
streamlit.header("The fruit load list contain")
streamlit.dataframe(my_data_rows)

streamlit.header("Fruityvice Fruit Advice!")
add_my_fruit = streamlit.text_input('What fruit would you like to add?')
streamlit.write('Thanks for adding jack fruit ',  add_my_fruit)
my_cur.execute("insert into fruit_load_list values ('from streamlit')")


