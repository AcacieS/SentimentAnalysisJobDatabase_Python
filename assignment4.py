# 1. Please complete the following:
#   Your First name and Last Name: Acacie Song
#   Your Student ID: 261182381

# 2. Write your program here: 

#Import
import pickle

#Constant
NEW_LINE = "\n"
STOP_WORD_LIST= ["!",".","?",";",NEW_LINE]

#Q A1
def read_text(text_path): 
    """(str: file path)-->(list<str>)
    Return a list of each line in the text of the text_path file
    by ignoring the user pseudonym and add /n at the end of the line. 
    If there isn't any file, it will display "File does not exist."

    >>>read_text("text.txt")
    ["Hello \n", "How are you today? \n",
     "Good I hope! \n", "Ok take care! \n"]
    """
    try:
        fobj = open(text_path,"r")
        word_dict = []

        #Each line
        for line in fobj:
            line = line.strip()
            line_split = line.split(",")

            #Add just the comment of the line.
            word_dict += [line_split[1]+NEW_LINE]
        fobj.close()
        return word_dict

    #if not find file
    except FileNotFoundError:
        print("File does not exist")


#Q A2
def read_pickle(path_to_pkl):
    """(str: pickle file path)-->(dict)
    Return a dictionary of the content in the pickle file.

    >>>read_pickle("sentiment_dictionary.pkl")
    {'POSITIVE': ['great', 'love', 'recommend',
    'laugh', 'happy', 'brilliant'],
    'NEGATIVE': ['terrible', 'awful', 'hideous', 'sad', 'cry', 'bad'],
    'NEUTRAL': ['meh', 'indifferent', 'ignore']}
    """
    fobj = open(path_to_pkl,"rb")
    saved_obj = pickle.load(fobj)
    fobj.close()
    return saved_obj


#Q A3
def sentiment_frequencies(text, dictionary_word):
    """(str, dict<str:str>)-->(dict<str:float>)
    Count the number of words from the category in the text for each categories.
    And this number divided by the number of words in the text.
    Return the frequency for each category in a dictionary.

    >>>text = "i love this movie it is great and the adventure\
         scenes are fun i highly recomend it but the theatre was\
         terrible and there was an awful smell"
    >>>dictionary_word = {'POSITIVE': ['great', 'love', 'recommend',
        'laugh', 'happy', 'brilliant'],
        'NEGATIVE': ['terrible', 'awful', 'hideous', 'sad', 'cry', 'bad'],
        'NEUTRAL': ['meh', 'indifferent', 'ignore']}
    >>>sentiment_frequencies(text, dictionary_word)
    {"POSITIVE": 0.11, "NEGATIVE": 0.07, "NEUTRAL": 0.0}


    >>>text = "i am really happy it is a great day\
         i recommend to laugh to be happy"
    >>>dictionary_word = {'POSITIVE': ['great', 'love', 'recommend',
        'laugh', 'happy', 'brilliant'],
        'NEGATIVE': ['terrible', 'awful', 'hideous', 'sad', 'cry', 'bad'],
        'NEUTRAL': ['meh', 'indifferent', 'ignore']}
    >>>sentiment_frequencies(text, dictionary_word)
    {'POSITIVE': 0.31, 'NEGATIVE': 0.0, 'NEUTRAL': 0.0}


    >>>text = "his daughter is a girl she has a dog it\
         likes to play with cat and several things that the man buy"
    >>>dictionary_word = {"Woman":["she","her","woman","girl",
        "lady","daughter"],
        "Man":["he","his","man","girl","guy","son"],
        "Object/Animal":["it","dog","cat","animal","things"]}
    >>>sentiment_frequencies(text, dictionary_word)
    {'Woman': 0.14, 'Man': 0.14, 'Object/Animal': 0.18}
    """
    #Separate the text into word list
    word_split = text.split()

    dict_frequency={}
    
    #Get pos, neg, neutral: connotation
    for connotation in dictionary_word:
        count = 0
        #Each word in the list
        for word in word_split:
            #Each emotion of the connotation
            for emotion in range(len(dictionary_word[connotation])):
                #Count how many times the word in the list is same as the emotion
                if word == dictionary_word[connotation][emotion]:
                    count+=1

        #To add the frequency in dict: number of emotions
        #from same categorie divided. by length of the text
        if count == 0:
            dict_frequency[connotation]= round(float(0),2)
        else:
            dict_frequency[connotation]=round(float(count/len(word_split)),2)
    return dict_frequency
            

#Q A4
def compute_polarity(dict_frequency):
    """(dict<str:int>)-->str
    Return the category(key) that has the highest frequency, 
    if there are more than one that is same highest,
    return the first highest frequency.
    
    >>>dict_frequency = {"POSITIVE": 0.11, "NEGATIVE": 0.07, "NEUTRAL": 0.0}
    >>>compute_polarity(dict_frequency)
    "POSITIVE"

    >>>dict_frequency = {"POSITIVE": 0.04, "NEGATIVE": 0.22, "NEUTRAL": 0.22}
    >>>compute_polarity(dict_frequency)
    "NEGATIVE"

    >>>dict_frequency = {"WOMAN": 0.0, "MAN": 0.11,
     "ANIMAL": 0.05, "OBJECT": 0.23}
    >>>compute_polarity(dict_frequency)
    "OBJECT"
    """
    frequency = 0
    polarity = ""
    #For each category
    for connotation in dict_frequency:
        #Compare if the frequency of the connotation is higher
        #than the one before than, change it to the higher one.
        if frequency<dict_frequency[connotation]:
            frequency=dict_frequency[connotation]
            polarity=connotation
    return polarity


#Q A5
def analyse_text(text_path, dict_path):
    """ (str: file path, str: pickle file path)-->(list<str>)
    For each line of the text in the text_path file, 
    convert the text to lower case and without pseudonym and ponctuation.
    Return a list of the highest frequency category(connotation) of each line.

    >>>analyse_text("posts.txt","sentiment_dictionary.pkl")
    ["POSITIVE", "NEGATIVE", "NEUTRAL", "POSITIVE"]

    >>>file = open('my_file.txt', 'r')
    >>>print(file.read())
    ALICE, I RECOMMEND YOU THIS MOVIE. IT MAKES ME LAUGH AND CRY SO MUCH!
    person67, I am indifferent about this movie. meh. 
    Kelly, I was really sad. And, they still ignore me.
    >>>analyse_text("my_file.txt","sentiment_dictionary.pkl")
    ['POSITIVE','NEUTRAL','NEGATIVE']

    >>>file = open('my_other_file.txt', 'r')
    >>>print(file.read())
    Amelia, I like the guy there with the dog.
    usern, He is not a good person! She should not likes him.
    friend, His dog is healthy. She likes cat. I don't know?
    >>>p=open('pickle.pkl', 'rb')
    >>>pickle.load(p)
    {WOMAN: ['she','woman','girl','she'],
    MAN: ['guy','he','his','him'],
    NEUTRAL: ['dog','cat','it','I','person']}
    >>>analyse_text("my_other_file.txt","pickle.pkl")
    ['NEUTRAL','MAN','NEUTRAL']

    """
    list_polarity = []
    #Open the text_path to get the list of line in the text.
    word_dict = read_text(text_path)
    dictionary_word = read_pickle(dict_path)

    #Get each line
    for line in word_dict:
        new_word_dict = ""
        #Lower case and Separate into word.
        line = line.lower() 
        line_split = line.split()
        
        #To remove the stop words
        for word in line_split:
            for stop_word in STOP_WORD_LIST: 
                if stop_word in word:
                    word = word.replace(stop_word,"")      
            new_word_dict+=word+" "

        #For frequency 
        dict_frequency = sentiment_frequencies(new_word_dict, dictionary_word)
        list_polarity += [compute_polarity(dict_frequency)]
    return list_polarity             




#PARTIE B
#Q B1
class Company:
    """
    This class represents a Company object

    Instance attributes:
        attr1 (str): The company's name.
        attr2 (SyntaxWarning): The company's location.

    """
    #Attributes of Company
    def __init__(self, name, location):
        """(str, str)-->Company
        Returns a new object of type Company
        with the given name and location.

        >>> company1 = Company("Cycle4Energy","Montreal")
        >>> company1.name
        "Cycle4Energy"
        >>> company1.location
        "Montreal"
        """
        self.name = name
        self.location = location

    #Updated of location
    def update_location(self, new_location):
        """(str)--> NoneType
        Takes a new location and changed the old location
        of that company to the new one.

        >>> company1 = Company("Cycle4Energy","Montreal")
        >>> company1.location
        'Montreal'
        >>> commpany1.update_location("San Francisco")
        >>> company1.location
        'San Francisco'

        >>> company2 = Company("Walmart","New York")
        >>> company2.location
        'New York'
        >>> commpany2.update_location("France")
        >>> company2.location
        'France'

        >>> company3 = Company("YMCA","Westmount")
        >>> company3.location
        'Westmount'
        >>> commpany3.update_location("Centre-ville")
        >>> company3.location
        'Centre-ville'
        """
        self.location = new_location


#Q B2

class JobOffer:
    """
    This class represents a Job Offer object

    Instance attributes:
        attr1 (str): The job offer's title.
        attr2 (Company): The job offer's company information.
        attr3 (str): The job offer's contract.
        attr4 (int): The job offfer's salary.
        attr5 (str): The job offer's description.
    """
    #Attributes of JobOffer
    def __init__(self, title, company, contract, salary, description):
        """
        (str, Company, str, int, str)--> JobOffer
        Returns a new object of type JobOffer
        with the given title, company, contract, salary, description.

        Example:
            >>>cmp1 = Company("Harnham","London")
            >>>about = "Design, implement and optimize fraud software solutions"
            >>>job1 = JobOffer("Fraud Analytics Manager",cmp1,
            "Permanent",120000,about)

            >>>job1.title
            "Fraud Analytics Manager"
            >>>job1.company.name
            "Harnham"
            >>>job1.company.location
            "London"
            >>>job1.contract
            "Permanent"
            >>>job1.salary
            120000
            >>>job1.description
            "Design, implement and optimize fraud software solutions"
        """
        self.title = title
        self.company = company
        self.contract = contract
        self.salary = salary
        self.description = description

    #Update of description
    def update_description(self, new_description):
        """(str)--> NoneType
        Takes a new description and changed the old description
        of that company to the new one.

        Example 1:
            >>>cmp1 = Company("Harnham","London")
            >>>about = "Design, implement and optimize fraud software solutions"
            >>>job1 = JobOffer("Fraud Analytics Manager",cmp1,
            "Permanent",120000,about)

            >>>job1.description
            "Design, implement and optimize fraud software solutions"
            >>>new_about = "Enjoy your job, that’s it!"
            >>>job1.update_description(new_about)
            >>>job1.description
            "Enjoy your job, that’s it!"

        Example 2:
            >>>cmp2 = Company("Walmart","New York")
            >>>about2 = "Working as cashier, knowing how to calculate"
            >>>job2 = JobOffer("Cashier",cmp2,"Permanent",120,about2)

            >>>job2.description
            "Working as cashier, knowing how to calculate"
            >>>new_about2 = "Be a normal person and tolerate others!"
            >>>job2.update_description(new_about2)
            >>>job2.description
            "Be a normal person and tolerate others!"

        Example 3:
            >>>cmp3 = Company("YMCA","Westmount")
            >>>about3 = "Checking if everything is good, cleaning the gym."
            >>>job3 = JobOffer("Cleaner",cmp3,"Permanent",1500,about3)

            >>>job3.description
            "Checking if everything is good, cleaning the gym."
            >>>new_about3 = "Welcome to student also"
            >>>job3.update_description(new_about3)
            >>>job3.description
            "Welcome to student also"

        """
        self.description = new_description

    #How to display JobOffer
    def __str__(self):
        """() --> 
        Return the string of the attributes and assigned value of JobOffer. 
        It configure how it is display by separating each instance attribute
        (includes for the class company name and location) with \n.
        So, it can print per line

        Example 1:
            >>>cmp1 = Company("Harnham","London")
            >>>about = "Design, implement and optimize fraud software solutions"
            >>>job1 = JobOffer("Fraud Analytics Manager",cmp1,
            "Permanent",120000,about)

            >>>str(job1)
            "Title: Fraud Analytics Manager\nCompany: Harnham\n\
            Location: London\nContract: Permanent\nDescription: Design,\
            implement and optimise fraud software solutions\nSalary: 120000"

        Example 2:
            >>>cmp2 = Company("Walmart","New York")
            >>>about2 = "Working as cashier, knowing how to calculate"
            >>>job2 = JobOffer("Cashier",cmp2,"Permanent",120,about2)

            >>>str(job2)
            "Title: Cashier\nCompany: Walmart\n\
            Location: New York\nContract: Permanent\nDescription: Working\
            as cashier, knowing how to calculate\nSalary: 120"

        Example 3:
            >>>cmp3 = Company("YMCA","Westmount")
            >>>about3 = "Checking if everything is good, cleaning the gym."
            >>>job3 = JobOffer("Cleaner",cmp3,"Permanent",1500,about3)

            >>>str(job3)
            "Title: Cleaner\nCompany: YMCA\n\
            Location: Westmount\nContract: Permanent\nDescription: Checking\
            if everything is good, cleaning the gym.\nSalary: 1500"
        """
        
        title = "Title: " + self.title + NEW_LINE
        companyName = "Company: " + self.company.name + NEW_LINE
        company = "Company: " + self.company.name + NEW_LINE
        companyLocation = "Location: " + self.company.location + NEW_LINE
        
        contract = "Contract: " + self.contract + NEW_LINE
        description = "Description: " + self.description + NEW_LINE
        salary = "Salary: " + str(self.salary)
        
        result_text = (title + companyName + companyLocation
        + contract + description + salary)
        return result_text


def build_job_database():
    """()--> NoneType
    It creates two JobOffer objects by asking the user for the information 
    for the instance attributes values of each of the jobOffer.
    It will then ask the user to change the description of the first jobOffer
    which will be updated in the first jobOffer.
    Then, it will print it out 
    the new first JobOffer with the new description.
    """
    print("Welcome to New Job Entry! Let's create our first entry.")
    
    #First offer
    print("PLEASE ENTER REQUESTED DATA FOR OFFER 1")
    title1 = input("Title: ")
    name1 = input("Company: ")
    location1 = input("Location: ")
    contract1 = input("Contract: ")
    description1 = input("Description: ")
    salary1 = int(input("Salary: "))
    
    company1 = Company(name1, location1)
    offer1 = JobOffer(title1, company1, contract1, salary1, description1)

    #Second offer
    print("PLEASE ENTER REQUESTED DATA FOR OFFER 2")
    title2 = input("Title: ")
    name2 = input("Company: ")
    location2 = input("Location: ")
    contract2 = input("Contract: ")
    description2 = input("Description: ")
    salary2 = int(input("Salary: "))

    company2 = Company(name2, location2)
    offer2 = JobOffer(title2, company2, contract2, salary2, description2)

    #Modify first offer description
    print("Employer modified OFFER 1 description!")
    print("PLEASE ENTER THE UPDATED OFFER 1 DESCRIPTION")
    update_description1 = input("Description: ")
    offer1.update_description(update_description1)

    #Redisplay 
    print("Find updated OFFER 1 below:")
    print(offer1)
    
#Fin!!!!! Thanks for your work and help for this course! Have a beautiful end of year! 2024 is coming!






