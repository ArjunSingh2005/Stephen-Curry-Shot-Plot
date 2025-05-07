# Stephen-Curry-Shot-Plot

🏀 Stephen Curry Shot Data Visualization
This project is a comprehensive web-based visualization tool that maps Stephen Curry’s career shot data onto an interactive half-court background. Built using Streamlit, it combines data processing with Python, Pandas, and SQL, and leverages HTML for custom layout enhancements. The goal is to provide an intuitive interface for exploring Curry’s shooting patterns, tendencies, and performance over different seasons and shot types.

📊 Features
Interactive Shot Chart: Displays Curry’s shot locations on a half-court image.

Make vs. Miss Toggle: Filter shots by outcome (make/miss).

Season Filter: View shots by individual year or across his entire career.

Shot Type Filter: Drill down by 3PT, 2PT, layups, floaters, etc.

Dynamic Stats Panel: Updates total shots, shooting percentage, and filtered shot counts in real time.

Clean UI with HTML Customization: Enhanced layout and responsive styling via embedded HTML elements.

Example Data
The shot data should be structured as follows in your CSV file:
Season,X_Loc,Y_Loc,Quarter,Time,Shot Type,Made
2009-2010,33.9,29.9,1st quarter,11:25.0,3-pointer,False
2009-2010,11.8,19.5,1st quarter,9:31.0,2-pointer,True
...

🧱 Tech Stack
Component	Description
Python	Core programming language for backend logic and data processing.
Pandas	Used for reading, filtering, and transforming Curry’s shot data from CSV or SQL.
SQL	Shot data is stored and queried using SQLite/PostgreSQL to support scalable filtering.
Streamlit	Frontend framework to serve the dashboard and handle interactive controls.
Matplotlib	Used for plotting shot coordinates over a half-court background image.
HTML/CSS	Embedded within Streamlit to customize the layout, add styling, and ensure visual clarity.
