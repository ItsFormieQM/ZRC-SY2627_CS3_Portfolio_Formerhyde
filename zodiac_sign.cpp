#include <iostream>
#include <string>
using namespace std;

string calc_result(unsigned int calc_birthday);
int main() {
	unsigned int birthday;
	unsigned int buffer;

	cout << "Enter your birthday (Baseline: 1900): ";
	cin >> birthday;

	if (birthday < 1900) {
		cout << "\nAge must be greater than or equal to 1900!";
		return -1;
	}
	
	unsigned int result = (birthday - 1900) % 12;

	cout << "Your Chinese zodiac sign is: " << calc_result(result);
	return 0;
}

string calc_result(unsigned int calc_birthday) {

	switch (calc_birthday) {
		case 0:
			return "Rat";
		case 1:
			return "Ox";
		case 2:
			return "Tiger";
		case 3:
			return "Rabbit";
		case 4:
			return "Dragon";
		case 5:
			return "Snake";
		case 6:
			return "Horse";
		case 7:
			return "Goat";
		case 8:
			return "Monkey";
		case 9:
			return "Rooster";
		case 10:
			return "Dog";
		case 11:
			return "Pig";
		default:
			return "error";
	}
}