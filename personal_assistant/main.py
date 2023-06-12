# main.py
from assistant.personal_assistant import PersonalAssistant

def print_menu():
    print("\nWhat can I help you with?")
    print("1. Organize files")
    print("2. Google search")
    print("3. Keyword alerts")
    print("4. Generate a citation")
    print("5. Shorten a URL")
    print("6. Quit")

def print_google_search_menu():
    print("\nChoose a Google search option:")
    print("1. Regular search")
    print("2. Scheduled search")
    print("3. Filtered search")
    print("4. Back to main menu")

def main():
    assistant = PersonalAssistant()

    while True:
        print_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            directory = input("Enter directory to organize: ")
            extensions_input = input("Enter extensions to organize or leave blank to consider all: ")
            extensions = extensions_input.split() if extensions_input else None
            print(f"You are organizing all extensions in the directory {directory}") if (extensions == None) else print(f"You are organizing extensions {extensions} in the directory {directory}")
            decision = input("To confirm type Y else type N: ")
            if (decision.lower() =="y"):
                assistant.organize_files(directory, extensions=extensions) 
            else: 
                continue         

        elif choice == '2':
            while True:
                print_google_search_menu()
                search_choice = input("Choose an option: ")

                if search_choice == '1':
                    query = input("Enter search query: ")
                    assistant.google_search(query)
                elif search_choice == '2':
                    query = input("Enter search query: ")
                    time_of_day = input("Enter time of day for search (24h format HH:MM): ")
                    assistant.schedule_search(time_of_day, query)
                elif search_choice == '3':
                    query = input("Enter search query: ")
                    site = input("Enter site to filter (optional): ")
                    filetype = input("Enter filetype to filter (optional): ")
                    intitle = input("Enter title to filter (optional): ")
                    assistant.filtered_search(query, site=site, filetype=filetype, intitle=intitle)
                elif search_choice == '4':
                    break
                else:
                    print("Invalid choice. Please enter a number from the menu.")
        elif choice == '3':
            url_input = input("Enter URLs to monitor (separate with spaces): ")
            urls = url_input.split()
            keyword = input("Enter keyword to alert on: ")
            output_file = input("Enter name of file to write alerts to: ")
            assistant.start_keyword_alert(urls, keyword, output_file)
        elif choice == '4':
            citation_type = input("Enter the citation type (book, paper, image, video): ")
            citation_format = input("Enter the citation format (mla, apa, chicago, turabian, ieee): ")
            # You would need to gather the appropriate arguments based on the citation type
            # For example, if the citation type is a book, you would ask for the author, title, city, publisher, and year
            args = input("Enter the arguments for the citation, separated by commas: ").split(',')
            citation = assistant.generate_citation(f"cite_{citation_type}_{citation_format}", *args)
            print(f"Here is your citation:\n{citation}")
        elif choice == '5':
            url = input("Enter the URL to shorten: ")
            short_url = assistant.shorten_url(url)
            print(f"Here is your shortened URL: {short_url}")
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please enter a number from the menu.")

if __name__ == '__main__':
    main()

