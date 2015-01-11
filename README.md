#Expectation Maximization
This is an implementation of the expectation maximization.

##Usage

###Compilation/Install
```bash
git clone https://github.com/A92hm/multi-armed-bandit.git
```

###Execution
The library code is under the algorithm folder.
But to see how to use the algorithm you can look at the demo.py script.
```bash
python demo.py sample_input/input.csv
```

### Input Data
The input data consists of a CSV file in the following order:
```bash
input_data_value, expectation_of_category_1 , expectation_of_category_2 , ..., expectation_of_category_n
```

##Dependencies
* [Python2.7](https://www.python.org/download/releases/2.7/)
* [Numpy](http://www.numpy.org/)
* [Matplotlib](http://matplotlib.org/) (For graphing)

##Structure
    expectation-maximization
    ├── LICENSE
    ├── demo.py                     - Demo of the algorithm in use
    ├── sample_input
    │   └── input.csv               - Sample input file
    └── algorithm                   - Algorithm implementation
        └── EM.py                   - Expectation Maximization algorithm

##[Potential Bugs](https://github.com/A92hm/expectation-maximization/issues)
##To do
##License
[MIT license](http://opensource.org/licenses/MIT)
