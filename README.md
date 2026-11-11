# Python Chilla: Python for Data Science

Code, notebooks, datasets and assignments from the 40-day **Python Chilla** (Jan 2022), a free online Python for data science course run by [Codanics](https://codanics.com/) with [Scholarship Network Pakistan](https://www.facebook.com/groups/scholarships.pk/) and taught by **Dr. Muhammad Ammar Tufail**.

I took the course and kept everything here, from my first line of Python to the machine learning assignments. I've since organized it so anyone can work through it on their own. You don't need any coding background to start.

- Course videos (Urdu/Hindi): [YouTube playlist](https://www.youtube.com/watch?v=QvPekMN4F0w&list=PL9XvIvvVL50HVsu-Ao8NBr0UJSO8O6lBI)
- Maintained by: [Ali Nawaz](https://aliktk.github.io/alinawaz.github.io/) ([Google Scholar](https://scholar.google.com.br/citations?hl=en&user=oFzPPSMAAAAJ), [ResearchGate](https://www.researchgate.net/profile/Ali-Nawaz-14))

## Who this is for

Students, researchers and anyone from a non-CS background who wants to load real data, explore it, plot it for a report or paper, and train basic ML models. Most examples use small local datasets such as course survey data, Titanic, salary data and FAO crop production for Pakistan and India.

## How to go through it

| Step | Folder | What's in it |
|---|---|---|
| 1 | [`Python_programming/`](Python_programming) | Your first line of code, operators, strings, variables, input, if/else, functions, loops, imports, error handling, indexing, data structures |
| 2 | [`graphs/`](graphs), [`Python_programming/`](Python_programming) (16–23) | Bar, line and box plots, seaborn, plotly, analysis of the course's own student data |
| 3 | [`numpy/`](numpy), [`pandas/`](pandas) | Arrays, DataFrames, cleaning, wrangling, exploratory data analysis |
| 4 | [`machine_learning/`](machine_learning) | Linear and polynomial regression, logistic regression, KNN, decision trees, random forest, Naive Bayes, SVM, k-means, a first neural network in Keras |
| 5 | [`opencv_with_python/`](opencv_with_python) | Image basics with OpenCV |
| 6 | [`assignments/`](assignments), [`projects/`](projects) | Weekly assignments with solutions, plus small projects |

Datasets are in [`data/`](data).

## Running the notebooks

**No install:** open any `.ipynb` file on GitHub and click "Open in Colab", or upload it to [Google Colab](https://colab.research.google.com/).

**On your laptop:**

```bash
git clone https://github.com/Aliktk/Python_Chilla.git
cd Python_Chilla
conda create -n python-chilla python=3.11
conda activate python-chilla
pip install numpy pandas matplotlib seaborn plotly scikit-learn opencv-python jupyter
jupyter notebook
```

Some notebooks were written in 2022 against older library versions. If one breaks, open an issue or a PR.

## Contributing

Fixes, clearer explanations and updated notebooks are welcome. Open an issue or a pull request.

## License

Code and notebooks are under the [Apache 2.0 License](LICENSE). Course content and videos belong to Codanics and Dr. Muhammad Ammar Tufail. Please credit them if you reuse this material.
