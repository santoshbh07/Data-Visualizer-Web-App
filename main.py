import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import io

# ---------------------------
# Streamlit App Configuration
# ---------------------------
st.set_page_config(
    page_title="Data Visualizer",
    layout="centered",
    page_icon="📊"
)

# ---------------------------
# Title
# ---------------------------
st.title("📊 Data Visualizer")

# ---------------------------
# File Upload
# ---------------------------
uploaded_file = st.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file is not None:
    # Read file
    try:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
    except Exception as e:
        st.error(f"❌ Error reading file: {e}")
        st.stop()

    # Success message
    st.success(f"✅ Loaded `{uploaded_file.name}` successfully!")

    # ---------------------------
    # Preview and Column Selection
    # ---------------------------
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("🔎 Data Preview")
        st.dataframe(df.head())

    with col2:
        st.subheader("⚙️ Select Columns")

        # Allow user to drop unwanted columns
        unwanted_cols = st.multiselect(
            "Remove unwanted columns:",
            options=df.columns.tolist()
        )
        df = df.drop(columns=unwanted_cols)

        # Update columns list after dropping
        columns = df.columns.tolist()

        # Axis selection
        x_axis = st.selectbox("X-axis", options=["None"] + columns, index=0)
        y_axis = st.selectbox("Y-axis", options=["None"] + columns, index=0)

        # Plot type selection
        plot_list = ["Line Plot", "Bar Chart", "Scatter Plot", "Histogram", "Count Plot"]
        selected_plot = st.selectbox("Select a Plot", options=plot_list)

    # ---------------------------
    # Plotting Section
    # ---------------------------
    if st.button("Generate Plot"):
        fig, ax = plt.subplots(figsize=(7, 5))

        try:
            if selected_plot == "Histogram":
                if x_axis != "None":
                    sns.histplot(x=df[x_axis], ax=ax, kde=True)
                else:
                    st.warning("⚠️ Please select a column for the X-axis.")

            elif selected_plot == "Count Plot":
                if x_axis != "None":
                    sns.countplot(x=df[x_axis], ax=ax)
                else:
                    st.warning("⚠️ Please select a column for the X-axis.")

            else:
                if x_axis != "None" and y_axis != "None":
                    if selected_plot == "Line Plot":
                        sns.lineplot(x=df[x_axis], y=df[y_axis], ax=ax)
                    elif selected_plot == "Bar Chart":
                        sns.barplot(x=df[x_axis], y=df[y_axis], ax=ax)
                    elif selected_plot == "Scatter Plot":
                        sns.scatterplot(x=df[x_axis], y=df[y_axis], ax=ax)
                else:
                    st.warning("⚠️ Please select both X and Y axes for this plot.")

            # Label formatting
            ax.tick_params(axis="x", labelsize=10)
            ax.tick_params(axis="y", labelsize=10)

            # Title & labels
            ax.set_title(f"{selected_plot}", fontsize=14)
            if x_axis != "None":
                ax.set_xlabel(x_axis, fontsize=12)
            if y_axis != "None":
                ax.set_ylabel(y_axis, fontsize=12)

            st.pyplot(fig)
            
            # Save plot to buffer
            buf = io.BytesIO()
            fig.savefig(buf, format="png")
            buf.seek(0)

            # Download button
            st.download_button(
                label="📥 Download Plot",
                data=buf,
                file_name=f"{selected_plot.lower().replace(' ', '_')}.png",
                mime="image/png"
            )

        except Exception as e:
            st.error(f"❌ Error generating plot: {e}")
