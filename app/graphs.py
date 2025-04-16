import streamlit as st
import pandas as pd
import os

data_path = r'C:\Users\Jash\OneDrive\Desktop\Internship-Assignment\data'
data = pd.read_csv(os.path.join(data_path, 'final.csv'))

image_path = r'C:\Users\Jash\OneDrive\Desktop\Internship-Assignment\images'
img_list = ['one.png', 'two.png', 'three.png', 'four.png', 'five.png', 'six.png', 'seven.png', 'eight.png', 'nine.png', 'ten.png']

caption_list = [
    "This is a bar plot of the top 10 most frequent commentators present in the dataset.",
    "This is a line graph of number of comments vs the month, and we can see two spikes, one around November, presumably due to the election, and another near January, possibly due to Trump's ceremony.",
    "This is a bar plot of the comments vs Subreddits, and all but r/Republicans and r/PoliticalDiscussion have an equal weightage in the data.",
    "These are the top commentators for the subreddit r/WorldPolitics.",
    "These are the top commentators for the subreddit r/Republicans.",
    "This is the day-by-day activity of r/Anarchism, the subreddit is most active on mondays and fridays.",
    "This is the same as above for r/Politics, and here the most active day is saturday by a wide margin.",
    "The Distribution of sentiment scores is almost a normal distribution, with almost equal comments being positive and negative, and the median being 0.",
    "Average mean daily sentiment of the data, presumably the days the sentiment was high was during the exit polls, and low during the counting and results. After November, when the number of rows are more, the sentiment is almost 0, which may suggest the stop of the use of bots for propaganda.",
    "This is a wordcloud of the most frequent words, and it is clear that for the both sides, Trump always trump in any discussion, this also suggests that for Americans, the man and his words matter way more than his actions."

]

data = data.drop(columns=['Unnamed: 0.1', 'Unnamed: 0'])

def make_plots(img, caption, num):
    st.header(f"Plot {num}:")
    st.image(img)
    st.subheader(caption)
    st.divider()

st.title("Insights and Plots from Reddit Comments data")

st.divider()
st.header("This is final data after cleaning and preprocessing: ")
st.dataframe(data)
st.divider()

st.header("Plots: ")
for i in range(10):
    make_plots(os.path.join(image_path, img_list[i]), caption_list[i], (i + 1))

st.header("Libraries used for this Project: ")
st.html("<ul>"
"<li><h3>Pandas</h3></li>"
"<li><h3>Matplotlib</h3></li>"
"<li><h3>VaderSentiment</h3></li>"
"<li><h3>CountVectorize</h3></li>"
"<li><h3>wordcloud</h3></li>"
"</ul>")

st.divider()

st.header("Further Improvements possible: ")
st.html("<ul>"
"<li><h3>Comments can be grouped into groups like [Liberals, Centrist, Conservative] using heuristics and NLP.</h3></li>"
"<li><h3>Cosine Similarity can be used to find similar comments, and then similar subreddits from the comments.</h3></li>"
"<li><h3>A fun interactive applet could be an LSTM next word predictor using a top commentator's comments and then asking it to finish sentences beginning with some controversial words and topics.</h3></li>"
"<li><h3>A General more deeper analysis into the dataset and more plotting.</h3></li>"
"</ul>")

st.divider()