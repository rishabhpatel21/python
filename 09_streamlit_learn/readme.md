# Streamlit Basics

Streamlit is an open-source app framework for Machine Learning and Data Science projects. It allows you to create interactive web applications easily and quickly using Python.

## Getting Started with Streamlit

### Installation

To get started with Streamlit, you need to have Python installed on your machine. Once you have Python set up, you can install Streamlit using pip:

```bash
pip install streamlit
```

### Running a Streamlit App

Create a new Python file, e.g., `app.py`, and add some code to it. Then, run the app using the Streamlit CLI:

```bash
streamlit run app.py
```

## Basic Functions

Streamlit provides a variety of functions to create interactive elements in your app:

1. **Title and Headers**
    ```python
    st.title('My Streamlit App')
    st.header('Header')
    st.subheader('Subheader')
    ```

2. **Text and Markdown**
    ```python
    st.text('This is some text.')
    st.markdown('**This is markdown text.**')
    ```

3. **Widgets**
    - **Buttons**
        ```python
        if st.button('Say hello'):
            st.write('Hello!')
        ```
    - **Selectbox**
        ```python
        language = st.selectbox('Select a programming language', ['Python', 'R', 'Java', 'C++', 'JavaScript'])
        st.write(f'You selected {language}')
        ```

4. **Displaying Data**
    - **DataFrame**
        ```python
        import pandas as pd
        df = pd.DataFrame({'Column 1': [1, 2, 3], 'Column 2': [4, 5, 6]})
        st.dataframe(df)
        ```
    - **Charts**
        ```python
        st.line_chart(df)
        ```

## Advanced Features

1. **Caching**
    Streamlit provides caching to optimize performance by storing expensive computations.
    ```python
    @st.cache
    def expensive_computation():
        # computation logic
        return result
    ```

2. **Layouts**
    Streamlit supports different layouts using columns and expanders.
    ```python
    col1, col2 = st.columns(2)
    with col1:
        st.write('Column 1')
    with col2:
        st.write('Column 2')

    with st.expander('Expand for more details'):
        st.write('Detailed information here')
    ```

## Conclusion

Streamlit is a powerful tool for building web applications in Python. With its simplicity and ease of use, you can create interactive dashboards and applications for data science projects effectively. For more details, visit the [Streamlit Documentation](https://docs.streamlit.io/).

