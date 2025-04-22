import os

def main():
    print("Training started...")
    files = os.listdir('.')
    print("Files in directory:", files)
    print("Training complete.")

if __name__ == "__main__":
    main()
