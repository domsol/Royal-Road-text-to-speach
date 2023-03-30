import sys
import startUpCheck
import GUI


# main function is the start location of the code
def main():
    """MAIN(), start/end location"""

    print("loading System")
    startUpCheck.startUp()
    GUI.main()
    sys.exit("System TTS finished. End of code.")


if __name__ == "__main__":
    main()
