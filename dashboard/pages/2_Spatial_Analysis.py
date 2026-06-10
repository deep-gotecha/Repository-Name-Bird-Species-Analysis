import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Spatial Analysis",
    page_icon="🌍",
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

st.title("🌍 Spatial Analysis")

st.markdown("""
Analyze bird observations across habitats,
parks and biodiversity hotspots.
""")

st.markdown("---")

# --------------------------------------------------
# HABITAT DISTRIBUTION
# --------------------------------------------------

st.subheader("Habitat Distribution")

habitat_df = (
    birds_df["Habitat"]
    .value_counts()
    .reset_index()
)

habitat_df.columns = [
    "Habitat",
    "Observations"
]

fig = px.pie(
    habitat_df,
    names="Habitat",
    values="Observations",
    hole=0.4
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# --------------------------------------------------
# ADMIN UNIT COUNTS
# --------------------------------------------------

st.subheader(
    "Observations by Administrative Unit"
)

admin_df = (
    birds_df["Admin_Unit_Code"]
    .value_counts()
    .reset_index()
)

admin_df.columns = [
    "Admin Unit",
    "Observations"
]

fig = px.bar(
    admin_df,
    x="Admin Unit",
    y="Observations",
    text="Observations"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# --------------------------------------------------
# TOP BIODIVERSITY HOTSPOTS
# --------------------------------------------------

st.subheader(
    "Top Biodiversity Hotspots"
)

hotspot_df = (
    birds_df.groupby(
        "Admin_Unit_Code"
    )["Common_Name"]
    .nunique()
    .reset_index()
)

hotspot_df.columns = [
    "Admin Unit",
    "Unique Species"
]

hotspot_df = hotspot_df.sort_values(
    "Unique Species",
    ascending=False
)

fig = px.bar(
    hotspot_df,
    x="Admin Unit",
    y="Unique Species",
    text="Unique Species"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# --------------------------------------------------
# MOST ACTIVE PLOTS
# --------------------------------------------------

st.subheader(
    "Top 15 Most Active Plots"
)

plot_df = (
    birds_df["Plot_Name"]
    .value_counts()
    .head(15)
    .reset_index()
)

plot_df.columns = [
    "Plot",
    "Observations"
]

fig = px.bar(
    plot_df,
    x="Plot",
    y="Observations",
    text="Observations"
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

• Forest habitat contains the highest number of observations.

• ANTI recorded the largest number of bird sightings.

• MONO contains the highest biodiversity.

• Several plots consistently attract bird activity.

• Species richness is distributed across multiple parks.
""")
