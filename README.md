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
  - 

- How can the community help? - provide links to the issue board/any suitable page.
- Who are you looking for? In terms of skills needed

## **THE PROBLEM**

- There were already a lot of algortihms for Named Entity Recognition, but not for this specific topic with manufacturing characteristics. The algortihm can still be trained for other parameters to extract other needed information.

## **PRODUCT FEATURES/FUNCTIONS**

- The algorthm uses NER of SpaCy to train the train data with Deep Learning (NN) for the characteristics mentioned. 
- With a web application any kind of text can be given as input, and the output could be received with the classified entities.

## **PROJECT VIABILITY**

- How do you intend to test and measure how effectively your Hardware or Product Design meets the needs or problem you intend to solve?
- What is your plan that will make your Project:
    - economically sustainable
    - scalable business model
    - desirable and accessible to the intended end user
- At what stage is your Project at and what proof do you have about the viability?

## **THE TEAM**

- As a research partner of the Open!Next project, a small team has created the solution so as to contribute for OSH.
- (Names?)
- Who are you? Tell us a little bit about your team members and your background. 
- Our team has some basic Python skills.
- Do you have all the skills covered?
- What skills are you looking for?
- How long have you been working on this project and where?

## **THE BILL OF MATERIALS**

- List the materials and components that were used in this project so far. Where the choice of materials or components was for the purpose of arriving at the first prototype, you can make note of what the Product would *ideally* be made with.
- What was the total cost of all your materials, components and supplies? For one unit or initial batch?

## **THE MANUFACTURING/PRODUCTION/ASSEMBLY**

- What are the general steps for production? (you can copy and paste the general parameters from **[here]( https://github.com/OPEN-NEXT/wp3_pub/blob/master/T3.2/Documentation%20%26%20Guidelines/Production%20parameters.md)**)
- What machines or tools did you use to make your prototype(s)? (3D printer, CNC, laser cutter?)
- Do you know the settings of the machines or tools? (you can copy and paste the parameters from here: **[3D printing parameters](https://github.com/OPEN-NEXT/wp3_pub/blob/master/T3.2/Documentation%20%26%20Guidelines/3D%20Printing%20guideline.md)**)
- What fabrication materials are needed?
- Once manufactured or bought part are there, how does the assembly process look like? - Tip: support with images/vidoes for better understanding


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
- What electronics or programming is needed? 
- Describe here the process of compiling the electronics and what programming is required. 
- Could you include a sketch of your board? Ideally, you also include the source code.

## **ABOUT THE PROTOTYPE**

- How did you prototype your project? Make sure the electronics are added onto the BOM as well
- Do you have videos or photos to show for the different iterations?
- Demonstrate the workflows used and as much about the process of ideation to design to physical prototype. It's a good idea to include the problems you faced and how you fixed it.

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
