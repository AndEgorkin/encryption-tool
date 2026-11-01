# Encryption Tool

Recomended python version: 3.14.8

A small Python CLI project implementing three classical ciphers:

- **Caesar cipher** — encryption, decryption and frequency-based key guessing.
- **Rail Fence cipher** — encryption, decryption and trigram-based brute force.
- **Vernam cipher** — XOR encryption and decryption with a generated key.

## Usage

1. Place your message in `input.txt`. For Vernam decryption, put the key on the second line.
2. Run the main Python file, e.g. `python encryption.py`.
3. Follow the prompts. The result is written to `output.txt`.

Keep `Freq_data.py` next to the main script to enable frequency-based key guessing.

> **Note:** This is an educational project, not a tool for secure communication. The current Vernam file format may not handle every control character reliably.
