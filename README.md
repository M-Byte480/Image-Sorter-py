# Picture Sorter
A quick python script to sort pictures into folders based on their creation date, (and keywords in the file name)

Format: `YYYY/MM/filename.jpg`
So there is YYYY > MM > filename.jpa folders

## Usage
1. Clone the repository
2. Run the script with the path to the folder containing the pictures as an argument
3. Arguments: 
    - `main.py <source_folder_root> <destination_folder_root> <optional_arg>`
    - eg: `main.py "C:\Users\user\OneDrive\Phone\all picures" "C:\test" --adv`

if the --a flag is set, it will go to a sub directory function and group the files into a `screenshots/YYYY/MM`, `pictures/YYYY/MM` and `screen_recordings/YYYY/MM` these categories can be changed within the function which retrieves the folder category. 