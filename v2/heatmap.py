import plotly.express as px
import pandas as pd

data = {
    
    "Category": [
        "Foundation (97%)", "Foundation (97%)", "Foundation (97%)",
        "Foundation (97%)", "Foundation (97%)", "Foundation (97%)",
        "Foundation (97%)", "Foundation (97%)", "Foundation (97%)",
        "Migration (67%)", "Migration (67%)", "Migration (67%)",
        "O&M, New CRs and Revenue Execution (34%)", "O&M, New CRs and Revenue Execution (34%)",
        "O&M, New CRs and Revenue Execution (34%)", "O&M, New CRs and Revenue Execution (34%)",
        "O&M, New CRs and Revenue Execution (34%)"
    ],

    "Subcategory": [
        "Foundation Building (95.6%)", "Foundation Building (95.6%)", "Foundation Building (95.6%)",
        "Foundation Building (95.6%)", "Foundation Building (95.6%)", "Foundation Building (95.6%)",
        "Security Requirement (95.0%)", "Sandbox Foundation (100.0%)", "Sandbox Test (100.0%)",
        "Migration2 (0%)", "Pilot Migration (90.0%)", "Pilot Migration (90.0%)",
        "Revenue Execution for H1 (10.0%)", "O&M Assurance (80.0%)",
        "New CR (26.7%)", "New CR (26.7%)", "New CR (26.7%)"
    ],

    "Label": [
        "LDZ 100%", "LOG 100%", "CMDB 100%",
        "Automation 98%", "NetWork 100%", "Security 80%",
        "Security Requirement 95%", "Sandbox Foundation 100%", "Sandbox Test 100%",
        "Migration2 0%", "Pilots 100%", "Migration Process 80%",
        "Revenue Execution 10%", "O&M Assurance 80%",
        "AI 10%", "CFTV 10%", "Backup 60%"
    ],

    "Values": [
        3.0,   # LDZ 100%
        3.0,   # LOG 100%
        3.0,   # CMDB 100%

        3.0,   # Automation 98%
        3.0,   # NetWork 100%
        3.0,   # Security 80%

        9.68,  # Security Requirement 95%
        16.13, # Sandbox Foundation 100%
        12.0,  # Sandbox Test 100%

        21.942,  # Migration2 (60% de Migration)
        7.314,   # Pilots (50% de Pilot Migration)
        7.314,   # Migration Process (50% de Pilot Migration)

        29.03, # Revenue Execution 10%
        12.90, # O&M Assurance 80%

        3.23,  # AI 10%
        3.23,  # CFTV 10%
        6.45   # Backup 60%
    ],

    "Conclusion": [
        100,  # LDZ 100%
        100,  # LOG 100%
        100,  # CMDB 100%

        98,   # Automation 98%
        100,  # NetWork 100%
        80,   # Security 80%

        95,   # Security Requirement 95%
        100,  # Sandbox Foundation 100%
        100,  # Sandbox Test 100%

        0,   # Migration2 20%
        100,  # Pilots 100%
        80,   # Migration Process 80%

        10,   # Revenue Execution 10%
        80,   # O&M Assurance 80%

        10,   # AI 10%
        10,   # CFTV 10%
        60    # Backup 60%
    ],

    "Details": [
        "LDZ detail", "LOG detail", "CMDB detail",
        "Automation detail", "NetWork detail", "Security detail",
        "Security Requirement detail", "Sandbox Foundation detail", "Sandbox Test detail",
        "Migration2 detail", "Pilots detail", "Migration detail",
        "Revenue detail", "O&M detail",
        "AI detail", "CFTV detail", "Backup detail"
    ]
}

df = pd.DataFrame(data)

fig = px.treemap(
    df,
    path=["Category", "Subcategory", "Label"],
    values="Values",
    color="Conclusion",
    hover_data=["Details", "Conclusion"],
    color_continuous_scale=['red', 'yellow', 'green'],
    range_color=(0, 100),
    title=""
)

fig.update_layout(
    title_font_size=20,
    margin=dict(t=50, l=25, r=25, b=25),
    annotations=[
        dict(
            x=0.5,
            y=-0.1,
            showarrow=False,
            text="Tamanho = Volume / Cor = Conclusão (%)",
            xref="paper",
            yref="paper",
            font=dict(size=12, color="gray"),
        )
    ]
)

fig.show()
