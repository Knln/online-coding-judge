read str
if [ "$str" = "Y" ];
then
    echo "YES"
elif [ "$str" = "y" ];
then
    echo "YES"
elif [ "$str" = "N" ];
then
    echo "NO"
elif [ "$str" = "n" ];
then
    echo "NO"
fi
