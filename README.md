
```markdown
# Mnemonic Saver

Mnemonic Saver is a Python program that helps you generate a list of permutations based on a template with question marks and search for Ethereum addresses associated with those generated mnemonics. This can be useful for recovering lost Ethereum addresses when you have a vague idea of the corresponding mnemonic phrases.

## Usage

### 1. Generating Mnemonics

1. Run the program to generate a list of permutations of Ethereum mnemonics based on your provided word groups.
2. The program will ask you for the first word group (e.g., "johnny ? alex ?") and a second word group file (a list of words saved in a text file, e.g., `wordlist.txt`).
3. It will generate permutations for the question marks and save them in a file named `mnemonic.txt`.

### 2. Searching for a Target Address

1. Run the program to search for a specific Ethereum address in the generated mnemonics.
2. Provide the name of the `mnemonic.txt` file you generated in the previous step.
3. Enter the target Ethereum address you want to search for.
4. Provide the name of the file where the results will be saved.

## Installation

To use this program, you need to have Python installed on your system. You can install the required Python packages by running the following command:

```bash
pip install eth-account termcolor
```

## How to Run

1. Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/mnemonic-saver.git
```

2. Change the working directory to the project folder:

```bash
cd mnemonic-saver
```

3. Follow the usage instructions mentioned above for generating mnemonics and searching for a target address.

## Example

To demonstrate how to use this program, let's consider a hypothetical scenario where you want to recover a lost Ethereum address.

1. Run the program to generate permutations of mnemonics based on the template you remember.
2. Once you have the `mnemonic.txt` file, use it to search for your target Ethereum address.
3. The program will list all generated addresses and indicate if it finds a match with your target address.
