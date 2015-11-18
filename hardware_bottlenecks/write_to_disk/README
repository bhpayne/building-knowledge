== creating disk activity ==

==== reading from disk ====

====== hdparm ======

benchmark disk performance

sudo hdparm -t /dev/sda
—> disk reads about 270 MB/sec

sudo hdparm -T /dev/sda
—> cache reads about 5000 MB/sec

==== writing file to disk ====

====== dd ======

https://www.thomas-krenn.com/en/wiki/Linux_I/O_Performance_Tests_using_dd
"So that I/O performance measurements will not be affected by these caches (temporary memory), the oflag parameter can be used."

time dd if=/dev/zero of=dat.img bs=1024 count=0 seek=1024

time dd if=/dev/urandom of=dat.img bs=1 count=0 seek=$[1024*1024*1024]
—> 1GB takes 2.3 seconds

http://www.stevefortuna.com/check-disk-speed-quickly-and-easily-in-linux/
dd if=/dev/zero of=test bs=1048576 count=2048
--> takes 15 seconds
dd if=test of=/dev/null bs=1048576
--> takes 5 seconds

====== file copy ======

vi file.txt
  hello
  world
  
cp file.txt orig.txt
n=3
for i in {1..$n}; do cat file.txt file.txt > file2.txt && mv file2.txt file.txt; done


== monitoring disk activity ==

sudo iotop

iostat -c

iotop 
--> monitors system-wide activity to and from disk

http://superuser.com/questions/226744/how-do-i-log-file-system-read-writes-by-filename-in-linux

http://www.thattommyhall.com/2011/02/18/iops-linux-iostat/


