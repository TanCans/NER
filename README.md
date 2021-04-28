### **Named Entity Recognition for extracting Open Source Hardware project characteristics**

- In this repository you can find an application, which introduces a main focus in Named Entity Recognition (NLP or NER).
- The aim is to extract common entities within a text (or webpages).
- For this purpose, the Spacy library is used to train a deep learning model based on neural netrworks to detect entitios from text data.
- To be able to train the model, it will also show how to create a train dataset and label them in order to perform NER.
- This project is designed for the end users or developers, who need to receive the charateristics of OSH projects. 
- The selected characteristics are manufacturing process, machine type, material and dimensions. 
- As a future step, this informations can be linked to the suitable manufacturers for users to find corresponding Makerspace/Fablabs in order to construct their prototypes.

## **CURRENT STATUS**

- Technology status of the project is OTRL 6, which means it is a ready-to-use product and demonstrated in relevant environment.
- Documentation status of the project is ODRL 3, which means it is an early release.
- The next steps are
  - Fullfilling the documentation
  - New use cases
  - Enhancing the algorithm for a better score
- The needed skills are basic python skills and some enthasuiasm.

## **THE PROBLEM**

- There were already a lot of algortihms for Named Entity Recognition, but not for this specific topic with manufacturing characteristics. The algortihm can still be trained with other train data or for other parameters to extract other needed information and enhance the use cases.

## **PRODUCT FEATURES/FUNCTIONS**

- The algorthm uses NER of SpaCy to train the train data with Deep Learning (NN) for the characteristics mentioned. 
- With a web application any kind of text can be given as input, and the output could be received with the classified entities.

## **THE TEAM**

- As a research partner of the Open!Next project, a small team from Fraunhofer IPK has created the solution so as to contribute for OSH.
- Our team has some basic Python skills.

## **ABOUT THE DESIGN**

- We will perform the following: (how is this process with the application?)
  - Create a train dataset from OSH project websites. (Giving example?)
  - Label the dataset with the selected entities using Doccano labeling tool manually.
  - Save the labels in a text file as JSONL.
  - Spacy Neural Network model to train a new statistical model.
  - We will save the model.
  - We will create a Spacy NLP pipeline and use the new model to detect manufacturing entities.


## PROGRAMMING

- Needed softwares are
  - Python Compiler (Python 3.7 or more)
  - Doccano (1.3.0)
- Needed libraries are
  - SpaCy (3.0.5)
  - json
  - Tkinter
  - requets
  - bs4 as Beautiful Soup
  - Pandas
  - Pickle
- Need to download an IDE environmennt on you computer, clone the repository on you IDE, then to run the application, run either runModel_support file one or two 
- Describe here the process of compiling the electronics and what programming is required. 
- Could you include a sketch of your board? Ideally, you also include the source code.

## **INSTRUCTIONS TO RUN THE APPLICATION**
- Copy the URL of the repository
- Open the python IDE which allows to clone github repository, in our case we used pycharm (version?)
-	create a new project and save it
- In the project, go to vcs and click on create git repository (for the ide it may be that you need to install git)
- Instead of vcs, it will show git, under git select clone and paste the url
-	It will ask to login (when private)
-	After cloning the repository, it will open in your ide, you need to create the python environment if it has not happened automaticalyy, and the python compiler for opening application 1 or 2, go from directory to selected app, run the runModel_support 
- The application will start in a new window, you can give your input and see the results

## **INSTRUCTIONS TO MODIFY**

### CREATING A DATASET
- To create a dataset, our team used basic definitions and some open source hardware plattforms. The train dataset is saved as txt to import in doccano later on.

### LABELING THE DATA
-This step is for labeling the entities using Doccano, but if you already have labeled data, you can skip this step and directly go to training the model.
- First step is to install doccano, please follow the [doccano](https://doccano.github.io/doccano/getting-started/) instructions and open the program
- For WIndows installation,
  - `pip install doccano`
  - `doccano`
- Go to http://127.0.0.1:8000/
- Login with username: admin and password:password
<img src="https://user-images.githubusercontent.com/60435723/116371480-bfbeef00-a80b-11eb-8bc1-429b771d1ac5.png" width="400">
- Click create, type in your project name, description and select the sequence labeling project type
- ![image](https://user-images.githubusercontent.com/60435723/116376637-bdab5f00-a810-11eb-817b-8e5f7cef8db9.png)
- After creating project, click on dataset an import your dataset
- Go to Labels and create your labels
- Go back to your imported dataset and click annotate
- The first entity will open, you can select the word/s you want to label and continue untill all your dataset is labeled accordingly
- After finishing the labeling process, click "Export Dataset" as JSONL file format under Actions and save the file

### TRAINING THE MODEL
- First step is to install spacy
- Firstly we read the JSONL file:
```
  import json
  labeled_data = []
  with open(r"project_1_dataset_v4.jsonl", "r", encoding='utf-8') as read_file:
    for line in read_file:
        data = json.loads(line)
        labeled_data.append(data)
  print(labeled_data)
```

- After reading our data, we need to convert the format
 ```
 TRAINING_DATA = []
  for entry in labeled_data:
      entities = []
      for e in entry['labels']:
          entities.append((e[0], e[1],e[2]))
      spacy_entry = (entry['text'], {"entities": entities})
      TRAINING_DATA.append(spacy_entry)
 print(TRAINING_DATA)
```
- Next step is to train the model- We use Deep Learning (NN) and set a dropout rate of 0.3 to prevent overfitting.
```
import spacy
import random
import json
from spacy.tokens import Doc
from spacy.training import Example
nlp = spacy.blank("en")
ner = nlp.create_pipe("ner")
nlp.add_pipe('ner')
for _, annotations in TRAINING_DATA:                    #goes through all the entities are get the name token.label_ one
    for ent in annotations.get("entities"):
        ner.add_label(ent[2])
# Start the training
nlp.begin_training()
# Loop for 40 iterations
for itn in range(40):
    # Shuffle the training data
    random.shuffle(TRAINING_DATA)
    losses = {}
# Batch the examples and iterate over them
    for batch in spacy.util.minibatch(TRAINING_DATA, size=2):
        for text, annotations in batch:
        # create Example
            doc = nlp.make_doc(text)
            example = Example.from_dict(doc, annotations)
            # Update the model
            nlp.update([example], losses=losses, drop=0.3)
            example = Example.from_dict(doc, annotations)
    print(losses)
```
- While training data, you can receive some warnings at first, then the iterations should start and take a few minutes
<img src="https://user-images.githubusercontent.com/60435723/116433904-3a0e6400-a84a-11eb-939c-7070aaa4d3c0.png" width="400">
- After iterations stop, we save the model

```
 nlp.to_disk("./my.model")
```
- Testing the model

```
from spacy import displacy
example = "an example test"
doc = nlp(example)
displacy.render(doc, style='ent')
```

## **POTENTIAL IMPROVEMENTS**

- How do you intend to improve this project?
- What you would do different from the first prototype towards the final product?
- What would you like to achieve with your project in the next year?

## **Include any additional information in the Drive.**

Please include any additional information, files or documentation that you would like us to consider inside the Files section of your Project.

## **If you’re a company or organization:**
- [ ] Talk to your legal department
- [ ] Make a marketing plan for the project
- [ ] Have a person looking after community management (identifying & inviting collaborators, responding to issues, reviewing and merging pull requests)


References used:
1. [Reference 1](https://wikifactory.com/+wikifactory/project-example-template/file/README.md)
2. 
