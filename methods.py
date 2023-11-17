import json_lines
import pandas as pd
import matplotlib.pyplot as plt

'''
a function to get a list of articles from the data source with a number as the
parameter
'''
def retrieve_articles(number):

    # the local file name of the data
    file_name = r"Data/aylien-covid-news.jsonl"

    # declare an empty list to hold the articles
    article_list = []

    # open the file
    with open(file_name, "rb") as f:

        # set the reader object
        article_object = json_lines.reader(f)

        # while the number of articles is greater than 0
        while number > 0:

            # assign the next aricle from the dataset
            article = next(article_object)

            # append this item to the article list
            article_list.append(article)

            # decrement the number by 1
            number = number - 1

    # return the article list
    return article_list


# function to extract the necessary data from a list of articles
def extract_data(article_list):

    # list to hold the authors of articles
    author_list = []

    # list to hold the dates the articles were published
    date_list = []

    # string to hold author field
    author = "author"

    # string to hold name field
    name = "name"

    # string to hold published_at field
    published_at = "published_at"

    # list to hold the extracted author names that have 15 or more publications
    extracted_author_list = []

    '''
    list to hold the extracted dates of artciles
    from authors with 15 or more publications
    '''
    extracted_date_list = []

    # loop through the articles in the article_list
    for article in article_list:

        # append the authors of the artciles to the author list
        author_list.append(article[author][name])

        # append the date to the date list
        date_list.append(article[published_at])

    # calling helper function to return unique author list
    unique_author_list_15 = get_unique_author_list_15(author_list)

    # for artciles in the list
    for article in article_list:

        # if the name is in the unique list of > 15
        if article[author][name] in unique_author_list_15:

            # add the name to a new name list
            extracted_author_list.append(article[author][name])

            # add the date to a new published at list
            extracted_date_list.append(article[published_at])

    # create a dataframe for the results
    df = pd.DataFrame({author : extracted_author_list,
    published_at : extracted_date_list})

    # return the data frame
    return df


# helper function to get unique authors with greater than 15 publictions
def get_unique_author_list_15(author_list):

    # list to hold the authors with 15 or more publications
    author_list_15 = []

    # list to hold the unique author names i.e. no duplicates
    unique_author_list_15 = []

    # dictionary to hold the author and a count of their articles
    author_frequency = {}

    # loop over the authors in the list
    for author in author_list:

        # if author is in the dictionary
        if author in author_frequency:

            # increment the author frequency count
            author_frequency[author] += 1

        # otherise
        else:
            # initialise the author frequency count
            author_frequency[author] = 1

    # iterate through the dictionary
    for key, value in author_frequency.items():

        # if the author has more than 15 publictions
        if value >= 15:

            # add value to a new author list
            author_list_15.append(key)

    # create a list of unique names only
    unique_author_list_15 = set(author_list_15)

    # return the unique list of authors with more than 15 publictions
    return unique_author_list_15

# function to return a specific author from a dataframe
def return_search_author(search_author, df):

    # if the author is in the dataframe
    if search_author in df.values:

        # create a new dataframe with this author
        new_df = df[(df['author'] == search_author)]

        # return the data
        return new_df

    # if the author is not in the data frame
    else:

        # print error message
        print('\nAuthor not found')

        new_df = pd.DataFrame()

        # return null
        return new_df


# method to format the data
def format_data(df):

    # define the subplots
    fig, ax = plt.subplots()

    # hide the axes
    fig.patch.set_visible(True)
    ax.axis('off')
    ax.axis('tight')

    # create table
    table = ax.table(cellText=df.values, colLabels=df.columns, loc='center')

    # display table
    plt.show()
