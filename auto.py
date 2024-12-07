#This script automatically runs all the programs for you. You just need to enter the name of the folder needed to be created and follow the instructions 
import os
import subprocess

# Define paths to your scripts
face_shot_script = "face_shot.py"
train_model_script = "train_model.py"
face_rec_script = "face_rec.py"
dataset_folder = "dataset"

def create_person_folder(person_name):
    # Create a folder inside the 'dataset' folder with the person's name
    person_folder_path = os.path.join(dataset_folder, person_name)
    
    if not os.path.exists(person_folder_path):
        os.makedirs(person_folder_path)
        print(f"Folder created: {person_folder_path}")
    else:
        print(f"Folder already exists: {person_folder_path}")
    
    return person_folder_path

def run_script(script_name):
    # Run a python script using subprocess
    try:
        subprocess.run(['python3', script_name], check=True)
        print(f"{script_name} ran successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_name}: {e}")

def main():
    # Ask the user if they want to enroll or verify
    choice = input("Do you want to (1) enroll a new face or (2) verify an existing face? Enter 1 or 2: ")
    
    if choice == "1":
        # Enroll new face
        person_name = input("Enter the person's name for enrollment: ")
        
        # Create a new folder for the person
        create_person_folder(person_name)
        
        # Run face_shot.py and train_model.py in order
        run_script(face_shot_script)
        run_script(train_model_script)
        
        # Ask if they want to verify the newly enrolled face
        verify_choice = input("Do you want to verify the newly enrolled face? (yes/no): ").lower()
        if verify_choice == "yes":
            run_script(face_rec_script)
        else:
            print("Enrollment complete. Verification skipped.")
    
    elif choice == "2":
        # Verify existing face
        print("Verifying face...")
        
        # Directly run face_rec.py to verify
        run_script(face_rec_script)
    
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()

