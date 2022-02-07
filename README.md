# Mocku for Change

My thesis project explores the use of “mockumentary” genre (audiovisual products that use the language of documentary to tell an invented story) as a new language for science education to engage young students in exploring Climate Change issues. 

I supported 40 high school students in ideating, shooting and producing 7 false documentaries, where fictional climate stories were pictured as if in a real documentary.

My main goal is to understand if this genre can be useful to overcome the “imaginative and cultural failure that lies at the heart of the climate crisis” (Amitav Ghosh - The great derangment) helping students in developing linguistic, argumentative and imaginative skills needed to enhance imagination and the capacity to talk about the contemporary challenge of Climate Change.

# About the project

The project in this repository is meant for analysing and visualising the part of my thesis data related to this research question:
Is the mockumentary genre able to inspire and help students telling about Climate Change main (sub)topics?

Each group of students made a video, for each of those 7 videos I collected two kind of data that are related to this analysis. They are about:

- how many topics have been addressed in the video:
- how much the video is coherent with the mockumentary genre style:

Data are stored in an .xlsx file (more info about the structure of this file will be discussed ahead).

## Topics

Three levels have been taken into consideration for topics: Intention, Reality and Perception. At each of this levels a topic can be "present" or "slightly present".  

## Genre score

To each video I attributed a Genre Score, calculated by this formula:

Genre Score = (2*j_score + 2*e_score + a_score)/5

J_score is the score given by a jury of experts; a_score is the score given by an audience and finally e_score is a score that take into consideration how many of the 5 typycal elements of the genre were used and if each of them was coherent: it is calculaed as: sum(element_use*element_coherence). J_score, a_score and e_score are numbers beetween 0 and 5, element_use and element_coherence are either 0 (topic not used/not coherent) or 1 (udes/coherent).

### The program is divided into the following files:

- In the file [funtions](https://github.com/EmmaDOrto/Mocku_for_change/blob/main/functions.py) I have built the functions that do the main calculations.

- The file [thesis_data](https://github.com/EmmaDOrto/Mocku_for_change/blob/main/thesis_data.xlsx) it's a .xlsx file that is imported in analysis file. It has three different sheets. The first one is called "topics" and contains data about topics addressment for each group. The second and the third, called respectively "lelements" and "score", contain data needed to calculate genre score for each group. 

- In the file [analysis](https://github.com/EmmaDOrto/Mocku_for_change/blob/main/analysis.py) there is the main part of the code, where the data file and function file are imported to perform the data analysis.

- In the file [test](https://github.com/EmmaDOrto/Mocku_for_change/blob/main/test.py) I have tested all the functions in functions file to ensure that they work properly.

- In the repository [testing_files](https://github.com/EmmaDOrto/Mocku_for_change/tree/main/testing_files) there are two files (a .csv and a .xlsx) imported in the test file. They must never be changed.

To show you some results, those are the final dataframe an related plot for the condition "Topic present or slightly present in perception": ![plot_image](https://github.com/EmmaDOrto/Mocku_for_change_data_analisys/blob/main/plot_image.png)