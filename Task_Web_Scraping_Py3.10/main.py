import streamlit as st
import pandas as pd

# from scrape_selenium import Scraper
from scrape_playwright import Scraper
from Compare.compare_playwright_selenium import time_taken

st.set_page_config(page_title="Web Scraper", page_icon="🕷️")
st.title("Web Scraper of - E Maryland Marketplace (EMMA)")


@st.cache_data
def compare(pages):
    return pd.DataFrame(
        data=[time_taken(page) for page in range(1, pages)],
        columns=["Playwright", "Selenium"],
        index=[page for page in range(1, pages)],
    )


st.line_chart(compare(5))


@st.cache_data
def convert_for_download(df):
    return df.to_csv().encode("utf-8")


if "result" not in st.session_state:
    st.session_state.result = pd.DataFrame()

pages = st.number_input("Enter number of pages to scrape:", min_value=1, max_value=400)
scrape = st.button("Scrape")

if scrape:
    scraper = Scraper(
        url="https://emma.maryland.gov/page.aspx/en/rfp/request_browse_public"
    )

    st.session_state.result = scraper.scrape_site(pages)


if st.session_state.get("result") is not None and not st.session_state.result.empty:
    st.write(st.session_state.result)

    with st.form(key="file", border=True):
        file_name = st.text_input("Enter file name:")
        submit = st.form_submit_button("Export to CSV")

    if submit:
        st.session_state["csv"] = convert_for_download(st.session_state.result)

        st.session_state.result.to_excel(
            f"output_files/{file_name}.xlsx",
            index=False,
            sheet_name="EMMA",
            engine="openpyxl",
        )
        st.session_state["ready_download"] = True

    if st.session_state.get("ready_download", False):
        st.write("Your file is ready for download")
        if st.download_button(
            "Download CSV file",
            data=st.session_state.csv,
            file_name=f"{file_name}.csv",
            mime="text/csv",
            icon=":material/download:",
        ):
            st.balloons()
            st.success("Download Successful")
