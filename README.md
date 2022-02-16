# Mocku for Change

My thesis project explores the use of “mockumentary” genre (audiovisual products that use the language of documentary to tell an invented story) as a new language for science education to engage young students in exploring Climate Change issues. 

I supported 40 high school students in ideating, shooting and producing 7 false documentaries, where fictional climate stories were pictured as if in a real documentary.

My main goal is to understand if this genre can be useful to overcome the “imaginative and cultural failure that lies at the heart of the climate crisis” (Amitav Ghosh - The great derangment) helping students in developing linguistic, argumentative and imaginative skills needed to enhance imagination and the capacity to talk about the contemporary challenge of Climate Change.

# About the project

The project in this repository is meant for analysing and visualising the part of my thesis data related to this research question:
Is the mockumentary genre able to inspire and help students telling about Climate Change main (sub)topics?

Each group of students made a video, for each of those 7 videos I collected two types of data that are related to this analysis. They are about:

- how many topics have been addressed in the video,
- how much the video is coherent with the mockumentary genre style.

Data are stored in an .xlsx file (more info about the structure of this file will be discussed ahead).

## Topics

Three levels have been taken into consideration for topics: Intention, Reality and Perception. At each of this levels a topic can be absent, "present" or "slightly present".  

## Genre score

To each video I attributed a Genre Score, calculated by this formula:

Genre Score = (2*j_score + 2*e_score + a_score)/5

J_score is the score given by a jury of experts; a_score is the score given by an audience and finally e_score is a score that take into consideration how many of the 5 typycal elements of the genre were used and if each of them was coherent. It is calculaed as: sum(element_use*element_coherence). J_score, a_score and e_score are numbers beetween 0 and 5, element_use and element_coherence are either 0 (topic not used/not coherent) or 1 (udes/coherent).

### The program is divided into the following files:

- In the file [paths](https://github.com/EmmaDOrto/Mocku_for_change/blob/main/paths.txt) there are the local paths for saving the analysis_results.xlsx file with final dataframes and .png images of plots. It's a .txt file that is imported in analysis file. 

- In the file [funtions](https://github.com/EmmaDOrto/Mocku_for_change/blob/main/functions.py) I have built the functions that do the main calculations.

- The file [thesis_data](https://github.com/EmmaDOrto/Mocku_for_change/blob/main/thesis_data.xlsx) it's a .xlsx file that is imported in analysis file. It has three different sheets. The first one is called "topics" and contains data about topics addressment for each group. The second and the third, called respectively "elements" and "score", contain data needed to calculate genre score for each group. 

- In the file [analysis](https://github.com/EmmaDOrto/Mocku_for_change/blob/main/analysis.py) there is the main part of the code, where the data file and function file are imported. For each group it calculates a group score, then it counts topics that fulfil certain conditions (For example "Topic present in results" or "Topic present or slightly present in perception") and finally it calculates correlation beetween conditions and genre scores and visualizes the related scatter plot.

- In the file [test](https://github.com/EmmaDOrto/Mocku_for_change/blob/main/test.py) I have tested all the functions in functions file to ensure that they work properly.

- In the repository [testing_files](https://github.com/EmmaDOrto/Mocku_for_change/tree/main/testing_files) there are two files (a .csv and a .xlsx) imported in the test file. They must never be changed.

### How to launch the program:

1. First, the user has to choose the local paths to the folders where data and graphs must be saved. They must be wrote in a .txt file in the format of [paths](https://github.com/EmmaDOrto/Mocku_for_change/blob/main/paths.txt)

2. Then, to start the program the user has to launch the file [analysis](https://github.com/EmmaDOrto/Mocku_for_change/blob/main/analysis.py) which imports [thesis_data](https://github.com/EmmaDOrto/Mocku_for_change/blob/main/thesis_data.xlsx) from CLI as first argument and then parameters from [paths](https://github.com/EmmaDOrto/Mocku_for_change/blob/main/paths.txt), that has to be given as second argument. So the user has to launch the analysis file from the command line with the syntax "python analysis.py data.xlsx paths.txt" (in our case, "python analysis.py thesis_data.xlsx paths.txt"). The final analysed dataframes and plot images are saved automatically in the local paths.

To show you some results, those are the final dataframe an related plot for the condition "Topic present or slightly present in perception": 


#### Topic present or slightly present in perception 

| --- | Count |Topic type | Score |
| --- | --- | --- | --- |
G1 | 10 | Solutions/Relationships/Choices/Collectivity/F...  | 1.76 |
G2 | 10 | Reality/Complexity/Solutions/Relationships/Cho...  | 2.75 |
G3 |  7 | Solutions/Collectivity/Future/Possible scenari...  | 2.20 |
G4 | 15 | Reality/Complexity/Circular causality/Data/Cho...  | 3.64 |
G5 | 15 | Reality/Complexity/Solutions/Relationships/Cho...  | 4.15 |
G6 | 12 | Reality/Complexity/Data/Relationships/Choices/...  | 2.95 |
G7 | 12 | Reality/Complexity/Data/Solutions/Relationship...  | 4.25 |


![plot_image](https://github.com/EmmaDOrto/Mocku_for_change/blob/main/images/pres_slipres_perception.png)