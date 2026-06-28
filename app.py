import matplotlib.pyplot as plt
import streamlit as st

#create data/list
interventions = [
    "Influenza vaccination", "Prenatal care", "Chlorination",
    "Smoking cessation advice", "Cholesterol screening", "Helmet promotion",
    "H.I.V./AIDS treatment", "Hypertension drugs", "Airplane safety",
    "Heart disease screening", "Kidney transplants", "Fire prevention",
    "Heart transplants", "Pneumonia vaccines", "Breast cancer screening",
    "Smoke detectors", "Neonatal intensive care", "Toxin control",
    "Seatbelts and car seats", "Cervical cancer screening", "Medicaid",
    "Colorectal screening", "Highway improvement", "Speed limits",
    "Construction safety", "Leukemia treatment", "Heart bypass surgery",
    "Flammability standards", "Vehicle inspection", "Cholesterol treatment",
    "Pesticide control", "Intensive care", "Disaster preparedness",
    "Asbestos control", "School bus safety", "Arsenic control",
]

#the cost is not an exact amount, I estimated it by looking at the figure
costs = [
    5, 8, 12, 15, 18, 22, 28, 35, 40, 45, 52, 58, 62, 68, 75,
    80, 85, 95, 105, 115, 180, 195, 210, 235, 255, 275, 310,
    365, 410, 520, 580, 680, 720, 830, 845, 850
]

#set colors of the bar graphs
colors = ["#f28e2b" if n == "Medicaid" else "#e0e0e0" for n in interventions]

#plot
plt.rcParams["font.family"] = "Arial"
plt.figure(figsize=(9, 13))
plt.barh(interventions, costs, color=colors, zorder=3)

#ax object, we can access this object for customization of the graph
ax = plt.gca()

#title
plt.title("Cost to save a year of life with...", loc='left', pad=35, x=-0.25, fontsize=14, fontweight="bold")

#x axis ticks on top and bottom
plt.tick_params(top=True, bottom=True, labeltop=True, labelbottom=True)
tick_positions = [200, 400, 600, 800]
tick_labels = ["$200k", "$400k", "$600k", "$800k"]
plt.xticks(tick_positions, tick_labels)
plt.tick_params(axis='x', length=0)

#creating intervention header
ax.text(-0.14, 1.0, "INTERVENTION", transform=ax.transAxes, fontsize=9)

#creating the y spines
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["left"].set_visible(True)
ax.spines["left"].set_color("#555555")
ax.spines["left"].set_linewidth(1.5)
ax.spines["left"].set_bounds(-0.35, 35.3)

#highlighting medicaid
plt.text(192, interventions.index("Medicaid"), "about $180,000", va="center", fontsize=9)

#add the source
plt.figtext(-0.055, 0.07, "Source: Angela Wyse and Bruce D. Meyer, including analysis of prior intervention cost research. Values are \nmeasured in 2019 dollars. By The New York Times.",
            fontsize=7.5, color="gray", ha='left')

plt.gca().set_ylim(-0.5, len(interventions) + 0.5)

#add the gridlines
plt.gca().xaxis.grid(True, color='#f0f0f0', linestyle='-', linewidth=1, zorder=1)

#display in streamlit
fig = plt.gcf()
st.pyplot(fig)
