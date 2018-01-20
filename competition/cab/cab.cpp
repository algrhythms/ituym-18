#include <iostream>

//#define DEBUG

int main(){
    int n, temp;
    std::cin >> n;

    int *nums = new int[n]();

    for(int i = 0; i < n; ++i){
        std::cin >> temp;
        nums[i] = temp;
    }

    int nOps, l, r, x, **ops;
    std::cin >> nOps;
    ops = new int*[nOps];
    for(int i = 0; i < nOps; ++i){
        ops[i] = new int[4]();
        std::cin >> temp;

        if(temp == 1){
            std::cin >> l >> r;
            ops[i][0] = temp;
            ops[i][1] = l;
            ops[i][2] = r;
        }
        else{
            std::cin >> l >> r >> x;
            #ifdef DEBUG
            std::cout << temp << " " << l << " " << r << " " << x << "\n";
            #endif
            ops[i][0] = temp;
            ops[i][1] = l;
            ops[i][2] = r;
            ops[i][3] = x - 1;
        }
        #ifdef DEBUG
        std::cout << ops[i][0] << " " <<  ops[i][1] << " " << ops[i][2] << " " << ops[i][3] << "\n";
        #endif
    }

    int sum;
    unsigned long setMask = 0UL, clearMask = ~(0UL);
    for(int i = 0; i < nOps; ++i){
        switch(ops[i][0]){
            case 1:
                sum = 0;
                for(int j = ops[i][1] - 1; j < ops[i][2]; ++j)
                    sum += nums[j];
                std::cout << sum << "\n";
                break;
            case 2:
                for(int j = ops[i][1] - 1; j < ops[i][2]; ++j)
                    nums[j] |= 1UL << ops[i][3];
                break;
            case 3:
                for(int j = ops[i][1] - 1; j < ops[i][2]; ++j)
                    nums[j] &= ~(1UL << ops[i][3]);
                break;
            default:
                return 1;
        }
        #ifdef DEBUG
        for(int j = 0; j < n; ++j)
            std::cout << nums[j] << " ";
        std::cout << "\n";
        #endif
    }

    return 0;
}