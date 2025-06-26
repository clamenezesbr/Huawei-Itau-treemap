Aqui está a tradução completa para o inglês:

---

# 📊 Huawei - Itaú Project Progress Visualizer

This project aims to **clearly and interactively visualize the progress of activities related to Huawei's cloud migration project with Itaú Bank**. The tool uses structured data from Excel spreadsheets and transforms them into *Treemap* charts, enabling detailed analysis of the progress by project, category, and subcategory.

---

## 🔍 Features

* Treemap visualization with 3 hierarchical levels: Project → Category → Subcategory (or directly Category, if no subcategory exists).
* Colors based on completion percentage, with a gradient from red (0%) to green (100%).
* Block sizes proportional to the weight (%) of each activity.
* Dynamic labels, avoiding unnecessary levels when no subcategory is present.

---

## 💼 Context

This project was developed to support Huawei's *Professional Services & Delivery* team in tracking the progress of the cloud migration project for client Itaú. The tool enables **faster and more strategic decision-making**, based on data updated directly from an Excel spreadsheet.

---

## ⚙️ Technologies Used

* **Python 3.x**
* **Pandas**: for data reading and manipulation.
* **Plotly Express**: for creating the interactive Treemap chart.
* **Excel (.csv)**: as the main source of progress data.

---

## 🧠 How It Works

1. The data is stored in an Excel spreadsheet exported as `.csv` (e.g., `Treemap_info.csv`).
2. The Python script:

   * Loads the data using `pandas`.
   * Implements logic to avoid empty subcategories.
   * Generates a Treemap chart based on weights and completion percentages.
   * Applies a color gradient to indicate progress level.
3. The chart is displayed interactively in the browser.

---

## ▶️ Running the Project

To run the project locally:

```bash
pip install pandas plotly
python visualizador.py
```

Make sure the file `Treemap_info.csv` is in the same directory as the Python script.

---

## 📁 File Structure

```
├── Treemap_info.csv       # Data spreadsheet (exported from Excel)
├── visualizador.py        # Main script for chart generation
└── README.md              # Project documentation
```

---

## 💡 Future Ideas

* 🔧 **Graphical User Interface (GUI)**: Create a simple interface where the user can:

  * Upload their own `.csv` spreadsheet
  * View the generated treemap automatically
  * Adjust settings like color scale, font size, and chart structure

* 🌐 **Web Version (Flask or Streamlit)**: Make the project available as a web application, accessible via browser, facilitating use across different departments of the company.

* 📄 **Export to PDF/PNG**: Allow exporting the chart in static formats for use in presentations and reports.

---

## 👨‍💼 Author

**Gabriel Menezes**
Cloud Intern – Huawei Brazil
[LinkedIn](https://www.linkedin.com/in/gabriel-resende-menezes)

---

![Preview](https://i.ibb.co/rGbPDKkg/Map2.png)
