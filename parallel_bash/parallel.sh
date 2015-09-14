# subshells

# serial:
#sleep 2; echo "hello"
#sleep 1; echo "I'm ben"
#sleep 3; echo "mike"

( sleep 2; echo "hello" ) &
( sleep 1; echo "I'm ben" ) &
( sleep 3; echo "mike" ) &