import itertools
import os
from eth_account import Account
from termcolor import colored
import sys

def generate_permutations(word, length):
    permutations = list(itertools.permutations(word, length))
    return [' '.join(p) for p in permutations]

def replace_question_marks(word, replacements):
    results = []
    for replacement in replacements:
        replaced_word = word
        for r in replacement:
            replaced_word = replaced_word.replace('?', r, 1)
        results.append(replaced_word)
    return results

# First code block used to generate a mnemonic
first_word_group = input("Enter the first word group (example: johnny ? alex ?): ").split()
second_word_group_file = "wordlist.txt"

if os.path.isfile(second_word_group_file):
    with open(second_word_group_file, 'r') as file:
        second_word_group = file.read().splitlines()
else:
    print(f"'{second_word_group_file}' file not found. Please create the file or check the file name.")
    exit()

question_mark_count = sum(1 for word in first_word_group if '?' in word)
permutations = generate_permutations(second_word_group, question_mark_count)
results = []
for permutation in permutations:
    result = list(first_word_group)
    result_index = 0
    for word_index in range(len(result)):
        if '?' in result[word_index]:
            result[word_index] = permutation.split()[result_index]
            result_index += 1
    results.append(' '.join(result))

# Save the results to "mnemonic.txt"
program_directory = os.path.dirname(os.path.realpath(__file__))
with open(f'{program_directory}/mnemonic.txt', 'w') as file:
    file.write('\n'.join(results))
print(f"\nWordlist saved to '{program_directory}/mnemonic.txt' file.")

# Second code block used to search for a target address
def main():
    # Enable unaudited HD wallet features
    Account.enable_unaudited_hdwallet_features()

    # Get the filename for the mnemonic phrases (Use the "mnemonic.txt" file generated with the previous code)
    mnemonics_filename = "mnemonic.txt"  # Use the name of your "mnemonic.txt" file.

    # Get the target address to search for
    target_address = input("Enter the target address you want to search for: ")

    # Get the filename for the results (addresses) output
    results_filename = input("Enter the name of the file to save the addresses: ")

    try:
        # Read the file containing mnemonics
        with open(mnemonics_filename, 'r') as mnemonics:
            # Open the results file to write and append results
            with open(results_filename + ".txt", 'w+') as results:
                counter = 1
                found = False

                # Process each mnemonic
                for mnemonic in mnemonics:
                    if found:
                        break

                    try:
                        # Create an Ethereum account from the mnemonic
                        acct = Account.from_mnemonic(mnemonic.rstrip())

                        # Format the result as mnemonic:address
                        result_line = f"{mnemonic.rstrip()}:{acct.address}"

                        # Write the result to the results file
                        results.write(result_line + "\n")

                        # Print the result in green if the target address is found
                        if acct.address.lower() == target_address.lower():
                            print(colored(result_line + " (Found!)", 'green'))
                            found = True
                        else:
                            print(result_line)
                    except Exception as e:
                        # Handle exceptions (errors)
                        # Print the error message in red
                        print(colored(str(counter) + ": " + str(e) + "\n", 'red'))

                    counter += 1

                if found:
                    print("Target address found! Check the results in " + results_filename + ".txt file.")
                else:
                    print("Target address not found.")
    except KeyboardInterrupt:
        print("\nClosed")
        sys.exit(0)

if __name__ == "__main__":
    main()
