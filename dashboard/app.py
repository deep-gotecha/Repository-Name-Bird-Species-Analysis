import streamlit as st
import pandas as pd
import plotly.express as px

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="Bird Species Dashboard",
    page_icon="🐦",
    layout="wide"
)

# ==================================================
# LOAD DATA
# ==================================================


@st.cache_data
def load_data():

    df = pd.read_csv(
        "../cleaned_data/birds_cleaned.csv"
    )

    return df


df = load_data()

# ==================================================
# SIDEBAR
# ==================================================

st.sidebar.title("🐦 Navigation")

st.sidebar.markdown("""
Bird Species Observation Analysis Dashboard
""")

st.sidebar.markdown("---")

# ==================================================
# FILTERS
# ==================================================

st.sidebar.header("Filters")

habitat_filter = st.sidebar.multiselect(
    "Select Habitat",
    options=df["Habitat"].unique(),
    default=df["Habitat"].unique()
)

admin_filter = st.sidebar.multiselect(
    "Select Admin Unit",
    options=df["Admin_Unit_Code"].unique(),
    default=df["Admin_Unit_Code"].unique()
)

# ==================================================
# FILTER DATA
# ==================================================

filtered_df = df[
    (df["Habitat"].isin(habitat_filter))
    &
    (df["Admin_Unit_Code"].isin(admin_filter))
]

# ==================================================
# HEADER
# ==================================================

st.title("🐦 Bird Species Observation Analysis Dashboard")



st.markdown("""
### National Park Bird Monitoring Program

Interactive dashboard for exploring:

- Temporal Trends
- Spatial Analysis
- Species Diversity
- Environmental Factors
""")

st.markdown("---")

# ==================================================
# KPI SECTION
# ==================================================

total_observations = len(filtered_df)

total_species = filtered_df["Common_Name"].nunique()

forest_obs = len(
    filtered_df[
        filtered_df["Habitat"] == "Forest"
    ]
)

grassland_obs = len(
    filtered_df[
        filtered_df["Habitat"] == "Grassland"
    ]
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Observations",
        f"{total_observations:,}"
    )

with col2:
    st.metric(
        "Unique Species",
        total_species
    )

with col3:
    st.metric(
        "Forest Observations",
        forest_obs
    )

with col4:
    st.metric(
        "Grassland Observations",
        grassland_obs
    )

st.markdown("---")

st.subheader("Quick Statistics")

stats_df = pd.DataFrame({
    "Metric": [
        "Total Observations",
        "Unique Species",
        "Forest Records",
        "Grassland Records"
    ],
    "Value": [
        total_observations,
        total_species,
        forest_obs,
        grassland_obs
    ]
})

st.dataframe(
    stats_df,
    use_container_width=True
)

# ==================================================
# DOWNLOAD DATASET
# ==================================================

csv = filtered_df.to_csv(index=False)

st.download_button(
    label="📥 Download Filtered Dataset",
    data=csv,
    file_name="birds_filtered.csv",
    mime="text/csv"
)

st.markdown("---")

# ==================================================
# CHARTS
# ==================================================

col1, col2 = st.columns(2)

# --------------------------------------------------
# HABITAT DISTRIBUTION
# --------------------------------------------------

with col1:

    st.subheader("Habitat Distribution")

    habitat_df = (
        filtered_df["Habitat"]
        .value_counts()
        .reset_index()
    )

    habitat_df.columns = [
        "Habitat",
        "Count"
    ]

    fig = px.pie(
        habitat_df,
        names="Habitat",
        values="Count",
        hole=0.4
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# --------------------------------------------------
# TOP SPECIES
# --------------------------------------------------

with col2:

    st.subheader("Top 10 Species")

    species_df = (
        filtered_df["Common_Name"]
        .value_counts()
        .head(10)
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
        orientation="h"
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

st.markdown("---")

# ==================================================
# PROJECT SUMMARY
# ==================================================

st.subheader("Project Summary")

st.info(f"""
Dataset contains **{total_observations:,} observations**
covering **{total_species} unique bird species**
across Forest and Grassland habitats.

Use the left sidebar filters to explore:

• Temporal Analysis

• Spatial Analysis

• Species Analysis

• Environmental Analysis
""")

st.subheader("Top Insights")

st.markdown("""
### Key Project Findings

✅ June recorded the highest number of bird observations.

✅ Northern Cardinal was the most frequently observed species.

✅ MONO exhibited the highest biodiversity.

✅ Forest habitat recorded more observations.

✅ Grassland habitat showed nearly identical species diversity.

✅ Bird activity was highest under low-wind and low-disturbance conditions.
""")

# ==================================================
# PROJECT INFORMATION
# ==================================================

st.markdown("---")

st.subheader("Project Information")

st.success("""
### Dataset Information

• Source: National Park Service Bird Monitoring Dataset

• Total Records: 15,372

• Total Species: 127

• Habitats: Forest and Grassland

### Tools Used

• Python

• Pandas

• NumPy

• SQL (SQLite)

• Plotly

• Streamlit
""")

# ==================================================
# FOOTER
# ==================================================

st.markdown("---")

st.markdown(
    """
    <center>
    Built with Python, Pandas, SQL, Plotly and Streamlit
    </center>
    """,
    unsafe_allow_html=True
)
