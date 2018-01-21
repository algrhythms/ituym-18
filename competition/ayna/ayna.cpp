#include <iostream>
#include <string>
#include <algorithm>

// #define DEBUG


unsigned int get_score (const std::string &lhs, const std::string &rhs)
{ // dumb version of KMP string search
	unsigned int lsize = lhs.size(), rsize = rhs.size();
	unsigned int i = 0, temp, score = 0;
	unsigned int lpos = lhs.rfind(rhs[0], lsize - 1);

	while (lpos != -1 && lpos + rsize >= lsize) {
		temp = 0;
		for(size_t j = lpos; j < lsize; ++j){
			if(lhs[j] == rhs[i++])
				temp++;
			else{
				temp = 0;
				break;
			}
		}
		i = 0;
		if (temp > score) score = temp;

		if (lpos)
			lpos = lhs.rfind(rhs[0], lpos - 1);
		else
			break;
	}

#ifdef DEBUG
	std::cout << "(get_score:)  lhs=" << lhs << " rhs=" << rhs << " score=" << score << "\n";
#endif /*DEBUG*/
	return score;
}


int get_max_concat (std::string words[], size_t size)
{
	unsigned int **scores = new unsigned int*[size];
	for (size_t i = 0; i < size; ++i)
		scores[i] = new unsigned int[size]();

	// set scores
	size_t i, j;
	for (i = 0; i < size; ++i)
		for (j = i + 1; j < size; ++j)
			scores[i][j] = get_score(words[i], words[j]);

	// get max score
	unsigned int maxScore = 0;
	for (i = 0; i < size; ++i)
	{
		for (j = i + 1; j < size - 1; ++j)
			scores[i + 1][j + 1] += scores[i][j];
		if (scores[i][j] > maxScore)
			maxScore = scores[i][j];
	}
	return maxScore;
}


int main(int argc, char const *argv[])
{
	size_t loopCnt = 0;
	std::cin >> loopCnt;

	std::string *words = new std::string[loopCnt];
	for (size_t i = 0; i < loopCnt; ++i)
		std::cin >> words[i];

	std::sort(words, words + loopCnt);

	std::cout <<  get_max_concat(words, loopCnt) << "\n";

	return 0;
}