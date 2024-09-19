import streamlit as st
import processes.data_loader as data_loader
import pages.page_home as page_home
import pages.page_club as page_club

@st.cache_data
def load_and_process_data():
    # Load data
    df_player_data = data_loader.get_data()
    return df_player_data


def main():
    df_player_data = load_and_process_data()

    # Define pages using lambda functions to call the page functions at runtime
    pages = {
        "Home": lambda: page_home.get_page(),  # Use lambda to delay the execution
        "Measure Overview": lambda: page_club.get_page(df_player_data),
    }

    # Create a sidebar for navigation with clickable page names
    st.sidebar.title("Navigation")
    selected_page = st.sidebar.radio("", options=list(pages.keys()))

    # Call the selected page function
    pages[selected_page]()


if __name__ == "__main__":
    main()
