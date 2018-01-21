#include <iostream>


int main(){
    int n, temp;
    std::cin >> n;

    int *nums = new int[n];

    for(int i = 0; i < n; ++i){
        std::cin >> temp;
        nums[i] = temp;
    }

    int nOps, l, r, x, sum;
    std::cin >> nOps;
    for(int i = 0; i < nOps; ++i){
        sum = 0;

        std::cin >> temp;
        switch(temp){
        case 1:
            sum = 0;
            std::cin >> l >> r;
            for(int j = l - 1; j < r; ++j)
                sum += nums[j];
            std::cout << sum << "\n";
            break;
        case 2:
            std::cin >> l >> r >> x;
            for(int j = l - 1; j < r; ++j)
                nums[j] |= 1UL << (x - 1);
            break;
        case 3:
            std::cin >> l >> r >> x;
            for(int j = l - 1; j < r; ++j)
                nums[j] &= ~(1UL << (x - 1));
            break;
        default:
            return 1;
        }
    }

    return 0;
}