def encrypt_caesar(plain_text, shift):
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                base = ord('a')
                encrypted_text += chr((ord(char) - base + shift_amount) % 26 + base)
            else:
                base = ord('A')
                encrypted_text += chr((ord(char) - base + shift_amount) % 26 + base)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt_caesar(cipher_text, shift):
    return encrypt_caesar(cipher_text, -shift)

def main():
    while True:
        choice = input("Would you like to encrypt or decrypt a message? (enter 'encrypt' or 'decrypt', or 'exit' to quit): ").strip().lower()
        if choice == 'encrypt':
            message = input("Enter the message to encrypt: ").strip()
            shift = int(input("Enter the shift value: "))
            encrypted_message = encrypt_caesar(message, shift)
            print(f"Encrypted message: {encrypted_message}")
        elif choice == 'decrypt':
            message = input("Enter the message to decrypt: ").strip()
            shift = int(input("Enter the shift value: "))
            decrypted_message = decrypt_caesar(message, shift)
            print(f"Decrypted message: {decrypted_message}")
        elif choice == 'exit':
            print("Thankyou!")
            break
        else:
            print("Invalid choice. Please enter 'encrypt', 'decrypt', or 'exit'.")

if __name__ == "__main__":
    main()
