# Dashboard_Stocks_Streamlit 📈

link----> https://dashboardstocksapp.streamlit.app/

![image](https://github.com/user-attachments/assets/8ec0063d-4b1f-41c6-9bf2-a302503b0f28)

## Introduction

Streamlit is an open-source app framework that allows you to deploy a web app that can be easily shared via a URL link. You can read more at the following link: https://streamlit.io/.
To create and view your project in real time, you must first follow the steps shown at this URL: https://docs.streamlit.io/get-started/installation/command-line


![image](https://github.com/user-attachments/assets/9ca36297-6e86-4de8-aa5c-f8217dd41a8a)

The main objective of this project is to create a Dashboard that displays the behaviour of certain stocks that you select in the selection panel.
The data used in this project is downloaded in real time using a python library called yfinance, you just need to install it and import it into your project.

## Code explanation

First you need to import the libraries used in this project.

![image](https://github.com/user-attachments/assets/333710d1-e972-4d6c-9ed3-fb9e618a3123)


Then add a sidebar that will have the function of inserting user data.

![image](https://github.com/user-attachments/assets/b879fde6-e212-4d2a-873c-f68919a6b08c)

And it looks like this:

![image](https://github.com/user-attachments/assets/61de4c8b-8223-4fda-9ec7-13eb958fc278)


Download the data

![image](https://github.com/user-attachments/assets/cc958f39-45c6-41a1-a0cf-a1153e789504)

You can calculate whatever you want; in this case, I calculated returns and standard deviations.

![image](https://github.com/user-attachments/assets/47368715-f6eb-4da6-822c-28f22311d4ff)

To create the dashboard you define the number of columns and the % you want them to occupy, in my case are three with a proportion of 15%, 45% and 40%.

![image](https://github.com/user-attachments/assets/41117c24-7a3e-4ef3-acb3-f48f9fef196a)

Each column defines what you want to include there. You can use predefined graphics that are available in streamlit or you can use other graphics from another library and call them with st.write

![image](https://github.com/user-attachments/assets/bf6d90e1-b3db-4934-a443-591c40710538)

## Conclusion

The possibilities are endless, you can let your imagination run wild, you can even implement a time series model to predict stock prices, segment stocks, etc.
This project serves as a reference to be able to quickly execute a dashboard using Python.

