import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Temporal Analysis",
    page_icon="📅",
    layout="wide"
)

# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------


@st.cache_data
def load_data():

    df = pd.read_csv(
        "../cleaned_data/birds_cleaned.csv"
    )

    df["Date"] = pd.to_datetime(
        df["Date"]
    )

    return df


birds_df = load_data()

# ---------------------------------------------------
# TITLE
# ---------------------------------------------------

st.title("📅 Temporal Analysis")

st.markdown("""
Explore bird observation trends across
months, seasons and survey visits.
""")

st.markdown("---")

# ---------------------------------------------------
# MONTHLY OBSERVATIONS
# ---------------------------------------------------

st.subheader(
    "Monthly Observation Trend"
)

monthly = (
    birds_df
    .groupby("Month_Name")
    .size()
    .reset_index(name="Observations")
)

month_order = [
    "May",
    "June",
    "July"
]

monthly["Month_Name"] = pd.Categorical(
    monthly["Month_Name"],
    categories=month_order,
    ordered=True
)

monthly = monthly.sort_values(
    "Month_Name"
)

fig = px.bar(
    monthly,
    x="Month_Name",
    y="Observations",
    text="Observations"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ---------------------------------------------------
# SEASON DISTRIBUTION
# ---------------------------------------------------

st.subheader(
    "Season Distribution"
)

season_df = (
    birds_df["Season"]
    .value_counts()
    .reset_index()
)

season_df.columns = [
    "Season",
    "Observations"
]

fig = px.pie(
    season_df,
    names="Season",
    values="Observations",
    hole=0.4
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ---------------------------------------------------
# DAILY TREND
# ---------------------------------------------------

st.subheader(
    "Daily Observation Trend"
)

daily = (
    birds_df
    .groupby("Date")
    .size()
    .reset_index(name="Observations")
)

fig = px.line(
    daily,
    x="Date",
    y="Observations",
    markers=True
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ---------------------------------------------------
# VISIT ANALYSIS
# ---------------------------------------------------

st.subheader(
    "Observation Count by Visit"
)

visit_df = (
    birds_df["Visit"]
    .value_counts()
    .sort_index()
    .reset_index()
)

visit_df.columns = [
    "Visit",
    "Observations"
]

fig = px.bar(
    visit_df,
    x="Visit",
    y="Observations",
    text="Observations"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ---------------------------------------------------
# KEY FINDINGS
# ---------------------------------------------------

st.markdown("---")

st.success("""
### Key Findings

• June recorded the highest bird observations.

• Summer observations exceeded Spring observations.

• Observation activity fluctuates across survey dates.

• Visit 1 and Visit 2 recorded the majority of sightings.
""")
