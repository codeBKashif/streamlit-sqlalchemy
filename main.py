import streamlit as st
from db_connection import Session
from tracking_model import User, user_editor_mapping, add_user
from constants import Gender
import pandas as pd


column_config = {
    "id": None,
    'Gender': st.column_config.SelectboxColumn(options=[gender.value for gender in Gender], width="medium")
}

# Display all users from the database
st.subheader("User List")

if "saved" not in st.session_state:
    st.session_state["saved"] = False

if st.session_state["saved"] == True:
    st.success("Data saved successfully")

users = Session.query(User).all()
user_list = [user.to_dict() for user in users] if len(users) > 0 else pd.DataFrame(columns=user_editor_mapping.keys())

edited_df = st.data_editor(user_list, use_container_width=True, num_rows="dynamic", key="user_list", column_config=column_config)

if st.button("Save Changes"):
    
    for key, value in st.session_state.user_list["edited_rows"].items():    
        user = Session.query(User).get(user_list[int(key)]["id"])
        user.from_dict(value)

    for value in st.session_state.user_list["added_rows"]:
        Session.add(add_user(value))

    for index in st.session_state.user_list["deleted_rows"]:
        Session.query(User).filter(User.id == user_list[index]["id"]).delete()

    Session.commit()

    st.session_state["saved"] = True
    st.rerun()