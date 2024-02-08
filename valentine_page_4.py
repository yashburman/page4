# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 00:39:02 2024

@author: Sreejit
"""

import streamlit as st

# Page title
st.title("When we first spent Durga puja and Christmas together")

# Image and text side by side
col1, col2 = st.columns(2)

# Image on the left
image_path = "img4.jpeg"  # Replace with the actual path to your image
col1.image(image_path, use_column_width=True, caption="You being absolute hottie")

col2.write("""
Last year, we did it all, and we did it right! We had our first proper Durga Puja where you looked absolutely stunning, and you were magical and a bit naughty (And that's what makes you so perfect). Seeing you in a saree is equivalent to witnessing a piece of art that must have taken a thousand years to perfect (but still comes nowhere near you), and I'm not going to beat around the bush... I have never been as turned on as I was then. 

You teased me so much, knowing full well that I was going crazy. Every moment, I thought about grabbing you, pushing you against the wall, and giving you all my love. To touch and caress you everywhere, pull your hair, bite your neck, tell you how much I love you, show you how much I love you, and make you feel what your love does to me. My heart was racing, it was so tough to keep myself from kissing you. There doesn't go a single night where I don't think of that moment and tell myself how lucky I am.
""")

col3, col4 = st.columns(2)

image_path = "img3.jpeg"  # Replace with the actual path to your image

col3.write("""And then came Christmas, and we went to Park Street Cemetery (where we committed our first sin, 	:smirk:), but let's try to keep this PG-13. This year, I met your friends, and you met mine. We came a bit closer to each other. Although I know I made you upset that day, I want to take this opportunity to let you know that we might not always get to spend a lot of time together, and I wish I could change that, but sadly, I can't.

But I promise you, one day, you'll get so tired of looking at my stoopid face all day, and I still won't leave you alone. I'll annoy you 27x7, and you couldn't stop me. I'll make you breakfast, lunch, and dinner and all the snacks in between. We'll shower together, live, laugh, and cry together. We will be with each other forever and ever.

Love,

I ran out of nick names that you gave me	:sweat_smile:""")
col4.image(image_path, use_column_width=True, caption=" Us being absolute cuties")

st.header("[When we first, well not really first :wink:](https://www.youtube.com/)")