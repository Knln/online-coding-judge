awk '{
total = $2 + $3 + $4
divided = total/3
if (divided < 50) {
    variable = "FAIL";
} else if (divided >= 50 && divided <= 80) {
    variable = "B";
} else {
    variable = "A";
}
print $0, ":", variable
}'
