import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

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

#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index( 'Fruit' )
streamlit.dataframe(my_fruit_list)



# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page
streamlit.dataframe( my_fruit_list )

# Let's put a pick list here so they can pick the fruit they want to include 


# Let's put a pick list here so they can pick the fruit they want to include
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
# Display the table on the page
streamlit.dataframe( fruits_to_show )

streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

#import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
# take the json versionof the response and normalize it
# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response())

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
# take the json versionof the response and normalize it
# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)

#import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")

# my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# my_cur = my_cnx.cursor()
my_cur.execute("SELECT *from fruit_load_list")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)


# my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# my_cur = my_cnx.cursor()
# my_cur.execute("SELECT *from fruit_load_list")
my_data_row = my_cur.fetchone()
streamlit.header("Hello from Snowflake:")
streamlit.dataframe(my_data_row)


# my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# my_cur = my_cnx.cursor()
# my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values ('jackfruit')")
# #my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values ('jackfruit')")
# my_cur.execute("SELECT *from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("Hello from Snowflake:")
streamlit.dataframe(my_data_rows) 

my_cur = my_cnx.cursor()

# Execute the query to select data from the 'fruit_load_list' table
my_cur.execute("SELECT * FROM fruit_load_list")

# Fetch one row of data
my_data_row = my_cur.fetchone()

# Display the results
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)

# Get user input for the new fruit
add_my_fruit = streamlit.text_input("Enter the name of the new fruit:")

# Adding a new fruit to the 'fruit_load_list' table if the user provides input
if add_my_fruit:
        insert_query = f"INSERT INTO fruit_load_list VALUES ('{add_my_fruit}')"
        try:
            my_cur.execute(insert_query)
        except snowflake.connector.Error as e:
            streamlit.error(f"Error executing the query: {e}")
        
        # Commit the transaction (required for data to be saved)
        my_cnx.commit()
        
        streamlit.text("New fruit added successfully!")

my_cur.execute("SELECT * FROM fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("Hello from Snowflake:")
streamlit.dataframe(my_data_rows) 
        
# Close the cursor and connection
# my_cur.close()
# my_cnx.close()

# streamlit.write ('Thanks for adding', add_my_fruit)
# my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values ('from streamlit')")


 
