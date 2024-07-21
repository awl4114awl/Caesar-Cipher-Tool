def caesar_cipher(text, shift, encrypt=True):
  result = ""
  if not encrypt:
      shift = -shift
  for i in range(len(text)):
      char = text[i]
      if char.isalpha():
          shift_base = 65 if char.isupper() else 97
          result += chr((ord(char) + shift - shift_base) % 26 + shift_base)
      else:
          result += char
  return result
