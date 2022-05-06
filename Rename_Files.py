# importing module

from pathlib import Path



def Rename_Files_One_Folder(User_Rename_Value, filename):
        global counter
        extenstion = filename.suffix
       
        
        file_new_name = str(User_Rename_Value) +'-'+str(counter) + str(extenstion)
      
         
        filename.rename(Path(filename.parent, file_new_name))
        
        counter+=  1
       
        
        

def Main_Rename_Func(User_Rename_Value, folder_path):
    global counter
    for filename in folder_path.iterdir():
        
        if(filename.stem[0] == '.'):
               continue

        if (filename.is_dir()):
       
          counter = 1000
          Main_Rename_Func(filename.stem, Path(filename))
           
    
        else:   
            Rename_Files_One_Folder(User_Rename_Value, filename)  



# Calling main() function

if __name__ == '__main__':

    counter = 1000
    U_input_Path = input('Enter the path of the folder that contains the files \n'
                              'you wish to rename, \n'
                              ',Example of a path: /Downloads/Old_Images/\n >>> ')
    
    
    
    folder_path = Path(U_input_Path)
   


    User_Rename_Value = input('Enter the name you wish to be for all files\n'
                    'which will be followed with a unique Number\n'
                    'My old Images result (my old images 1)\n\n'
                    '>>> ')


    Main_Rename_Func(User_Rename_Value, folder_path)
    print('DONE')
