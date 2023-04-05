import streamlit as st
import time
from solver import numble_solve

st.title("Numble Solver")

st.write("Check out the daily Numble challenge: [https://numble.wtf/](https://numble.wtf/)")

target = st.number_input("Enter target", min_value=100)

def make_grid(cols,rows):
    grid = [0]*cols
    for i in range(cols):
        with st.container():
            grid[i] = st.columns(rows)
    return grid

mygrid = make_grid(2, 3)
num1 = mygrid[0][0].number_input("Enter number 1", min_value=1)
num2 = mygrid[0][1].number_input("Enter number 2", min_value=1)
num3 = mygrid[0][2].number_input("Enter number 3", min_value=1)
num4 = mygrid[1][0].number_input("Enter number 4", min_value=1)
num5 = mygrid[1][1].number_input("Enter number 5", min_value=1)
num6 = mygrid[1][2].number_input("Enter number 6", min_value=1)

if st.button("Solve"):
    start = time.time()
    solution = numble_solve([num1, num2, num3, num4, num5, num6], target)
    end = time.time()
    st.write(f"Solution: {solution}")
    st.write(f"Solved in {end-start:.5f} seconds")