# Multilingual-Fake-Word-Generator
A multilingual fake word generator + deployed API on Heroku.

## How to run
The main part of the project is the 'word_generator.py' program. Simply:
1. clone the repository on a local directory
2. install the required modules from requirements.txt
3. edit the 'word_generator.py' file in the main section to call the generate_word() function with the arguments of your choice
4. run the program with your python3 interpreter of choice

The program should either raise an exception or return a freshly generated fake word.

## How to run 2
The program is also deployed on heroku using Python's FastAPI framework. 

Is is accessible via the following URL: (https://fake-word-generator.herokuapp.com/)

Currently, there is no content on the home directory, so add a /<language> at the end of the url to generate a fake word in one of six supported languages: 'french', 'german', 'italian', 'spanish', 'english-us','english-uk'

Example Link: (https://fake-word-generator.herokuapp.com/english-uk)

A few optional parameters can also be passed in the form of url query strings; 'min_len' and 'max_len' can be used to specify a range of lengths for our word and 'start_letter' can be used to specify a starting letter for the word.

Example Link: (https://fake-word-generator.herokuapp.com/italian?max_len=8&min_len=8&start_letter=g)

The link above will generate an italian-sounding fake word starting with the letter 'g' with a length of 8 (since the minimum and maximum length are both set to 8).

The API returns a JSON response with 4 fields: 'word', 'error', 'language', and 'length'. Below is a sample response from the API for the request in the above link:
```
{
"word": "Ganotore",
"error": null,
"language": "italian",
"length": 8
}
```

## How does it work?
In order to immitate the features of a language, this program takes a statistical approach where it analyzes a long list of words from a languages and draws a table of letter sucession frequency. For instance, in US english, the letter 'e' has about a 9.61% probability to be following by an 'n', or a 4.11% probability to be followed by an 'a'.

Drawing this table of letter succession frequencies is the purpose of the 'frequency_table_generator.py' program. It takes a language as an argument and looks for the corresponding list of words in the "./base words/" subfolder. After analyzing the words from the file and making the necessary computations, it stores its results in a Pandas datafram that it exports as an Excel file in the "./counts/" subfolder.

'word_generator.py' load back the data from the excel file for the corresponding language in the "./counts/" subfolder and generates a word letter by letter following the succession probabilities until it reaches an end.

### A few key notes
- This project is largely based on an idea detailed in a video by french science education Youtuber David Louapre. [Link to the video](https://www.youtube.com/watch?v=YsR7r2378j0)
- The quality of the words generated will vary depending on the language, the starting character, and the length of the words. In most cases, a large fraction of the words generated will not give a convincing result. Try refreshing your the page or re-sending your request to keep generating new fake words until you find a covincing one.
