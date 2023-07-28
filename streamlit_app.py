import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError


# import streamlit
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

# import pandas
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



# # display fruityvice API responce
# streamlit.header("Fruityvice Fruit Advice!")
# try:
#   fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
#   if not fruit_choice:
#       streamlit.error('Please select a fruit to get information.')
#   else:
      fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
      fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
      streamlit.dataframe(fruityvice_normalized)
# display fruityvice API responce
streamlit.header("Fruityvice Fruit Advice!")

    
except URLError as e:
    streamlit.error()

# create the repeatable code block  (called a function)
def get_fruityvice_data(tghis_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json()
    return fruitvice_normlized
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
  if not fruit_choice:
      streamlit.error('Please select a fruit to get information.')
  else:
      back_from_function = get_fruitvice_data(fruit_choice)
      streamlit.dataframe(back_from_function)


streamlit.write('The user entered ', fruit_choice)

# import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/Watermelon")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
streamlit.text(fruityvice_response)

#streamlit.text(fruityvice_response.json())

# # write your own comment -what does the next line do? 
# fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# # write your own comment - what does this do?
# streamlit.dataframe(fruityvice_normalized)

streamlit.stop()
# import snowflake.connector
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


