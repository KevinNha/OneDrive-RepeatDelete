#This project will automate the process of checking for repetitive files in our 

import os
from send2trash import send2trash

class RepeatDelete():
    def files_in_dir(self, path):
        '''
        Returns a list of files in a given directory
        '''
        os.chdir(path)
        return os.listdir()

    def run(self):
        while True:
            onedrive_path = input("What is the path of your OneDrive contents?")
            if os.path.isdir(onedrive_path) == True:
                break
            else:
                print("Pleasea put in the correct directory."
                continue
                      
        while True:
            photo_path = input("What is the path of your photo folder?")
            if os.path.isdir(photo_path) == True:
                break
            else: 
                print("Please put in the correct directory.")
                continue
        
        files_in_comp, files_in_onedrive, i = self.files_in_dir(photo_path), self.files_in_dir(onedrive_path), 0

        for file in files_in_comp:
            if file in files_in_onedrive:
                send2trash(file)
                i+=1
                
        print(f"Moved {i} files to the recycling bin.")

        while True:
            exit_program = input("Exit program? Yes/No")
            if exit_program.lower() == "yes":
                exit()
            elif exit_program.lower() == "no":
                break
            else:
                continue

app = RepeatDelete()

if __name__ == "__main__":
    while True:
        app.run()
