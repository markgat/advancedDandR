# Surfs Up!
Planning a trip to Hawaii? With this application, we use weather station data to find precipitation trends in Hawaii for analysis.  
![surfs-up.jpeg](Images/surfs-up.png)
## Getting Started
### Installing
1) Git clone the repository to your local machine:
    ````
    $ git clone https://github.com/markgat/advancedDandR.git
    ````
## Running
### Jupiter Notebook
1) Create a terminal within the directory of the local repository, and enter the command ````$ jupyter notebook```` with a "y".
2) When the new page loads, locate ````climate_starter.ipynb```` and open it.
3) From here, you can run the blocks one-by-one by selecting the first block and clicking "Run" on top, for each cell, to see the process of analytics, or selecting "Cells" from the top bar and then "Run All" to see it execute all at once.
4) To shutdown, select "Quit" on Jupyter directory webpage.
### Flask Application
1) To begin, open an editor for ````climate_app.py```` and make sure sqlite database path to ````/Resources/hawaii.sqlite```` is set properly on line 10 based on the OS guidelines:
    ````
    # Unix/Mac - 4 initial slashes in total
    engine = create_engine('sqlite:////absolute/path/to/foo.db')

    # Windows
    engine = create_engine('sqlite:///C:\\path\\to\\foo.db')

    # Windows alternative using raw string
    engine = create_engine(r'sqlite:///C:\path\to\foo.db')
    ````
Removing any ````\```` from the path if there is any whitespace.
2) Next, run the python program "climate_app.py".
3) A URL will be displayed from the returned results,
````
 Running on http://127.0.0.1:5000/
````
Open link to startup web application locally on web browser.  
4) This will launch a local API for the weather data where you can make queries based on the URL extensions described on the homepage for dates 2010-01-01 to 2017-08-23.
5) To close program, close the web page and press Ctrl + C in the terminal 
containing the URL.