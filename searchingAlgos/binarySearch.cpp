
#include <iostream>
#include <vector>

int binarySearch(std::vector<int> arr, int size, int target) {
    int low, high, mid = 0;
    
    //high is initialized with the size of the vector
    high = size-1;

    while (high >= low ){
        //sets mid to the vector's midpoint
        mid = (high + low) / 2;

        
        if (arr[mid] < target){
            low = mid -1;
        }
        else if (arr[mid] > target){
            high = mid - 1;
        }
        else{
            //return mid bc that is our target
            return mid;
        }
    }
    return -1; //if not found

}

int main()
{

    int size; //this is the total length of the array
    int target = 0;;
    int targetIndex =0;

    //user enters desired length of the array
    std::cout << "Please entire the length of the array as an integer: ";
    std::cin >> size;

    std::vector<int> arr(size);

    //this loop allows the user to enter the elements in the vector
    for (int i = 0; i < size; i++) {
        std::cout << "Please enter the element for index " << i << " out of " << size << ": ";
        std::cin >> arr[i];
        std::cout << std::endl;
    }

    for (int i = 0; i < size; i++) {
        std::cout << "You entered: " << arr[i] << " ";
    }

    std::cout << "Enter a target value: ";
    std::cin >> target;

// stores the index of the target value returned from binarySearch function
    targetIndex = binarySearch(arr, size, target);

    if (targetIndex == -1){
        std::cout << target << " was not found\n";
    }
    else{
        std::cout << "Found " << target << " at index " << targetIndex << std::endl;
    }
    

 return 0;

}