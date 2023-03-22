# mongo_transfer
A script that lets you transfer large sums of data to mongodb from a json

I made this because importmongo was really slow for me.
In my experience the time it takes to transfer data slows with the duration of the transfer, for me it went from ~5 seconds per 10 000 transfers 
at the 1st transfer to about ~8 seconds per 10 000 transfers at the ~3 000 000th transfer
