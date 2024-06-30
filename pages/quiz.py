import streamlit as st
from levelshtein_distance import levenshtein_distance


def main():
    st.title('Quiz')
    st.divider()
    st.header('Question 2')
    with st.echo():
        options = st.multiselect("Your favorite colors:",
                                 ["Green", "Yellow", "Red", "Blue"],
                                 ["Yellow", "Red"])
        st.write("You selected:", options)

    st.divider()
    st.header('Question 5')
    with st.echo():
        distance = levenshtein_distance('elmets', 'elements')
        st.write('Distance = ', distance)

    st.divider()
    st.header('Question 7')
    with st.echo():
        with st.form("my_form"):
            col1, col2 = st.columns(2)
            f_name = col1.text_input('First Name')
            l_name = col2.text_input('Last Name')
            submitted = st.form_submit_button("Submit")
            if submitted:
                st.write("First Name: ", f_name, " - Last Name:", l_name)

    st.divider()
    st.header('Question 8')
    with st.echo():
        st.file_uploader("Choose files", accept_multiple_files=True)


if __name__ == "__main__":
    main()
