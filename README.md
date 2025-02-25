# CxC 2025 Datathon

Hello everyone! We are QCxC, a group of hackers from Quebec. We participated in the 2025 edition of the CxC datathon, sponsored by Federato.
Here is a demo of our project:
[https://www.youtube.com/watch?v=9-DZIzlyi2g](https://www.youtube.com/watch?v=9-DZIzlyi2g)

## Table of Contents

- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)

---

## Project Overview

Our project is organized into three main parts:

- **Data Analysis:**  
  We process and visualize the Federato dataset to reveal key insights such as the most popular OS device types, event durations, and geographical user distribution.

- **Machine Learning Model:**  
  We build and train a model that predicts user behavior based on personal information and historical mouse tracking data, enabling a more personalized user experience.

- **LLM Chatbot:**  
  We develop an AI chatbot designed to help Federato employees quickly retrieve information in a user-friendly manner, significantly reducing the time and effort required to query databases.

---

## Technologies Used

- **Python:** Data processing, analysis, and model development.
- **Pandas:** Data cleaning and CSV-to-DataFrame conversion.
- **Matplotlib:** Creating visualizations such as charts and graphs.
- **Seaborn:** Enhancing data visualization aesthetics.
- **Numpy:** Efficient data manipulation.
- **Flask API:** Integrating our machine learning model into an API.
- **Tensorflow:** Building and training the machine learning model.
- **React:** Front-end rendering.
- **Next.js:** Building a responsive front-end.
- **Tailwind CSS:** Styling and enhancing the UI.

---
## Getting Started

To set up and run the project locally:

1. **Clone the Repository:**
```bash
   git clone https://github.com/they3ll0w/CxC2025
   cd CxC2025
```
2. **Download Requirements:**
```bash
   pip install -r requirements.txt
   npm install
```

3. **Run APIs:**
```bash
   python llm_api.py
   python model_api.py
```

3. **Start the Development Server:**
```bash
   npm start
```
