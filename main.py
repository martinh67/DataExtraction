# import the modules required for the main method
import time
import pandas as pd
from methods import retrieve_articles, extract_data
from methods import format_data, return_search_author

# start a timer for the program
start = time.time()

# declare the main function
def main():

    # assign the article list to a variable
    article_list = retrieve_articles(10000)

    # extract the data required from the question
    df = extract_data(article_list)

    # create a new dataframe with a specific author
    new_df = return_search_author('Sky Sports', df)

    # if the return is empty
    if new_df.empty:

        # in form the user that no results were generated
        print("\nNo results")

    # otherwise
    else:

        # format the data in a table
        format_data(new_df)


# dunder method to run the main method
if __name__ == "__main__":
    main()

# print timing data for the program
print("\n" + 40*"#")
print(time.time() - start)
print(40*"#" + "\n")
