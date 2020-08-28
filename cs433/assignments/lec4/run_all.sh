for f in *.py; 
do 
    printf "\n$f :\n"; 
    python3 $f; 
    printf "\n--------\n"; 
done
