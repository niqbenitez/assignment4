#!/bin/bash

echo "first number:"
read num1

echo "secnd number:"
read num2

if [ "$num1" -gt "$num2" ]; then
  echo "The larger number is: $num1"
elif [ "$num2" -gt "$num1" ]; then
  echo "The larger number is: $num2"
else
  echo "Both numbers are equal: $num1"
fi