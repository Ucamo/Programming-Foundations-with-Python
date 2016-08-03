import time
import webbrowser


total_breaks =3
break_count=1
print("This program started at: "+time.ctime())
while(break_count<=total_breaks):
    time.sleep(10)
    print("Break number: ",break_count," started at: "+time.ctime())
    webbrowser.open("https://www.youtube.com/watch?v=AEE6oOGYNW0")
    break_count = break_count+1
