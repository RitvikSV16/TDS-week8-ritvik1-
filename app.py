import streamlit as st

def largest_number(a, b, c):
    """
    This function finds the largest among three numbers.
    """
    if (a >= b) and (a >= c):
        return a
    elif (b >= a) and (b >= c):
        return b
    else:
        return c

# Streamlit app
def app():
    st.title('Find the largest number')
    st.write('Enter three numbers below to find the largest among them')
    
    # Input fields for the numbers
    a = st.number_input('Enter first number', value=0, step=1)
    b = st.number_input('Enter second number', value=0, step=1)
    c = st.number_input('Enter third number', value=0, step=1)
    
    if st.button('Find largest'):
        # Call function to find largest number
        result = largest_number(a, b, c)
        # Display result
        st.write('Largest number:', result)

if __name__ == '__main__':
    app()
