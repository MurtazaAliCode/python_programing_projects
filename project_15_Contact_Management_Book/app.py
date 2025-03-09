import streamlit as st

# Initialize session state if not already present
if "contacts" not in st.session_state:
    st.session_state.contacts = {}

st.title("📞 Contact Management Book")

menu = ["Create Contact", "View Contact", "Update Contact", "Delete Contact", "Search Contact", "Count Contacts"]
choice = st.sidebar.selectbox("Select an option", menu)

if choice == "Create Contact":
    st.subheader("Create a New Contact")
    name = st.text_input("Enter your name:")
    age = st.number_input("Enter your age:", min_value=1, max_value=120, step=1)
    mobile = st.text_input("Enter your mobile number:")
    if st.button("Add Contact"):
        if name and mobile:
            st.session_state.contacts[name] = {"Age": age, "Mobile": mobile}
            st.success(f"Contact {name} has been created successfully.")
        else:
            st.warning("Please enter valid details.")

elif choice == "View Contact":
    st.subheader("View Contact Details")
    name = st.text_input("Enter the name to view:")
    if st.button("View"):
        if name in st.session_state.contacts:
            contact = st.session_state.contacts[name]
            st.write(f"**Name:** {name}\n**Age:** {contact['Age']}\n**Mobile:** {contact['Mobile']}")
        else:
            st.error("Contact not found!")

elif choice == "Update Contact":
    st.subheader("Update Contact")
    name = st.text_input("Enter the name to update:")
    if st.button("Search Contact"):
        if name in st.session_state.contacts:
            new_name = st.text_input("Enter updated name:", value=name)
            age = st.number_input("Enter updated age:", min_value=1, max_value=120, step=1)
            mobile = st.text_input("Enter updated mobile number:", value=st.session_state.contacts[name]['Mobile'])
            if st.button("Update Contact"):
                st.session_state.contacts.pop(name)
                st.session_state.contacts[new_name] = {"Age": age, "Mobile": mobile}
                st.success(f"Contact {new_name} has been updated successfully.")
        else:
            st.error("Contact not found!")

elif choice == "Delete Contact":
    st.subheader("Delete Contact")
    name = st.text_input("Enter the name to delete:")
    if st.button("Delete Contact"):
        if name in st.session_state.contacts:
            del st.session_state.contacts[name]
            st.success(f"Contact {name} deleted successfully.")
        else:
            st.error("Contact not found!")

elif choice == "Search Contact":
    st.subheader("Search Contact")
    search_name = st.text_input("Enter contact name to search:")
    if st.button("Search"):
        found = False
        for name, contact in st.session_state.contacts.items():
            if search_name.lower() in name.lower():
                st.write(f"**Name:** {name}\n**Age:** {contact['Age']}\n**Mobile:** {contact['Mobile']}")
                found = True
        if not found:
            st.error("Contact not found!")

elif choice == "Count Contacts":
    st.subheader("Total Contacts")
    st.write(f"Total contacts in your contact book: **{len(st.session_state.contacts)}**")
