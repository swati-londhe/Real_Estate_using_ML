import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Recommend Apartments")

# Function to load a pickle file with pandas read_pickle for compatibility
def load_pickle_file(filename):
    try:
        data = pd.read_pickle(filename)
        return data
    except FileNotFoundError:
        st.error(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        st.error(f"Error loading '{filename}': {e}")
    return None

# Load location data and similarity matrices
location_df = load_pickle_file('location_distance.pkl')
cosine_sim1 = load_pickle_file('cosine_sim1.pkl')
cosine_sim2 = load_pickle_file('cosine_sim2.pkl')
cosine_sim3 = load_pickle_file('cosine_sim3.pkl')

# Stop if any file failed to load
if location_df is None or cosine_sim1 is None or cosine_sim2 is None or cosine_sim3 is None:
    st.stop()

# Ensure location_df is a DataFrame with a valid index
if not isinstance(location_df, pd.DataFrame) or location_df.index.empty:
    st.error("Error: 'location_distance.pkl' does not contain a valid DataFrame with an index.")
    st.stop()

# Recommender function with similarity scores
def recommend_properties_with_scores(property_name, top_n=5):
    cosine_sim_matrix = 0.5 * cosine_sim1 + 0.8 * cosine_sim2 + 1 * cosine_sim3

    # Get similarity scores for the selected property
    try:
        sim_scores = list(enumerate(cosine_sim_matrix[location_df.index.get_loc(property_name)]))
    except KeyError:
        st.error("Error: Selected property not found in location data.")
        return pd.DataFrame()

    # Sort and retrieve top recommendations
    sorted_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    top_indices = [i[0] for i in sorted_scores[1:top_n + 1]]
    top_scores = [i[1] for i in sorted_scores[1:top_n + 1]]
    top_properties = location_df.index[top_indices].tolist()

    recommendations_df = pd.DataFrame({
        'PropertyName': [str(name) for name in top_properties],
        'SimilarityScore': [float(score) for score in top_scores]
    })

    return recommendations_df

# Streamlit Interface
st.title('Select Location and Radius')

# Dropdown for location selection
selected_location = st.selectbox('Location', sorted(location_df.columns.to_list()))

# Input for radius
radius = st.number_input('Radius in Kms', min_value=1, value=5)

if st.button('Search'):
    # Filter locations within the specified radius
    result_ser = location_df[location_df[selected_location] < radius * 1000][selected_location].sort_values()
    for key, value in result_ser.items():
        st.text(f"{key} {round(value / 1000, 2)} kms")

# Recommendation section
st.title('Recommend Apartments')
selected_apartment = st.selectbox('Select an Apartment', sorted(location_df.index.to_list()))

if st.button('Recommend'):
    recommendation_df = recommend_properties_with_scores(selected_apartment)

    if recommendation_df.empty:
        st.warning("No recommendations found for the selected apartment.")
    else:
        # Debugging: Show the DataFrame structure before displaying
        st.write("Recommendation DataFrame structure:")
        st.write(recommendation_df)


