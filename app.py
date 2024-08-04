import streamlit as st
import pickle
from PIL import Image

# Function to load the todo list from a file
def load_todo_list():
    try:
        with open('todo_list.pickle', 'rb') as f:
            todo_list = pickle.load(f)
    except FileNotFoundError:
        todo_list = []
    return todo_list

# Function to save the todo list to a file
def save_todo_list(todo_list):
    with open('todo_list.pickle', 'wb') as f:
        pickle.dump(todo_list, f)

# Load the todo list
todo_list = load_todo_list()

# Page layout
st.set_page_config(layout="wide", page_title="My To-Do List", page_icon="📝")

# Load background image
bg_image = Image.open("Designer.png")  # Replace "bg.jpg" with your image file

# Title and background
st.image(bg_image, use_column_width=True)
st.markdown("<h1 style='text-align: center; color: white; font-size: 4rem; font-weight: bold;'>Your Daily To-Do List</h1>", unsafe_allow_html=True)

# Add new item
st.sidebar.header("Add New Task", divider="rainbow")
new_item = st.sidebar.text_input("Enter your task:", placeholder="e.g., Finish report")
if st.sidebar.button("Add Task"):
    todo_list.append(new_item)
    save_todo_list(todo_list)

# Display the todo list
st.header("Your Tasks", anchor="tasks")
col1, col2 = st.columns([1, 1.2])

with col1:
    if todo_list:
        for i, item in enumerate(todo_list):
            st.write(f"{i+1}. {item}")
    else:
        st.info("Your to-do list is empty. Add a new task!")

# Delete an item
with col2:
    if todo_list:
        item_to_delete = st.selectbox("Select item to delete", todo_list, index=0)
        if st.button("Delete Task", use_container_width=True):
            todo_list.remove(item_to_delete)
            save_todo_list(todo_list)
    else:
        st.empty()

# Styling with CSS
st.markdown("""
<style>
body {
    background-color: #f5f5f5;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    margin: 0;
    padding: 0;
}

h1 {
    color: white;
    text-shadow: 2px 2px 4px black;
}

h2 {
    color: #333;
}

.stButton {
    background-color: #282c34;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-weight: bold;
}

.stButton:hover {
    background-color: #4CAF50;
}

.stSidebar {
    background-color: #f8f9fa;
    padding: 20px;
}

.stSidebar h2 {
    color: #333;
    margin-top: 0;
}

.stSidebar input {
    padding: 10px;
    border: 1px solid #ced4da;
    border-radius: 5px;
    width: 100%;
    margin-bottom: 10px;
}

.stSidebar button {
    width: 100%;
}

.stEmpty {
    height: 200px;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 1.5rem;
}

.st-bb {
    background-color: #f8f9fa;
}

.st-bb > .st-bb {
    background-color: white;
}
</style>
""", unsafe_allow_html=True)