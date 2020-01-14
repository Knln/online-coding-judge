read n 
input="$(cat)"
for line in $input
do
    average=$(( line+average ))
done
result=`echo $average/$n | bc -l`
printf "%.3f\n" $result
