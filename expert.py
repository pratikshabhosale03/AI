import streamlit as st
from typing import List

locations={
    "pune":[
        "1.tulsibag",
        "2.fc road",
        "3.shaniwarwada",
        "4.friendship garden",
        "5.dagdusheth ganpati",
    ],

    "satara":[
        "1.motichowk",
        "2.ycis",
        "3.rajwada",
        "4.aaaaayurvedic garden",
        "5.ajinkyatara",
    ],
    "kolhapur":[
        "1.rankala",
        "2.mahalaxi temple",
        "3.jotiba temple",
        "4.kanheri math",
    ],
    "mumbai":[
        "1.gate way of india",
        "2.juhu beach",
        "3.csmt",
        "4.taj hotel",
    ],
}

st.header("places in maharashtra")

def respond(input:List[str]):
    destination=input[0].lower()
    if destination in locations:
        st.write("you have choosen {destination.capitalize()}")
        st.write("here are you places ")
        for i in locations[destination]:
            st.write(i)

    else:
        st.write("location not found")

if __name__=="__main__":
    options=st.multiselect(
        'choose the location',
        ["satara","pune","kolhapur","mumbai"],[]
    )

    col1,col2=st.columns([1,0.1])
    with col1:
        ask=st.button("ask")
    with col2:
        quit=st.button("quit")
    if(ask):
        respond(options)
    if(quit):
        st.write("thanks for visiting")

