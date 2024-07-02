import webbrowser

print("█░█ █▄░█ █░░ █ █▄░█ █▀▀")
print("█▄█ █░▀█ █▄▄ █ █░▀█ ██▄")

author = "MRME | https://github.com/MirRottenMe"
print("\nSupport Monero | 41fPj5qMKU1SJ4mFVKvbMRWskFWNP1xRjapwvpyfDTkJbvESrjR9jpHRegkTkiwoTcLPD5gw6x8ZmGbMEd3CjM9DNqagHDe")
print("\n" + author + "\n" + "A simple tool for increasing views for any service")
print("Before using this software, make sure that the chance of blocking will be small")
print("This tool is only for educational purposes and should not be used for malicious activities")
print("I categorically condemn cheating of views and do not promote this software")
print("\n================================")
print("\nUse this tool at your own risk!")
print("\n================================")
abs = input("\nDo you want to continue? (y/n) : ")
if abs == "y":
    print("\n================================")
    n = input("\nEnter the URL of the video, post, or channel >> ")
    print("\n================================")
    
    if n == "":
        print("\nPlease enter a valid URL")
    else:
        vi = input("\nEnter the number of views >> ")
        vis = int(vi)
        con = 0
        while(vis > con):
            webbrowser.open(n)
            con += 1
            print("View " + str(con) + " of " + str(vis))
print("\n================================")
print("\nThank you for using this tool!")
print("have a nice day bro)")