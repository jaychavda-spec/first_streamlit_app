import pandas
import streamlit

streamlit.title("Fat loss diet for the month of May")
streamlit.header("Find below foods")
streamlit.text("🥣 Breakfast at 09:00 A.M.")
streamlit.text("🥗 Brunch at 11:00 A.M.")
streamlit.text("🥑 Lunch at 02:00 P.M.")
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
streamlit.text("🍞 Dinner at 07:00 P.M.")

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index("Fruit")
streamlit.multiselect("Pick some fruits : ",list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)


