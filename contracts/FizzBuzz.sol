pragma solidity ^0.8.9;

contract FizzBuzz {
    function CheckNumber(uint256 number) public view returns(string memory){
        if(number % 3 == 0 && number % 5 == 0){
            return "Fizz Buzz";
        }
        else if(number % 3 == 0 && number % 5 != 0){
            return "Fizz";
        }
        else if(number % 3 != 0 && number % 5 == 0){
            return "Buzz";
        }
        else{
            return "";
        }
    }
}