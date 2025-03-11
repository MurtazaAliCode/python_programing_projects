import streamlit as st
import os

def create_file(file_name):
    try:
        with open(file_name, "x") as f:
            st.success(f"{file_name} created successfully.")
    except FileExistsError:
        st.warning(f"File {file_name} already exists.")
    except Exception as e:
        st.error(f"An error occurred while creating the file: {e}")

def view_all_files():
    files = os.listdir()
    if not files:
        st.info("No files found.")
    else:
        st.write("### Files in the directory:")
        for file in files:
            st.write(f"📄 {file}")

def delete_file(file_name):
    try:
        os.remove(file_name)
        st.success(f"{file_name} deleted successfully.")
    except FileNotFoundError:
        st.warning(f"File {file_name} not found.")
    except Exception as e:
        st.error(f"An error occurred while deleting the file: {e}")

def read_file(file_name):
    try:
        with open(file_name, "r") as f:
            content = f.read()
            st.text_area(f"Content of {file_name}:", content, height=200)
    except FileNotFoundError:
        st.warning(f"File {file_name} not found.")
    except Exception as e:
        st.error(f"An error occurred while reading the file: {e}")

def edit_file(file_name, content):
    try:
        with open(file_name, "a") as f:
            f.write(content + "\n")
            st.success(f"Content added to {file_name} successfully.")
    except FileNotFoundError:
        st.warning(f"File {file_name} not found.")
    except Exception as e:
        st.error(f"An error occurred while editing the file: {e}")

# Streamlit UI Design
st.set_page_config(page_title="File Manager", page_icon="📂", layout="centered")
st.markdown(
    """
    <style>
    body {
        background-color: #1E1E2F;
        color: white;
        font-family: Arial, sans-serif;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 18px;
        padding: 10px;
        border-radius: 8px;
    }
    .stTextInput>div>div>input {
        background-color: #282A36;
        color: white;
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("📂 File Management Web App")
option = st.sidebar.radio("Choose an action:", ["Create File", "View All Files", "Delete File", "Read File", "Edit File"])

if option == "Create File":
    file_name = st.text_input("Enter the file name to create:")
    if st.button("Create File") and file_name:
        create_file(file_name)

elif option == "View All Files":
    if st.button("Refresh File List"):
        view_all_files()

elif option == "Delete File":
    file_name = st.text_input("Enter the file name to delete:")
    if st.button("Delete File") and file_name:
        delete_file(file_name)

elif option == "Read File":
    file_name = st.text_input("Enter the file name to read:")
    if st.button("Read File") and file_name:
        read_file(file_name)

elif option == "Edit File":
    file_name = st.text_input("Enter the file name to edit:")
    content = st.text_area("Enter data to add:")
    if st.button("Save Changes") and file_name and content:
        edit_file(file_name, content)

st.sidebar.info("Use this app to manage files interactively.")
