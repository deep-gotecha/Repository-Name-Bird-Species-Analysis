import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Environmental Analysis",
    page_icon="🌦️",
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

st.title("🌦️ Environmental Analysis")

st.markdown("""
Explore how environmental conditions influence bird observations.
""")

st.markdown("---")

# --------------------------------------------------
# KPI SECTION
# --------------------------------------------------

avg_temp = round(
    birds_df["Temperature"].mean(),
    1
)

avg_humidity = round(
    birds_df["Humidity"].mean(),
    1
)

most_common_sky = (
    birds_df["Sky"]
    .value_counts()
    .idxmax()
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Average Temperature",
        f"{avg_temp} °C"
    )

with col2:
    st.metric(
        "Average Humidity",
        f"{avg_humidity}%"
    )

with col3:
    st.metric(
        "Most Common Sky",
        most_common_sky
    )

st.markdown("---")

# --------------------------------------------------
# TEMPERATURE DISTRIBUTION
# --------------------------------------------------

st.subheader(
    "Temperature Distribution"
)

fig = px.histogram(
    birds_df,
    x="Temperature",
    nbins=20
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# --------------------------------------------------
# HUMIDITY DISTRIBUTION
# --------------------------------------------------

st.subheader(
    "Humidity Distribution"
)

fig = px.histogram(
    birds_df,
    x="Humidity",
    nbins=20
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# --------------------------------------------------
# TEMPERATURE BY HABITAT
# --------------------------------------------------

st.subheader(
    "Temperature Distribution by Habitat"
)

fig = px.box(
    birds_df,
    x="Habitat",
    y="Temperature",
    color="Habitat"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# --------------------------------------------------
# HUMIDITY BY HABITAT
# --------------------------------------------------

st.subheader(
    "Humidity Distribution by Habitat"
)

fig = px.box(
    birds_df,
    x="Habitat",
    y="Humidity",
    color="Habitat"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# --------------------------------------------------
# SKY CONDITIONS
# --------------------------------------------------

st.subheader(
    "Bird Observations by Sky Condition"
)

sky_df = (
    birds_df["Sky"]
    .value_counts()
    .reset_index()
)

sky_df.columns = [
    "Sky Condition",
    "Count"
]

fig = px.bar(
    sky_df,
    x="Sky Condition",
    y="Count",
    text="Count"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# --------------------------------------------------
# WIND CONDITIONS
# --------------------------------------------------

st.subheader(
    "Bird Observations by Wind Condition"
)

wind_df = (
    birds_df["Wind"]
    .value_counts()
    .reset_index()
)

wind_df.columns = [
    "Wind",
    "Count"
]

fig = px.bar(
    wind_df,
    x="Wind",
    y="Count",
    text="Count"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# --------------------------------------------------
# DISTURBANCE EFFECT
# --------------------------------------------------

st.subheader(
    "Disturbance Impact on Observations"
)

dist_df = (
    birds_df["Disturbance"]
    .value_counts()
    .reset_index()
)

dist_df.columns = [
    "Disturbance",
    "Count"
]

fig = px.bar(
    dist_df,
    x="Disturbance",
    y="Count",
    text="Count"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# --------------------------------------------------
# CORRELATION MATRIX
# --------------------------------------------------

st.subheader(
    "Environmental Correlation Matrix"
)

corr_df = birds_df[
    [
        "Temperature",
        "Humidity",
        "Visit",
        "Year"
    ]
].corr()

fig = px.imshow(
    corr_df,
    text_auto=True,
    aspect="auto",
    color_continuous_scale="RdBu_r"
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

• Temperature is concentrated around 20–25°C.

• Humidity is generally high across observation periods.

• Grassland habitats show wider environmental variation.

• Partly Cloudy and Clear conditions dominate observations.

• Light wind conditions are associated with most observations.

• Temperature and Humidity show a mild negative correlation.
""")
