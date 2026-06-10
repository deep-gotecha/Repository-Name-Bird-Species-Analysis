import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Species Analysis",
    page_icon="🐦",
    layout="wide"
)

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------


@st.cache_data
def load_data():

    df = pd.read_csv(
        "../cleaned_data/birds_cleaned.csv"
    )

    return df


birds_df = load_data()

# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("🐦 Species Analysis")

st.markdown("""
Explore bird species diversity,
abundance and observation characteristics.
""")

st.markdown("---")

# --------------------------------------------------
# KPI SECTION
# --------------------------------------------------

total_species = birds_df["Common_Name"].nunique()

top_species = (
    birds_df["Common_Name"]
    .value_counts()
    .idxmax()
)

top_species_count = (
    birds_df["Common_Name"]
    .value_counts()
    .max()
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Unique Species",
        total_species
    )

with col2:
    st.metric(
        "Top Species",
        top_species
    )

with col3:
    st.metric(
        "Observations",
        top_species_count
    )

st.markdown("---")

# --------------------------------------------------
# TOP 15 SPECIES
# --------------------------------------------------

st.subheader(
    "Top 15 Most Observed Bird Species"
)

species_df = (
    birds_df["Common_Name"]
    .value_counts()
    .head(15)
    .reset_index()
)

species_df.columns = [
    "Species",
    "Observations"
]

fig = px.bar(
    species_df,
    x="Observations",
    y="Species",
    orientation="h",
    text="Observations"
)

fig.update_layout(
    yaxis=dict(
        categoryorder="total ascending"
    )
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# --------------------------------------------------
# SPECIES DIVERSITY BY HABITAT
# --------------------------------------------------

st.subheader(
    "Species Diversity by Habitat"
)

diversity_df = (
    birds_df.groupby("Habitat")
    ["Common_Name"]
    .nunique()
    .reset_index()
)

diversity_df.columns = [
    "Habitat",
    "Unique Species"
]

fig = px.bar(
    diversity_df,
    x="Habitat",
    y="Unique Species",
    text="Unique Species"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# --------------------------------------------------
# SEX DISTRIBUTION
# --------------------------------------------------

st.subheader(
    "Bird Sex Distribution"
)

sex_df = (
    birds_df["Sex"]
    .value_counts()
    .reset_index()
)

sex_df.columns = [
    "Sex",
    "Count"
]

fig = px.pie(
    sex_df,
    names="Sex",
    values="Count",
    hole=0.4
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# --------------------------------------------------
# IDENTIFICATION METHOD
# --------------------------------------------------

st.subheader(
    "Species Identification Methods"
)

method_df = (
    birds_df["ID_Method"]
    .value_counts()
    .reset_index()
)

method_df.columns = [
    "Method",
    "Count"
]

fig = px.bar(
    method_df,
    x="Method",
    y="Count",
    text="Count"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# --------------------------------------------------
# FLYOVER DISTRIBUTION
# --------------------------------------------------

st.subheader(
    "Flyover Observation Distribution"
)

fly_df = (
    birds_df["Flyover_Observed"]
    .value_counts()
    .reset_index()
)

fly_df.columns = [
    "Flyover",
    "Count"
]

fig = px.pie(
    fly_df,
    names="Flyover",
    values="Count",
    hole=0.4
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# --------------------------------------------------
# KEY FINDINGS
# --------------------------------------------------

st.markdown("---")

st.success("""
### Key Findings

• Dataset contains 127 unique bird species.

• Northern Cardinal is the most observed species.

• Forest and Grassland show nearly identical species diversity.

• Most birds were identified through singing.

• Flyover observations are extremely rare.

• Male/Female records are limited compared to unknown categories.
""")
