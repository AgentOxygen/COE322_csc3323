<p align="center">
  <img src="https://i.pinimg.com/236x/68/3c/6b/683c6b356584e183b1e365e6dcf1c312--unusual-animals-animals-photos.jpg" alt="Catous Birb">
<h1> <p align="center"> Homework 02: Mutants! </p></h1>
<h3> <p align="center"> Created by Cameron Cummins (not the image, just the script) </p></h3>
</p>

## Description of Tools

Included in this repository is a set of tools that will allow you to create mutant animals and store their characteristics in formatted JSON files.
All mutant animals are randomly generated according to Dr. Moreau's specifications:
* A head randomly chosen from this list: snake, bull, lion, raven, bunny
* A body made up of two animals randomly chosen using the petname library
* A random number of arms; must be an even number and between 2-10, inclusive
* A random number of legs; must be a multiple of three and between 3-12, inclusive non-random number of tails that is equal to the sum of arms and legs

These tools are divided into two scripts: **generate_animals.py** and **read_animals.py**

For **generate_animals.py**, useful functions include:
* genAnimal() - generates and returns a dictionary containing the characteristics of a randomly mutated animal according to Dr. Moreau's specifications
* genAnimals() - generates and returns a list of animal dictionaries, length specified
* genAnimalsJSON() - identical to genAnimals(), except it automatically outputs the list to a JSON file and returns nothing

For **read_animals.py**, useful functions include:
* getAnimals() - reads specified JSON file created by genAnimalsJSON() or of similar format to create and return a list animal dictionaries
* printRandomInfo() - reads specified JSON file and randomly selects an animal to output characteristics of to the console
* addName() - generates and returns a string "name" for any given animal dictionary  **New Feature!**

## How to Download
Download this repo using git. It will give you access to my other homeworks, but I'm too lazy to create a new repo just for HW 2.
 ```sh
 git clone https://github.com/AgentOxygen/csc3323_coe332.git
 ```

## How to Build
Contained in `/homework02` is a `Dockerfile` which we will use to build the project. Use the `docker build` command to build:
```sh
cd csc3323_coe332/homework02/
docker build -t username/homework02 .
```
This will build the container and make it locally accessible. Use `docker images` to view the container.

## How to Run
To generate a JSON file populated with mutant animals, run the container with the following and specify a `file_name`
```sh
docker run --rm -v $PWD:/data user/homework02 generate_animals.py "/data/file_name.json"
```
To read a JSON file, run the container with the following and specify the path in `"file_name.json"`
```sh
docker run --rm -v $PWD:/data user/homework02 read_animals.py "/data/file_name.json"
```
## How to Run Unit Tests
To run the unit tests, run the container with the following
```sh
docker run --rm -v $PWD:/data user/homework02 test_read_animals.py
```
