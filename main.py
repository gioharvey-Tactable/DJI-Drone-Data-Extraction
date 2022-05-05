from extract import retrieveFiles
import platform


if __name__ == "__main__":
    
    platform = platform.platform()
    
    drone_path = "DCIM"
    
    # NOTE: CHANGE the `drive_name`

    if not "mac" in platform and "linux" not in platform: # Windows
        # In my case (for eg C:, D: ...) 
        drive_name = "D" ## Change Here
        
        media_directory = f"{drive_name}:\{drone_path}"
        
    else: # (Mac or Linux)
        drive_name = "Untitled" ## Change Here
        
        media_directory = f"/Volumes/{drive_name}/{drone_path}" # Path to change (Mac)
    
    # retrieveFiles(media_directory)
