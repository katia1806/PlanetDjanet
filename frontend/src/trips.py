# trips_page.py
import streamlit as st
from database.database import save_reservation


def show_trips_page():
    st.header("Book your trip")

    with st.form(key="my_form"):
        f_n = st.text_input('First name')
        l_n = st.text_input('Last name')
        phone_number = st.text_input('Phone number')
        email = st.text_input('Email Address')
        number_of_tickets = st.number_input('Number of tickets', step=1, min_value=0, max_value=10)
        group_of = st.multiselect('Group of', ['Children', 'Teenagers', 'Adults', 'Elderly'])

        if st.form_submit_button("Send"):
            # Prepare the data for saving
            reservation_data = {
                "first_name": f_n,
                "last_name": l_n,
                "phone_number": phone_number,
                "email": email,
                "number_of_tickets": number_of_tickets,
                "group_of": group_of
            }

            # Save the data to the database
            save_reservation(reservation_data)
            st.success("Reservation saved successfully!")
            st.balloons()


