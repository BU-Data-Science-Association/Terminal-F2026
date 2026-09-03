Professor Gold lost his printed schedule! He has his schedule saved as a csv in this directory, but he lost his reading glasses too so he needs help reading it.

Figure out what he is supposed to be doing from 10-11am today, and write it on the whiteboard (irl, in CDS 164 if you can). 
Also find his 5 notes for your timespan of choosing and write them on the board along with english translations (use google for this)
---
Bash notes (try all of the below)
- you could just cat schedule.csv and read through the csv formatted text. But some better approaches are
- less schedule.csv - less is a text reading app so if a file is really long it won't just brick your terminal. good luck getting out though
- Pipe several things together! "|" is the pipe command which means to use the output from the command on the left as the input to the command on the right
To recreate a really basic version of excel (read-only), look at the schedule with cat schedule.csv | column -s, -t | less -S
- that should nicely format the comma-separated values into columns and stick you right into less
