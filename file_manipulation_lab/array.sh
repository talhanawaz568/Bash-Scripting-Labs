fruits=("apple" "banana" "cherry")
echo "Fruits array: ${fruits[@]}"

for fruit in "${fruits[@]}"; do
    echo "Fruit: $fruit"
done

fruits+=("mango")

echo "Updated Fruits array: ${fruits[@]}"
